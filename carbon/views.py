# carbon/views.py
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q, Sum, Avg, Count
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from datetime import date, datetime, timedelta
import json
import pandas as pd
from io import BytesIO

from .models import (
    CarbonCoefficient, CoefficientType, EmissionFactor, FuelType,
    InputCategory, InputData,
    GWPValues, ExcelReport,
    DynamicCarbonInput, SubScope  # Yeni modelleri ekledik
)
from .forms import (
    CarbonCoefficientForm, CoefficientTypeForm, EmissionFactorForm, FuelTypeForm,
    UserFirmAccessForm, BulkUploadForm, ReportGenerateForm,
    InputCategoryForm, ReportForm
)
from core.models import UserFirm, Firm, User

# Diğer view'larda da kullanmak için yardımcı fonksiyon
def get_user_firms(request):
    """Kullanıcının erişebileceği firmaları döndür"""
    if request.user.is_superuser:
        return Firm.objects.all()
    elif hasattr(request.user, 'user'):
        return Firm.objects.filter(user_associations__user=request.user.user)
    else:
        return Firm.objects.filter(user_associations__user=request.user)


@login_required
def api_get_options(request, option_type):
    """Dinamik seçenekleri döndür"""
    
    options = {
        'fuel_types': list(FuelType.objects.values('id', 'name')),
        'gas_types': [
            {'id': 'R410A', 'name': 'R410A (GWP: 2088)'},
            {'id': 'R32', 'name': 'R32 (GWP: 675)'},
            {'id': 'R404A', 'name': 'R404A (GWP: 3922)'},
        ],
        'material_types': list(CarbonCoefficient.objects.filter(
            scope=4, subscope='4.1'
        ).values('id', 'name')),
        'land_types': [
            {'id': 'forest', 'name': 'Orman'},
            {'id': 'agriculture', 'name': 'Tarım'},
            {'id': 'urban', 'name': 'Kentsel'},
        ],
        'change_types': [
            {'id': 'deforestation', 'name': 'Ormansızlaşma'},
            {'id': 'afforestation', 'name': 'Ağaçlandırma'},
            {'id': 'urbanization', 'name': 'Kentleşme'},
        ]
    }
    
    return JsonResponse(options.get(option_type, []), safe=False)

def calculate_co2e(scope, subscope, data):
    """CO2 eşdeğeri hesaplama"""
    
    # Her alt kapsam için özel hesaplama mantığı
    if scope == 1 and subscope == '1.1':
        # Sabit yanma
        fuel_type = FuelType.objects.get(id=data['fuel_type'])
        consumption = float(data['consumption'])
        return (consumption * fuel_type.co2_factor * fuel_type.density) / 1000000
        
    elif scope == 1 and subscope == '1.4':
        # Kaçak emisyonlar
        gwp = float(data['gwp'])
        leak_rate = float(data['leak_rate']) / 100
        capacity = float(data['gas_capacity'])
        quantity = float(data['quantity'])
        return (gwp * leak_rate * capacity * quantity) / 1000
        
    elif scope == 2 and subscope == '2.1':
        # Elektrik
        consumption = float(data['consumption'])
        grid_factor = 0.442  # kg CO2/kWh (Türkiye ortalaması)
        return (consumption * grid_factor) / 1000
        
    # Diğer hesaplamalar...
    
    return 0

@login_required
def api_recent_inputs(request):
    """Son girişleri getir"""
    
    firm_id = request.GET.get('firm')
    inputs = DynamicCarbonInput.objects.filter(
        firm_id=firm_id
    ).order_by('-datetime')[:20]
    
    data = []
    for inp in inputs:
        data.append({
            'id': inp.id,
            'datetime': inp.datetime.isoformat(),
            'scope': inp.scope,
            'subscope': f"{inp.subscope.code} - {inp.subscope.name}",
            'data': inp.data,
            'co2e_total': float(inp.co2e_total)
        })
    
    return JsonResponse(data, safe=False)


@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def coefficient_list_view(request):
    """Karbon katsayıları listesi"""
    
    # Filtreleme parametreleri
    scope = request.GET.get('scope')
    subscope = request.GET.get('subscope')
    coefficient_type = request.GET.get('coefficient_type')
    name_search = request.GET.get('name')
    
    # Temel sorgu
    coefficients = CarbonCoefficient.objects.all()
    
    # Filtreleri uygula
    if scope:
        coefficients = coefficients.filter(scope=scope)
    if subscope:
        coefficients = coefficients.filter(subscope=subscope)
    if coefficient_type:
        coefficients = coefficients.filter(coefficient_type=coefficient_type)
    if name_search:
        coefficients = coefficients.filter(name__icontains=name_search)
    
    # Tarihe göre sırala
    coefficients = coefficients.order_by('scope', 'subscope', 'coefficient_type', 'name', '-valid_from')
    
    context = {
        'coefficients': coefficients,
        'scope_choices': CarbonCoefficient.SCOPE_CHOICES,
        'subscope_choices': CarbonCoefficient.SUBSCOPE_CHOICES,
        'coefficient_type_choices': CarbonCoefficient.COEFFICIENT_TYPE_CHOICES,
        'selected_scope': scope,
        'selected_subscope': subscope,
        'selected_coefficient_type': coefficient_type,
        'name_search': name_search,
    }
    
    return render(request, 'carbon/coefficient_list.html', context)


@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def coefficient_create_view(request):
    """Yeni karbon katsayısı ekleme"""
    
    if request.method == 'POST':
        form = CarbonCoefficientForm(request.POST)
        if form.is_valid():
            coefficient = form.save(commit=False)
            coefficient.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            coefficient.save()
            messages.success(request, "Karbon katsayısı başarıyla eklendi.")
            return redirect('carbon:coefficient-list')
    else:
        form = CarbonCoefficientForm()
    
    context = {
        'form': form,
        'title': 'Yeni Karbon Katsayısı',
        'subscope_data': json.dumps(dict(CarbonCoefficient.SUBSCOPE_CHOICES)),
    }
    
    return render(request, 'carbon/coefficient_form.html', context)


@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def coefficient_update_view(request, pk):
    """Karbon katsayısı güncelleme"""
    
    coefficient = get_object_or_404(CarbonCoefficient, pk=pk)
    
    if request.method == 'POST':
        form = CarbonCoefficientForm(request.POST, instance=coefficient)
        if form.is_valid():
            form.save()
            messages.success(request, "Karbon katsayısı başarıyla güncellendi.")
            return redirect('carbon:coefficient-list')
    else:
        form = CarbonCoefficientForm(instance=coefficient)
    
    context = {
        'form': form,
        'title': 'Karbon Katsayısı Güncelle',
        'coefficient': coefficient,
        'subscope_data': json.dumps(dict(CarbonCoefficient.SUBSCOPE_CHOICES)),
    }
    
    return render(request, 'carbon/coefficient_form.html', context)


@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def coefficient_delete_view(request, pk):
    """Karbon katsayısı silme"""
    
    coefficient = get_object_or_404(CarbonCoefficient, pk=pk)
    
    if request.method == 'POST':
        coefficient.delete()
        messages.success(request, "Karbon katsayısı başarıyla silindi.")
        return redirect('carbon:coefficient-list')
    
    context = {
        'coefficient': coefficient,
    }
    
    return render(request, 'carbon/coefficient_confirm_delete.html', context)


@login_required
def ajax_get_subscopes(request):
    """AJAX ile alt kapsam seçeneklerini getir"""
    
    scope = request.GET.get('scope')
    subscopes = []
    
    if scope:
        for code, label in CarbonCoefficient.SUBSCOPE_CHOICES:
            if code.startswith(scope + '.'):
                subscopes.append({'code': code, 'label': label})
    
    return JsonResponse({'subscopes': subscopes})


@login_required
def ajax_get_coefficient_types(request):
    """AJAX ile belirli bir alt kapsam için uygun katsayı türlerini getir"""
    
    subscope = request.GET.get('subscope')
    
    # Alt kapsama göre uygun katsayı türlerini belirle
    coefficient_types_map = {
        '1.1': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_M3'],
        '1.2': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_TON_LT'],
        '1.3': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
        '1.4': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
        '1.5': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
        '2.1': ['EF_TCO2_MWH'],
        '3.1': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
        '3.2': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
        '3.3': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
        '3.4': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_TON_LT'],
        '3.5': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT', 'YOGUNLUK_TON_LT', 'EF_KG_CO2E_ODA'],
        '4.1': ['EF_KG_CO2_KG'],
        '4.2': ['EF_KG_CO2_KG', 'EF_TCO2E_KG'],
        '4.3': ['EF_KG_CO2E_KWH', 'EF_KG_CO2E_M3', 'EF_KG_CO2_TON', 'EF_KG_CO2_M3', 'EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
    }
    
    types = []
    if subscope and subscope in coefficient_types_map:
        allowed_types = coefficient_types_map[subscope]
        for code, label in CarbonCoefficient.COEFFICIENT_TYPE_CHOICES:
            if code in allowed_types:
                types.append({'code': code, 'label': label})
    
    return JsonResponse({'coefficient_types': types})


@login_required
@permission_required('carbon.view_input_carbon', raise_exception=True)
def dynamic_input_view(request):
    """Dinamik karbon girişi sayfası"""
    
    # Kullanıcının erişebileceği firmalar
    if request.user.is_superuser:
        user_firms = Firm.objects.all()
    elif hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
    else:
        user_firms = Firm.objects.filter(user_associations__user=request.user)
    
    context = {
        'user_firms': user_firms,
    }
    
    return render(request, 'carbon/dynamic_input.html', context)


@login_required
@require_http_methods(["POST", "DELETE"])
def api_dynamic_input(request, input_id=None):
    """Dinamik veri girişi kaydet veya sil"""
    
    if request.method == 'DELETE' and input_id:
        try:
            input_obj = DynamicCarbonInput.objects.get(id=input_id)
            # Yetki kontrolü
            if hasattr(request.user, 'user'):
                user_firms = Firm.objects.filter(user_associations__user=request.user.user)
            else:
                user_firms = Firm.objects.filter(user_associations__user=request.user)
            
            if input_obj.firm not in user_firms and not request.user.is_superuser:
                return JsonResponse({'success': False, 'message': 'Yetkiniz yok'})
            
            input_obj.delete()
            return JsonResponse({'success': True})
        except DynamicCarbonInput.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Kayıt bulunamadı'})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        
        # Alt kapsam bul veya oluştur
        subscope, _ = SubScope.objects.get_or_create(
            scope=data['scope'],
            code=data['subscope'],
            defaults={'name': f"Alt Kapsam {data['subscope']}"}
        )
        
        # CO2 hesaplama
        co2e_total = calculate_co2e(data['scope'], data['subscope'], data['data'])
        
        # Kaydet
        input_obj = DynamicCarbonInput.objects.create(
            firm_id=data['firm'],
            datetime=data['datetime'],
            scope=data['scope'],
            subscope=subscope,
            data=data['data'],
            co2e_total=co2e_total,
            created_by=request.user.user if hasattr(request.user, 'user') else request.user
        )
        
        return JsonResponse({
            'success': True,
            'id': input_obj.id,
            'co2e_total': float(co2e_total)
        })
    
    return JsonResponse({'success': False, 'message': 'Invalid method'})

# Dashboard View
@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def dashboard_view(request):
    """Karbon yönetim dashboard'u"""
    context = {}
    
    # Kullanıcının firmasını al
    user_firms = Firm.objects.filter(user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user)
    
    # Firma seçimi
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.warning(request, "Lütfen önce bir firma ile ilişkilendirilmeniz gerekmektedir.")
        return redirect('carbon:management-list')
    
    context['selected_firm'] = selected_firm
    context['user_firms'] = user_firms
    
    # Mevcut ay ve önceki ay
    current_date = date.today()
    current_year = current_date.year
    current_month = current_date.month
    
    if current_month == 1:
        prev_month = 12
        prev_year = current_year - 1
    else:
        prev_month = current_month - 1
        prev_year = current_year
    
    # Mevcut ay toplamları
    scope1_current = Scope1Data.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope2_current = Scope2Data.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope3_current = Scope3Data.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope4_current = Scope4Data.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    total_current = scope1_current + scope2_current + scope3_current + scope4_current
    
    # Önceki ay toplamları (karşılaştırma için)
    scope1_prev = Scope1Data.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope2_prev = Scope2Data.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope3_prev = Scope3Data.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope4_prev = Scope4Data.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    total_prev = scope1_prev + scope2_prev + scope3_prev + scope4_prev
    
    # Değişim hesaplama
    if total_prev > 0:
        emission_change = ((total_current - total_prev) / total_prev) * 100
    else:
        emission_change = 0
    
    # Yüzde hesaplamaları
    if total_current > 0:
        scope1_percentage = (scope1_current / total_current) * 100
        scope2_percentage = (scope2_current / total_current) * 100
        scope3_percentage = (scope3_current / total_current) * 100
        scope4_percentage = (scope4_current / total_current) * 100
    else:
        scope1_percentage = scope2_percentage = scope3_percentage = scope4_percentage = 0
    
    # Son 6 aylık trend verisi (grafik için)
    chart_labels = []
    scope1_data = []
    scope2_data = []
    scope3_data = []
    scope4_data = []
    
    for i in range(5, -1, -1):
        target_date = current_date - timedelta(days=i*30)
        month_year = target_date.strftime("%B %Y")
        chart_labels.append(month_year)
        
        # Her ay için toplamları al
        s1 = Scope1Data.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s2 = Scope2Data.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s3 = Scope3Data.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s4 = Scope4Data.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        scope1_data.append(float(s1))
        scope2_data.append(float(s2))
        scope3_data.append(float(s3))
        scope4_data.append(float(s4))
    
    # Son veri girişleri
    recent_entries = []
    
    # Scope 1 girişleri
    for entry in Scope1Data.objects.filter(firm=selected_firm).order_by('-created_at')[:3]:
        recent_entries.append({
            'created_at': entry.created_at,
            'scope': 'Kapsam 1',
            'location': entry.location,
            'value': entry.consumption_value,
            'unit': entry.consumption_unit,
            'co2e': entry.total_co2e,
            'edit_url': f"/carbon/scope1/{entry.pk}/update/"
        })
    
    # Scope 2 girişleri
    for entry in Scope2Data.objects.filter(firm=selected_firm).order_by('-created_at')[:3]:
        recent_entries.append({
            'created_at': entry.created_at,
            'scope': 'Kapsam 2',
            'location': entry.location,
            'value': entry.electricity_kwh,
            'unit': 'kWh',
            'co2e': entry.total_co2e,
            'edit_url': f"/carbon/scope2/{entry.pk}/update/"
        })
    
    # Girişleri tarihe göre sırala
    recent_entries.sort(key=lambda x: x['created_at'], reverse=True)
    recent_entries = recent_entries[:10]  # Son 10 giriş
    
    # Son raporlar
    recent_reports = Report.objects.filter(firm=selected_firm).order_by('-report_date')[:5]
    
    # Context'e ekle
    context.update({
        'total_emissions': total_current,
        'emission_change': emission_change,
        'scope1_total': scope1_current,
        'scope2_total': scope2_current,
        'scope3_total': scope3_current,
        'scope4_total': scope4_current,
        'scope1_percentage': scope1_percentage,
        'scope2_percentage': scope2_percentage,
        'scope3_percentage': scope3_percentage,
        'scope4_percentage': scope4_percentage,
        'data_completeness': 85,  # Örnek değer
        'pending_entries': 3,  # Örnek değer
        'chart_labels': json.dumps(chart_labels),
        'scope1_data': json.dumps(scope1_data),
        'scope2_data': json.dumps(scope2_data),
        'scope3_data': json.dumps(scope3_data),
        'scope4_data': json.dumps(scope4_data),
        'recent_entries': recent_entries,
        'recent_reports': recent_reports,
    })
    
    return render(request, 'carbon/dashboard.html', context)

# TOPLU VERİ YÜKLEME
@login_required
@permission_required('carbon.add_inputdata', raise_exception=True)
def bulk_upload_view(request):
    """Excel ile toplu veri yükleme"""
    if request.method == 'POST':
        form = BulkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            scope = form.cleaned_data['scope']
            
            # Excel dosyasını oku
            df = pd.read_excel(excel_file)
            
            # Scope'a göre işle
            if scope == 'scope1':
                process_scope1_excel(df, request.user)
            elif scope == 'scope2':
                process_scope2_excel(df, request.user)
            # ... diğer scope'lar
            
            messages.success(request, f"{len(df)} satır veri başarıyla yüklendi.")
            return redirect('carbon:dashboard')
    else:
        form = BulkUploadForm()
    
    return render(request, 'carbon/bulk_upload.html', {'form': form})

@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def management_list_view(request):
    """Karbon yönetim ana sayfası - Katsayı yönetimi dahil"""
    
    # Filtreleme parametreleri
    scope = request.GET.get('scope')
    subscope = request.GET.get('subscope')
    valid_from = request.GET.get('valid_from')
    valid_to = request.GET.get('valid_to')
    
    # Katsayıları getir
    coefficients = CarbonCoefficient.objects.all()
    
    # Filtreleri uygula
    if scope:
        coefficients = coefficients.filter(scope=scope)
    if subscope:
        coefficients = coefficients.filter(subscope=subscope)
    if valid_from:
        coefficients = coefficients.filter(valid_from__gte=valid_from)
    if valid_to:
        coefficients = coefficients.filter(valid_to__lte=valid_to)
    
    # Tarihe göre sırala
    coefficients = coefficients.order_by('scope', 'subscope', 'coefficient_type', 'name', '-valid_from')
    
    context = {
        'coefficients': coefficients,
        'subscope_choices': CarbonCoefficient.SUBSCOPE_CHOICES,
        'selected_scope': scope,
        'selected_subscope': subscope,
        'selected_valid_from': valid_from,
        'selected_valid_to': valid_to,
    }
    
    # Kullanıcı-Firma ilişkilendirme formu (eğer yetkisi varsa)
    if request.user.has_perm('carbon.can_manage_user_firm_access'):
        if request.method == 'POST':
            form = UserFirmAccessForm(request.POST)
            if form.is_valid():
                selected_user = form.cleaned_data['user']
                selected_firm = form.cleaned_data['firm']
                try:
                    UserFirm.objects.get(user=selected_user, firm=selected_firm)
                    messages.info(request, "Bu kullanıcı zaten bu firmaya atanmış.")
                except UserFirm.DoesNotExist:
                    UserFirm.objects.create(user=selected_user, firm=selected_firm, create=timezone.now())
                    messages.success(request, f"'{selected_user.name}' kullanıcısı '{selected_firm.name}' firmasına başarıyla atandı.")
                return redirect('carbon:management-list')
        else:
            form = UserFirmAccessForm()
        context['user_firm_form'] = form
    
    return render(request, 'carbon/management_list.html', context)


@login_required
@permission_required('carbon.add_emissionfactor', raise_exception=True)
def emissionfactor_create_view(request):
    """Emisyon faktörü oluşturma"""
    if request.method == 'POST':
        form = EmissionFactorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Emisyon faktörü başarıyla oluşturuldu.")
            return redirect('carbon:management-list')
    else:
        form = EmissionFactorForm()
    
    return render(request, 'carbon/emissionfactor_form.html', {
        'form': form,
        'title': 'Yeni Emisyon Faktörü'
    })

@login_required
@permission_required('carbon.change_emissionfactor', raise_exception=True)
def emissionfactor_update_view(request, pk):
    """Emisyon faktörü güncelleme"""
    factor = get_object_or_404(EmissionFactor, pk=pk)
    
    if request.method == 'POST':
        form = EmissionFactorForm(request.POST, instance=factor)
        if form.is_valid():
            form.save()
            messages.success(request, "Emisyon faktörü güncellendi.")
            return redirect('carbon:management-list')
    else:
        form = EmissionFactorForm(instance=factor)
    
    return render(request, 'carbon/emissionfactor_form.html', {
        'form': form,
        'title': 'Emisyon Faktörü Güncelle'
    })

@login_required
@permission_required('carbon.delete_emissionfactor', raise_exception=True)
def emissionfactor_delete_view(request, pk):
    """Emisyon faktörü silme"""
    factor = get_object_or_404(EmissionFactor, pk=pk)
    
    if request.method == 'POST':
        factor.delete()
        messages.success(request, "Emisyon faktörü silindi.")
        return redirect('carbon:management-list')
    
    return render(request, 'carbon/emissionfactor_confirm_delete.html', {
        'factor': factor
    })

# YAKIT TÜRÜ VIEW'LARI
@login_required
@permission_required('carbon.add_fueltype', raise_exception=True)
def fueltype_create_view(request):
    """Yakıt türü oluşturma"""
    if request.method == 'POST':
        form = FuelTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yakıt türü başarıyla oluşturuldu.")
            return redirect('carbon:management-list')
    else:
        form = FuelTypeForm()
    
    return render(request, 'carbon/fueltype_form.html', {
        'form': form,
        'title': 'Yeni Yakıt Türü'
    })

@login_required
@permission_required('carbon.change_fueltype', raise_exception=True)
def fueltype_update_view(request, pk):
    """Yakıt türü güncelleme"""
    fuel_type = get_object_or_404(FuelType, pk=pk)
    
    if request.method == 'POST':
        form = FuelTypeForm(request.POST, instance=fuel_type)
        if form.is_valid():
            form.save()
            messages.success(request, "Yakıt türü güncellendi.")
            return redirect('carbon:management-list')
    else:
        form = FuelTypeForm(instance=fuel_type)
    
    return render(request, 'carbon/fueltype_form.html', {
        'form': form,
        'title': 'Yakıt Türü Güncelle'
    })

@login_required
@permission_required('carbon.delete_fueltype', raise_exception=True)
def fueltype_delete_view(request, pk):
    """Yakıt türü silme"""
    fuel_type = get_object_or_404(FuelType, pk=pk)
    
    if request.method == 'POST':
        fuel_type.delete()
        messages.success(request, "Yakıt türü silindi.")
        return redirect('carbon:management-list')
    
    return render(request, 'carbon/fueltype_confirm_delete.html', {
        'fuel_type': fuel_type
    })


@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_generate_view(request):
    """Anlık karbon raporu oluştur (kaydetmeden)"""
    
    if request.method == 'POST':
        form = ReportForm(request.POST, user=request.user)
        if form.is_valid():
            firm = form.cleaned_data['firm']
            report_date = form.cleaned_data['report_date']
            
            # Rapor dönemini belirle (son 1 yıl)
            report_period_end = report_date
            report_period_start = report_date - timedelta(days=365)
            
            # Verileri topla (veritabanından)
            scope1_data = Scope1Data.objects.filter(
                firm=firm,
                period_year__gte=report_period_start.year,
                period_year__lte=report_period_end.year
            ).aggregate(
                total=Sum('total_co2e')
            )['total'] or 0
            
            scope2_data = Scope2Data.objects.filter(
                firm=firm,
                period_year__gte=report_period_start.year,
                period_year__lte=report_period_end.year
            ).aggregate(
                total=Sum('total_co2e')
            )['total'] or 0
            
            scope3_data = Scope3Data.objects.filter(
                firm=firm,
                period_year__gte=report_period_start.year,
                period_year__lte=report_period_end.year
            ).aggregate(
                total=Sum('total_co2e')
            )['total'] or 0
            
            scope4_data = Scope4Data.objects.filter(
                firm=firm,
                period_year__gte=report_period_start.year,
                period_year__lte=report_period_end.year
            ).aggregate(
                total=Sum('total_co2e')
            )['total'] or 0
            
            # Toplam emisyon
            total_emission = scope1_data + scope2_data + scope3_data + scope4_data
            
            # Direct (Kapsam 1) ve Indirect (Kapsam 2+3) oranları
            direct_emissions = scope1_data
            indirect_emissions = scope2_data + scope3_data + scope4_data
            
            if total_emission > 0:
                direct_ratio = (direct_emissions / total_emission) * 100
                indirect_ratio = (indirect_emissions / total_emission) * 100
            else:
                direct_ratio = 0
                indirect_ratio = 0
            
            # Rapor verilerini hazırla (kaydetmeden)
            report_data = {
                'firm': firm,
                'report_date': report_date,
                'report_period_start': report_period_start,
                'report_period_end': report_period_end,
                'scope1_total': scope1_data,
                'scope2_total': scope2_data,
                'scope3_total': scope3_data,
                'scope4_total': scope4_data,
                'total_emission': total_emission,
                'direct_ratio': direct_ratio,
                'indirect_ratio': indirect_ratio,
            }
            
            # Excel'e aktar düğmesine basıldıysa
            if 'export_excel' in request.POST:
                return export_report_to_excel(report_data)
            
            # Raporu göster
            return render(request, 'carbon/report_display.html', {
                'report': report_data,
                'form': form
            })
    else:
        form = ReportForm(user=request.user)
    
    return render(request, 'carbon/report_generate.html', {
        'form': form
    })


def export_report_to_excel(report_data):
    """Raporu Excel'e aktar"""
    output = BytesIO()
    
    # Excel writer oluştur
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Özet sayfası
        summary_data = {
            'Bilgi': ['Firma', 'Rapor Tarihi', 'Dönem Başlangıç', 'Dönem Bitiş'],
            'Değer': [
                report_data['firm'].name,
                report_data['report_date'].strftime('%d.%m.%Y'),
                report_data['report_period_start'].strftime('%d.%m.%Y'),
                report_data['report_period_end'].strftime('%d.%m.%Y')
            ]
        }
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name='Özet', index=False)
        
        # Emisyon verileri
        emissions_data = {
            'Kapsam': ['Kapsam 1', 'Kapsam 2', 'Kapsam 3', 'Kapsam 4', 'TOPLAM'],
            'Emisyon (tCO2e)': [
                report_data['scope1_total'],
                report_data['scope2_total'],
                report_data['scope3_total'],
                report_data['scope4_total'],
                report_data['total_emission']
            ],
            'Oran (%)': [
                report_data['scope1_total'] / report_data['total_emission'] * 100 if report_data['total_emission'] > 0 else 0,
                report_data['scope2_total'] / report_data['total_emission'] * 100 if report_data['total_emission'] > 0 else 0,
                report_data['scope3_total'] / report_data['total_emission'] * 100 if report_data['total_emission'] > 0 else 0,
                report_data['scope4_total'] / report_data['total_emission'] * 100 if report_data['total_emission'] > 0 else 0,
                100 if report_data['total_emission'] > 0 else 0
            ]
        }
        df_emissions = pd.DataFrame(emissions_data)
        df_emissions.to_excel(writer, sheet_name='Emisyonlar', index=False)
    
    # Excel dosyasını indir
    output.seek(0)
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    filename = f"Karbon_Raporu_{report_data['firm'].name}_{report_data['report_date'].strftime('%Y%m%d')}.xlsx"
    response['Content-Disposition'] = f'attachment; filename={filename}'
    
    return response

@login_required
@permission_required('carbon.add_report', raise_exception=True)
def report_generate_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_date = form.cleaned_data['report_date']
            
            # Kullanıcının firmasını bul
            if request.user.is_superuser:
                firm = Firm.objects.first()
            elif hasattr(request.user, 'user'):
                firm = Firm.objects.filter(user_associations__user=request.user.user).first()
            else:
                firm = Firm.objects.filter(user_associations__user=request.user).first()
            
            if not firm:
                raise PermissionDenied("No associated firm found.")
            
            # InputData'dan verileri al
            inputs = InputData.objects.filter(firm=firm, period_end__lte=report_date)
            
            total_co2e = 0.0
            direct_emissions = 0.0
            indirect_emissions = 0.0
            details = {}
            
            for input_data in inputs:
                factor = EmissionFactor.objects.filter(
                    Q(category=input_data.category.scope),
                    Q(valid_from__lte=report_date),
                    Q(valid_to__gte=report_date) | Q(valid_to__isnull=True)
                ).order_by('-valid_from').first()
                
                if factor:
                    co2e = input_data.value * factor.value
                    total_co2e += co2e
                    if input_data.category.scope in ['KAPSAM_1', 'KAPSAM_2']:
                        direct_emissions += co2e
                    else:
                        indirect_emissions += co2e
                    details[input_data.id] = {
                        'input_value': input_data.value,
                        'factor_value': factor.value,
                        'calculated_co2e': co2e
                    }
            
            direct_ratio = (direct_emissions / total_co2e * 100) if total_co2e > 0 else 0.0
            indirect_ratio = (indirect_emissions / total_co2e * 100) if total_co2e > 0 else 0.0

            if hasattr(request.user, 'user'):
                generated_by_user = request.user.user
            elif hasattr(request.user, 'profile'):
                generated_by_user = request.user.profile
            else:
                generated_by_user = None
            report_period_end = report_date
            report_period_start = report_date - timedelta(days=365)  # Son 1 yıl
            report = Report.objects.create(
                firm=firm,
                report_date=report_date,
                report_period_start=report_period_start,
                report_period_end=report_period_end,
                generated_by=generated_by_user,
                total_co2e=0,
                direct_ratio=0,
                indirect_ratio=0,
                scope1_total=0,
                scope2_total=0,
                scope3_total=0,
                scope4_total=0,
                scope5_total=0,
                scope6_total=0,
            )
            return redirect('carbon:report-list')
    else:
        form = ReportForm(initial={'report_date': timezone.now().date()})
    
    # ÖNEMLİ: GET request için mutlaka form'u render et
    return render(request, 'carbon/report_form.html', {'form': form})

@login_required
@permission_required('carbon.view_report', raise_exception=True)
def report_detail_view(request, pk):
    """Rapor detayı"""
    report = get_object_or_404(Report, pk=pk)
    
    # Yetki kontrolü
    if hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
        if report.firm not in user_firms:
            raise PermissionDenied
    
    return render(request, 'carbon/report_detail.html', {
        'report': report
    })

@login_required
@permission_required('carbon.view_report', raise_exception=True)
def report_download_view(request, pk):
    """Raporu indir"""
    report = get_object_or_404(Report, pk=pk)
    
    # Yetki kontrolü
    if hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
        if report.firm not in user_firms:
            raise PermissionDenied
    
    # Excel olarak indir
    import pandas as pd
    from io import BytesIO
    
    output = BytesIO()
    
    # Rapor verilerini DataFrame'e dönüştür
    data = {
        'Kapsam': ['Kapsam 1', 'Kapsam 2', 'Kapsam 3', 'Kapsam 4', 'Kapsam 5', 'Kapsam 6', 'TOPLAM'],
        'CO2e (ton)': [
            float(report.scope1_total),
            float(report.scope2_total),
            float(report.scope3_total),
            float(report.scope4_total),
            float(report.scope5_total),
            float(report.scope6_total),
            float(report.total_co2e)
        ]
    }
    
    df = pd.DataFrame(data)
    
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Özet', index=False)
        
        # Detaylı veri sayfaları eklenebilir
    
    output.seek(0)
    
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename=karbon_raporu_{report.pk}.xlsx'
    
    return response

# API VIEW'LARI
@login_required
def api_chart_data(request):
    """Grafik verileri API'si"""
    # Dashboard için grafik verilerini döndür
    return JsonResponse({
        'labels': [],
        'datasets': []
    })


@login_required
def dashboard_view(request):
    """Basit dashboard view"""
    return render(request, 'carbon/dashboard.html', {})

@login_required
def download_template_view(request, scope):
    """Excel şablon indirme - şimdilik boş"""
    messages.info(request, "Bu özellik henüz hazır değil.")
    return redirect('carbon:management-list')

@login_required
def bulk_upload_view(request):
    """Toplu veri yükleme - şimdilik boş"""
    messages.info(request, "Bu özellik henüz hazır değil.")
    return redirect('carbon:management-list')

@login_required
def fueltype_create_view(request):
    return redirect('carbon:management-list')

@login_required
def fueltype_update_view(request, pk):
    return redirect('carbon:management-list')

@login_required
def fueltype_delete_view(request, pk):
    return redirect('carbon:management-list')

# API view'ları
@login_required
def api_calculate_emission(request):
    from django.http import JsonResponse
    return JsonResponse({'status': 'not implemented'})

@login_required
def api_get_fuel_factors(request, fuel_id):
    from django.http import JsonResponse
    return JsonResponse({'status': 'not implemented'})

@login_required
def api_chart_data(request):
    from django.http import JsonResponse
    return JsonResponse({'status': 'not implemented'})

@login_required
def report_download_view(request, pk):
    messages.info(request, "İndirme özelliği henüz hazır değil.")
    return redirect('carbon:report-list')


@login_required
@permission_required('carbon.view_input_carbon', raise_exception=True)
def input_list_view(request):
    """Karbon girdi sayfası - yeni dinamik sisteme yönlendir"""
    return redirect('carbon:dynamic-input')


@login_required
def report_list_view(request):
    """Rapor listesi görüntüleme"""
    
    # Kullanıcının yetkili olduğu firmaları al
    if request.user.is_superuser:
        user_firms = Firm.objects.all()
    else:
        if hasattr(request.user, 'user'):
            user_profile = request.user.user
            user_firms = Firm.objects.filter(user_associations__user=user_profile)
        else:
            user_firms = Firm.objects.none()
    
    # Firma seçimi
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        try:
            selected_firm = Firm.objects.get(pk=selected_firm_id)
            if not request.user.is_superuser and selected_firm not in user_firms:
                messages.error(request, "Bu firmaya erişim yetkiniz yok!")
                selected_firm = user_firms.first() if user_firms else None
        except Firm.DoesNotExist:
            selected_firm = user_firms.first() if user_firms else None
    else:
        selected_firm = user_firms.first() if user_firms else None
    
    # Rapor listesi
    if selected_firm:
        reports = Report.objects.filter(firm=selected_firm).order_by('-report_date')
    else:
        reports = Report.objects.none()
    
    # İstatistikler
    total_emissions = 0
    latest_report = None
    
    if reports.exists():
        from django.db.models import Sum
        total_emissions = reports.aggregate(
            total=Sum('total_co2e')
        )['total'] or 0
        latest_report = reports.first()
    
    context = {
        'reports': reports,
        'user_firms': user_firms,
        'selected_firm': selected_firm,
        'total_emissions': total_emissions,
        'latest_report': latest_report,
    }
    
    return render(request, 'carbon/report_list.html', context)


@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_list_view(request):
    """Geçici rapor sayfası - ileride geliştirilecek"""
    return HttpResponse("""
        <html>
        <body style="padding: 50px; font-family: Arial;">
            <h1>Karbon Rapor Modülü</h1>
            <p>Bu modül henüz geliştirme aşamasındadır.</p>
            <a href="/portal/">Portal'a Dön</a>
        </body>
        </html>
    """)

@login_required
def excel_report_view(request):
    """Excel formatında karbon raporu görüntüleme"""
    
    # Firma seç
    if request.user.is_superuser:
        firms = Firm.objects.all()
    else:
        if hasattr(request.user, 'user'):
            firms = Firm.objects.filter(user_associations__user=request.user.user)
        else:
            firms = Firm.objects.none()
    
    selected_firm_id = request.GET.get('firm_id')
    selected_firm = None
    report = None
    scope1_data = None
    scope2_data = None
    scope4_data = None
    
    if selected_firm_id:
        selected_firm = get_object_or_404(Firm, pk=selected_firm_id)
        
        # Rapor getir veya oluştur
        year = int(request.GET.get('year', 2025))
        month = int(request.GET.get('month', 1))
        
        report = ExcelReport.objects.filter(
            firm=selected_firm,
            year=year,
            month=month
        ).first()
        
        if report:
            # Kapsam detaylarını getir
            scope1_data = Scope1Excel.objects.filter(
                firm=selected_firm,
                year=year,
                month=month
            )
            scope2_data = Scope2Excel.objects.filter(
                firm=selected_firm,
                year=year,
                month=month
            )
            scope4_data = Scope4Excel.objects.filter(
                firm=selected_firm,
                year=year,
                month=month
            )
    
    context = {
        'firms': firms,
        'selected_firm': selected_firm,
        'report': report,
        'scope1_data': scope1_data,
        'scope2_data': scope2_data,
        'scope4_data': scope4_data,
    }
    
    return render(request, 'carbon/excel_report.html', context)