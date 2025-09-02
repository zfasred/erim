# carbon/views.py
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q, Sum, Avg, Count
from django.http import JsonResponse, HttpResponse
from datetime import date, datetime, timedelta
import json
import pandas as pd
from io import BytesIO

from .models import (
    CoefficientType, EmissionFactor, FuelType,
    Scope1Data, Scope2Data, Scope3Data, Scope4Data,
    InputCategory, InputData, Report
)
from .forms import (
    CoefficientTypeForm, EmissionFactorForm, FuelTypeForm,
    Scope1DataForm, Scope2DataForm, Scope3DataForm, Scope4DataForm,
    UserFirmAccessForm, BulkUploadForm, ReportGenerateForm,
    InputCategoryForm, InputDataForm, ReportForm
)
from core.models import UserFirm, Firm

# Diğer view'larda da kullanmak için yardımcı fonksiyon
def get_user_firms(request):
    """Kullanıcının erişebileceği firmaları döndür"""
    if request.user.is_superuser:
        return Firm.objects.all()
    elif hasattr(request.user, 'user'):
        return Firm.objects.filter(user_associations__user=request.user.user)
    else:
        return Firm.objects.filter(user_associations__user=request.user)

# Dashboard View
@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def dashboard_view(request):
    """Karbon yönetim dashboard'u"""
    context = {}
    
    # Kullanıcının firmasını al
    user_firms = Firm.objects.filter(userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user)
    
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

# KAPSAM 1 VIEW'LARI
@login_required
@permission_required('carbon.add_scope1data', raise_exception=True)
def scope1_create_view(request):
    """Kapsam 1 veri girişi"""
    # Kullanıcının firmasını al
    user_firms = Firm.objects.filter(userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user)
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope1DataForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope1_data = form.save(commit=False)
            scope1_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope1_data.save()
            messages.success(request, "Kapsam 1 verisi başarıyla kaydedildi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope1DataForm(firm=selected_firm)
    
    return render(request, 'carbon/scope1_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 1 - Doğrudan Emisyon Veri Girişi'
    })

@login_required
@permission_required('carbon.change_scope1data', raise_exception=True)
def scope1_update_view(request, pk):
    """Kapsam 1 veri güncelleme"""
    scope1_data = get_object_or_404(Scope1Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user)
    if scope1_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope1DataForm(request.POST, instance=scope1_data, firm=scope1_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 1 verisi güncellendi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope1DataForm(instance=scope1_data, firm=scope1_data.firm)
    
    return render(request, 'carbon/scope1_form.html', {
        'form': form,
        'firm': scope1_data.firm,
        'title': 'Kapsam 1 Veri Güncelleme'
    })

# KAPSAM 2 VIEW'LARI
@login_required
@permission_required('carbon.add_scope2data', raise_exception=True)
def scope2_create_view(request):
    """Kapsam 2 veri girişi"""
    user_firms = Firm.objects.filter(userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user)
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope2DataForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope2_data = form.save(commit=False)
            scope2_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope2_data.save()
            messages.success(request, "Kapsam 2 verisi başarıyla kaydedildi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope2DataForm(firm=selected_firm)
    
    return render(request, 'carbon/scope2_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 2 - Elektrik Tüketimi Veri Girişi'
    })

# Benzer şekilde Kapsam 3 ve 4 için view'lar...

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

def process_scope1_excel(df, user):
    """Scope 1 Excel verilerini işle"""
    # Excel'deki sütun isimlerini kontrol et ve veritabanına kaydet
    for index, row in df.iterrows():
        try:
            fuel_type = FuelType.objects.get(name=row['Yakıt Türü'])
            firm = Firm.objects.get(name=row['Firma'])
            
            Scope1Data.objects.create(
                firm=firm,
                combustion_type='stationary',
                location=row['Lokasyon'],
                fuel_type=fuel_type,
                consumption_value=row['Tüketim'],
                consumption_unit=row['Birim'],
                period_year=row['Yıl'],
                period_month=row['Ay'],
                created_by=user.user if hasattr(user, 'user') else user
            )
        except Exception as e:
            # Hataları logla
            print(f"Satır {index} işlenirken hata: {e}")

# Mevcut view'larınızı koruyorum
@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def management_list_view(request):
    factors = EmissionFactor.objects.all()
    types = CoefficientType.objects.all()
    fuel_types = FuelType.objects.all()
    context = {
        'factors': factors, 
        'types': types,
        'fuel_types': fuel_types
    }

    if request.user.has_perm('carbon.can_manage_user_firm_access'):
        if request.method == 'POST':
            form = UserFirmAccessForm(request.POST)
            if form.is_valid():
                selected_user = form.cleaned_data['user']
                selected_firm = form.cleaned_data['firm']
                try:
                    UserFirm.objects.get(user=selected_user, firm=selected_firm)
                except UserFirm.DoesNotExist:
                    UserFirm.objects.create(user=selected_user, firm=selected_firm, create=timezone.now())
                    messages.success(request, f"'{selected_user.username}' kullanıcısı '{selected_firm.name}' firmasına başarıyla atandı.")
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

# KAPSAM 1 LİSTE VIEW'I
@login_required
@permission_required('carbon.view_scope1data', raise_exception=True)
def scope1_list_view(request):
    """Kapsam 1 verilerini listele"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope1_data = Scope1Data.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope1_data = Scope1Data.objects.none()
    
    return render(request, 'carbon/scope1_list.html', {
        'scope1_data': scope1_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.delete_scope1data', raise_exception=True)
def scope1_delete_view(request, pk):
    """Kapsam 1 veri silme"""
    scope1_data = get_object_or_404(Scope1Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope1_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        scope1_data.delete()
        messages.success(request, "Kapsam 1 verisi silindi.")
        return redirect('carbon:scope1-list')
    
    return render(request, 'carbon/scope1_confirm_delete.html', {
        'scope1_data': scope1_data
    })

# KAPSAM 2 VIEW'LARI
@login_required
@permission_required('carbon.view_scope2data', raise_exception=True)
def scope2_list_view(request):
    """Kapsam 2 verilerini listele"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope2_data = Scope2Data.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope2_data = Scope2Data.objects.none()
    
    return render(request, 'carbon/scope2_list.html', {
        'scope2_data': scope2_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.change_scope2data', raise_exception=True)
def scope2_update_view(request, pk):
    """Kapsam 2 veri güncelleme"""
    scope2_data = get_object_or_404(Scope2Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope2_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope2DataForm(request.POST, instance=scope2_data, firm=scope2_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 2 verisi güncellendi.")
            return redirect('carbon:scope2-list')
    else:
        form = Scope2DataForm(instance=scope2_data, firm=scope2_data.firm)
    
    return render(request, 'carbon/scope2_form.html', {
        'form': form,
        'firm': scope2_data.firm,
        'title': 'Kapsam 2 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_scope2data', raise_exception=True)
def scope2_delete_view(request, pk):
    """Kapsam 2 veri silme"""
    scope2_data = get_object_or_404(Scope2Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope2_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        scope2_data.delete()
        messages.success(request, "Kapsam 2 verisi silindi.")
        return redirect('carbon:scope2-list')
    
    return render(request, 'carbon/scope2_confirm_delete.html', {
        'scope2_data': scope2_data
    })

# KAPSAM 3 VIEW'LARI
@login_required
@permission_required('carbon.view_scope3data', raise_exception=True)
def scope3_list_view(request):
    """Kapsam 3 verilerini listele"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope3_data = Scope3Data.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope3_data = Scope3Data.objects.none()
    
    return render(request, 'carbon/scope3_list.html', {
        'scope3_data': scope3_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.add_scope3data', raise_exception=True)
def scope3_create_view(request):
    """Kapsam 3 veri girişi"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope3DataForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope3_data = form.save(commit=False)
            scope3_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope3_data.save()
            messages.success(request, "Kapsam 3 verisi başarıyla kaydedildi.")
            return redirect('carbon:scope3-list')
    else:
        form = Scope3DataForm(firm=selected_firm)
    
    return render(request, 'carbon/scope3_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 3 - Ulaşım Emisyonu Veri Girişi'
    })

@login_required
@permission_required('carbon.change_scope3data', raise_exception=True)
def scope3_update_view(request, pk):
    """Kapsam 3 veri güncelleme"""
    scope3_data = get_object_or_404(Scope3Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope3_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope3DataForm(request.POST, instance=scope3_data, firm=scope3_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 3 verisi güncellendi.")
            return redirect('carbon:scope3-list')
    else:
        form = Scope3DataForm(instance=scope3_data, firm=scope3_data.firm)
    
    return render(request, 'carbon/scope3_form.html', {
        'form': form,
        'firm': scope3_data.firm,
        'title': 'Kapsam 3 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_scope3data', raise_exception=True)
def scope3_delete_view(request, pk):
    """Kapsam 3 veri silme"""
    scope3_data = get_object_or_404(Scope3Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope3_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        scope3_data.delete()
        messages.success(request, "Kapsam 3 verisi silindi.")
        return redirect('carbon:scope3-list')
    
    return render(request, 'carbon/scope3_confirm_delete.html', {
        'scope3_data': scope3_data
    })

# KAPSAM 4 VIEW'LARI
@login_required
@permission_required('carbon.view_scope4data', raise_exception=True)
def scope4_list_view(request):
    """Kapsam 4 verilerini listele"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope4_data = Scope4Data.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope4_data = Scope4Data.objects.none()
    
    return render(request, 'carbon/scope4_list.html', {
        'scope4_data': scope4_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.add_scope4data', raise_exception=True)
def scope4_create_view(request):
    """Kapsam 4 veri girişi"""
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope4DataForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope4_data = form.save(commit=False)
            scope4_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope4_data.save()
            messages.success(request, "Kapsam 4 verisi başarıyla kaydedildi.")
            return redirect('carbon:scope4-list')
    else:
        form = Scope4DataForm(firm=selected_firm)
    
    return render(request, 'carbon/scope4_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 4 - Satın Alınan Ürün Veri Girişi'
    })

@login_required
@permission_required('carbon.change_scope4data', raise_exception=True)
def scope4_update_view(request, pk):
    """Kapsam 4 veri güncelleme"""
    scope4_data = get_object_or_404(Scope4Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope4_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope4DataForm(request.POST, instance=scope4_data, firm=scope4_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 4 verisi güncellendi.")
            return redirect('carbon:scope4-list')
    else:
        form = Scope4DataForm(instance=scope4_data, firm=scope4_data.firm)
    
    return render(request, 'carbon/scope4_form.html', {
        'form': form,
        'firm': scope4_data.firm,
        'title': 'Kapsam 4 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_scope4data', raise_exception=True)
def scope4_delete_view(request, pk):
    """Kapsam 4 veri silme"""
    scope4_data = get_object_or_404(Scope4Data, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        userfirm__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope4_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        scope4_data.delete()
        messages.success(request, "Kapsam 4 verisi silindi.")
        return redirect('carbon:scope4-list')
    
    return render(request, 'carbon/scope4_confirm_delete.html', {
        'scope4_data': scope4_data
    })

# carbon/views.py - report_list_view fonksiyonu
@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_list_view(request):
    if request.user.is_superuser:
        reports = Report.objects.all()
    elif hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
        reports = Report.objects.filter(firm__in=user_firms)
    else:
        reports = Report.objects.none()
    
    context = {'reports': reports}
    return render(request, 'carbon/report_list.html', context)

@login_required
@permission_required('carbon.add_report', raise_exception=True)
def report_generate_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report_date = form.cleaned_data['report_date']
            
            # Kullanıcının firmasını bul
            if request.user.is_superuser:
                # Süper kullanıcı için ilk firmayı al veya form'dan seç
                firm = Firm.objects.first()
            elif hasattr(request.user, 'user'):
                firm = Firm.objects.filter(user_associations__user=request.user.user).first()
            else:
                firm = Firm.objects.filter(user_associations__user=request.user).first()
            
            if not firm:
                raise PermissionDenied("No associated firm found.")

@login_required
@permission_required('carbon.view_report', raise_exception=True)
def report_detail_view(request, pk):
    """Rapor detayı"""
    report = get_object_or_404(Report, pk=pk)
    
    # Yetki kontrolü
    if hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(userfirm__user=request.user.user)
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
        user_firms = Firm.objects.filter(userfirm__user=request.user.user)
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

# MEVCUT VIEW'LARINIZ (inputdata) - backward compatibility
@login_required
@permission_required('carbon.add_inputdata', raise_exception=True)
def inputdata_create_view(request):
    """Eski input data create view"""
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            input_data = form.save(commit=False)
            if hasattr(request.user, 'user'):
                firm = Firm.objects.filter(userfirm__user=request.user.user).first()
                if not firm:
                    raise PermissionDenied("No associated firm found.")
                input_data.firm = firm
                input_data.created_by = request.user.user
            input_data.save()
            return redirect('carbon:input-list')
    else:
        form = InputDataForm()
    return render(request, 'carbon/inputdata_form.html', {'form': form})

@login_required
@permission_required('carbon.change_inputdata', raise_exception=True)
def inputdata_update_view(request, pk):
    """Eski input data update view"""
    input_data = get_object_or_404(InputData, pk=pk)
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(userfirm__user=request.user.user):
        raise PermissionDenied
    if request.method == 'POST':
        form = InputDataForm(request.POST, instance=input_data)
        if form.is_valid():
            form.save()
            return redirect('carbon:input-list')
    else:
        form = InputDataForm(instance=input_data)
    return render(request, 'carbon/inputdata_form.html', {'form': form})

@login_required
@permission_required('carbon.delete_inputdata', raise_exception=True)
def inputdata_delete_view(request, pk):
    """Eski input data delete view"""
    input_data = get_object_or_404(InputData, pk=pk)
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(userfirm__user=request.user.user):
        raise PermissionDenied
    if request.method == 'POST':
        input_data.delete()
        return redirect('carbon:input-list')
    return render(request, 'carbon/inputdata_confirm_delete.html', {'input_data': input_data})

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

# Diğer scope view'ları için boş fonksiyonlar
@login_required
def scope1_list_view(request):
    return redirect('carbon:input-list')

@login_required
def scope1_create_view(request):
    return redirect('carbon:input-list')

@login_required
def scope1_update_view(request, pk):
    return redirect('carbon:input-list')

@login_required
def scope1_delete_view(request, pk):
    return redirect('carbon:input-list')

# Benzer şekilde scope2, scope3, scope4 için...
@login_required
def scope2_list_view(request):
    return redirect('carbon:input-list')

@login_required
def scope2_create_view(request):
    return redirect('carbon:input-list')

@login_required
def scope2_update_view(request, pk):
    return redirect('carbon:input-list')

@login_required
def scope2_delete_view(request, pk):
    return redirect('carbon:input-list')

# Ve diğerleri...
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
@permission_required('carbon.view_inputdata', raise_exception=True)
def input_list_view(request):
    """Input listesi görüntüleme"""
    
    # Süper kullanıcı kontrolü
    if request.user.is_superuser:
        # Süper kullanıcı tüm firmaları görebilir
        user_firms = Firm.objects.all()
    else:
        # Normal kullanıcılar sadece ilişkili firmalarını görür
        if hasattr(request.user, 'user'):
            user_profile = request.user.user
            user_firms = Firm.objects.filter(user_associations__user=user_profile)
        else:
            user_firms = Firm.objects.filter(user_associations__user=request.user)
    
    # Firma seçimi
    selected_firm_id = request.GET.get('firm_pk')
    if selected_firm_id:
        selected_firm = get_object_or_404(Firm, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    # Veri listesi
    if selected_firm:
        inputs = InputData.objects.filter(firm=selected_firm)
    else:
        inputs = InputData.objects.none()
    
    context = {
        'inputs': inputs,
        'user_firms': user_firms,
        'selected_firm': selected_firm
    }
    return render(request, 'carbon/input_list.html', context)