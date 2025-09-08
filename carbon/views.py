# carbon/views.py
from django.utils import timezone
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q, Sum, Avg, Count
from django.http import JsonResponse, HttpResponse
from datetime import date, datetime, timedelta
from django.views.decorators.http import require_POST
from decimal import Decimal
import json
import pandas as pd
from io import BytesIO
from core.models import UserFirm, Firm, User  # Firm modelini import etmelisiniz


# Rest framework (eğer kullanıyorsanız)
try:
    from rest_framework import viewsets, status
    from rest_framework.decorators import action
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated
    from .serializers import (
        CompanyCarbonReportSerializer,
        EmissionFactorSerializer,
        CarbonCalculationInputSerializer
    )
except ImportError:
    pass  # Rest framework kurulu değilse

from .models import Report  # Report modelini import etmelisiniz
from .services import CarbonCalculationService, ExcelDataLoader
from .models import (
    CoefficientType, EmissionFactor, FuelType,
    Scope1Excel, Scope2Excel, Scope3Excel, Scope4Excel,
    InputCategory, InputData, Report,
    FuelType, GWPValues, Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport,
    ReportDetail, ProductAllocation
)
from .models import (
    CoefficientType, EmissionFactor, FuelType,
    InputCategory, InputData, Report,
    GWPValues, Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport,
    ReportDetail, ProductAllocation
)


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
    scope1_current = Scope1Excel.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope2_current = Scope2Excel.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope3_current = Scope3Excel.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope4_current = Scope4Excel.objects.filter(
        firm=selected_firm,
        period_year=current_year,
        period_month=current_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    total_current = scope1_current + scope2_current + scope3_current + scope4_current
    
    # Önceki ay toplamları (karşılaştırma için)
    scope1_prev = Scope1Excel.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope2_prev = Scope2Excel.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope3_prev = Scope3Excel.objects.filter(
        firm=selected_firm,
        period_year=prev_year,
        period_month=prev_month
    ).aggregate(total=Sum('total_co2e'))['total'] or 0
    
    scope4_prev = Scope4Excel.objects.filter(
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
        s1 = Scope1Excel.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s2 = Scope2Excel.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s3 = Scope3Excel.objects.filter(
            firm=selected_firm,
            period_year=target_date.year,
            period_month=target_date.month
        ).aggregate(total=Sum('total_co2e'))['total'] or 0
        
        s4 = Scope4Excel.objects.filter(
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
    for entry in Scope1Excel.objects.filter(firm=selected_firm).order_by('-created_at')[:3]:
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
    for entry in Scope2Excel.objects.filter(firm=selected_firm).order_by('-created_at')[:3]:
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
@permission_required('carbon.add_Scope1Excel', raise_exception=True)
def scope1_create_view(request):
    """Kapsam 1 veri girişi"""
    # Kullanıcının firmasını al
    user_firms = Firm.objects.filter(user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user)
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope1ExcelForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope1_data = form.save(commit=False)
            scope1_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope1_data.save()
            messages.success(request, "Kapsam 1 verisi başarıyla kaydedildi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope1ExcelForm(firm=selected_firm)
    
    return render(request, 'carbon/scope1_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 1 - Doğrudan Emisyon Veri Girişi'
    })

@login_required
@permission_required('carbon.change_Scope1Excel', raise_exception=True)
def scope1_update_view(request, pk):
    """Kapsam 1 veri güncelleme"""
    scope1_data = get_object_or_404(Scope1Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user)
    if scope1_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope1ExcelForm(request.POST, instance=scope1_data, firm=scope1_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 1 verisi güncellendi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope1ExcelForm(instance=scope1_data, firm=scope1_data.firm)
    
    return render(request, 'carbon/scope1_form.html', {
        'form': form,
        'firm': scope1_data.firm,
        'title': 'Kapsam 1 Veri Güncelleme'
    })

# KAPSAM 2 VIEW'LARI
@login_required
@permission_required('carbon.add_Scope2Excel', raise_exception=True)
def scope2_create_view(request):
    """Kapsam 2 veri girişi"""
    user_firms = Firm.objects.filter(user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user)
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope2ExcelForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope2_data = form.save(commit=False)
            scope2_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope2_data.save()
            messages.success(request, "Kapsam 2 verisi başarıyla kaydedildi.")
            return redirect('carbon:dashboard')
    else:
        form = Scope2ExcelForm(firm=selected_firm)
    
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
            
            Scope1Excel.objects.create(
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


# carbon/views.py - Yeni management view

@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def management_view(request):
    """Karbon yönetim ana sayfası - tek sayfada tüm işlemler"""
    
    # AJAX istekleri için
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        action = request.POST.get('action')
        
        if action == 'get_subcategories':
            # Alt kapsam listesini döndür
            scope = request.POST.get('scope')
            subcategories = get_subcategories_for_scope(scope)
            return JsonResponse({'subcategories': subcategories})
        
        elif action == 'get_items':
            # Seçilen kapsam ve alt kapsam için kalemleri getir
            scope = request.POST.get('scope')
            subcategory = request.POST.get('subcategory')
            
            items = EmissionFactor.objects.filter(
                category=scope,
                subcategory=subcategory
            ).values('id', 'name', 'value', 'unit', 'valid_from', 'valid_to', 'is_active')
            
            items_list = []
            for item in items:
                items_list.append({
                    'id': item['id'],
                    'name': item['name'],
                    'value': str(item['value']),
                    'unit': item['unit'],
                    'valid_from': item['valid_from'].strftime('%Y-%m-%d') if item['valid_from'] else '',
                    'valid_to': item['valid_to'].strftime('%Y-%m-%d') if item['valid_to'] else '',
                    'is_active': item['is_active']
                })
            
            return JsonResponse({'items': items_list})
        
        elif action == 'add_item':
            # Yeni kalem ekle
            try:
                EmissionFactor.objects.create(
                    name=request.POST.get('name'),
                    category=request.POST.get('category'),
                    subcategory=request.POST.get('subcategory'),
                    value=float(request.POST.get('value', 0)),
                    unit=request.POST.get('unit'),
                    valid_from=request.POST.get('valid_from'),
                    valid_to=request.POST.get('valid_to') or None,
                    source=request.POST.get('source', ''),
                    is_active=request.POST.get('is_active') == 'true'
                )
                return JsonResponse({'success': True, 'message': 'Kalem başarıyla eklendi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        
        elif action == 'update_item':
            # Kalem güncelle
            try:
                item_id = request.POST.get('item_id')
                item = EmissionFactor.objects.get(id=item_id)
                
                item.name = request.POST.get('name')
                item.value = float(request.POST.get('value', 0))
                item.unit = request.POST.get('unit')
                item.valid_from = request.POST.get('valid_from')
                item.valid_to = request.POST.get('valid_to') or None
                item.source = request.POST.get('source', '')
                item.is_active = request.POST.get('is_active') == 'true'
                item.save()
                
                return JsonResponse({'success': True, 'message': 'Kalem güncellendi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        
        elif action == 'delete_item':
            # Kalem sil
            try:
                item_id = request.POST.get('item_id')
                EmissionFactor.objects.get(id=item_id).delete()
                return JsonResponse({'success': True, 'message': 'Kalem silindi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
    
    # Normal sayfa yükleme
    context = {
        'scopes': get_scope_choices(),
        'units': get_unit_choices(),
    }
    
    return render(request, 'carbon/management_new.html', context)


def get_scope_choices():
    """Kapsam seçenekleri"""
    return [
        {'value': 'KAPSAM_1', 'label': 'Kapsam 1 - Doğrudan Emisyonlar'},
        {'value': 'KAPSAM_2', 'label': 'Kapsam 2 - Enerji Dolaylı'},
        {'value': 'KAPSAM_3', 'label': 'Kapsam 3 - Ulaşım'},
        {'value': 'KAPSAM_4', 'label': 'Kapsam 4 - Satın Alınan Ürünler'},
        {'value': 'KAPSAM_5', 'label': 'Kapsam 5 - Ürün Kullanımı'},
        {'value': 'KAPSAM_6', 'label': 'Kapsam 6 - Diğer'},
    ]


def get_subcategories_for_scope(scope):
    """Her kapsam için alt kategoriler"""
    subcategories = {
        'KAPSAM_1': [
            {'value': 'sabit_yanma', 'label': '1.1 Sabit Yanma'},
            {'value': 'mobil_yanma', 'label': '1.2 Mobil Yanma'},
            {'value': 'proses_emisyon', 'label': '1.3 Proses Emisyonları'},
            {'value': 'kacak_emisyon', 'label': '1.4 Kaçak Emisyonlar'},
        ],
        'KAPSAM_2': [
            {'value': 'elektrik', 'label': '2.1 Elektrik Tüketimi'},
            {'value': 'buhar', 'label': '2.2 Buhar Tüketimi'},
            {'value': 'sogutma', 'label': '2.3 Soğutma'},
            {'value': 'isitma', 'label': '2.4 Isıtma'},
        ],
        'KAPSAM_3': [
            {'value': 'upstream_nakliye', 'label': '3.1 Upstream Nakliye'},
            {'value': 'downstream_nakliye', 'label': '3.2 Downstream Nakliye'},
            {'value': 'personel_ulasim', 'label': '3.3 Personel Ulaşımı'},
            {'value': 'is_seyahat', 'label': '3.4 İş Seyahatleri'},
        ],
        'KAPSAM_4': [
            {'value': 'hammadde', 'label': '4.1 Hammaddeler'},
            {'value': 'yari_mamul', 'label': '4.2 Yarı Mamuller'},
            {'value': 'hizmet', 'label': '4.3 Hizmetler'},
            {'value': 'sermaye_mal', 'label': '4.4 Sermaye Malları'},
        ],
        'KAPSAM_5': [
            {'value': 'urun_kullanim', 'label': '5.1 Ürün Kullanımı'},
            {'value': 'urun_omur_sonu', 'label': '5.2 Ürün Ömür Sonu'},
        ],
        'KAPSAM_6': [
            {'value': 'diger', 'label': '6.1 Diğer Emisyonlar'},
        ],
    }
    return subcategories.get(scope, [])


def get_unit_choices():
    """Birim seçenekleri"""
    return [
        'kgCO2/TJ', 'tCO2/MWh', 'kgCO2e/kg', 'kgCO2e/L', 
        'kgCO2e/m³', 'kgCO2e/km', 'kgCO2e/kWh'
    ]


@login_required
@permission_required('carbon.view_management_carbon', raise_exception=True)
def management_list_view(request):  # İsmi aynı bırakıyoruz URL'ler uyumlu olsun
    """Karbon yönetim ana sayfası - tek sayfada tüm işlemler"""
    
    # AJAX istekleri için
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        action = request.POST.get('action')
        
        if action == 'get_subcategories':
            # Alt kapsam listesini döndür
            scope = request.POST.get('scope')
            subcategories = get_subcategories_for_scope(scope)
            return JsonResponse({'subcategories': subcategories})
        
        elif action == 'get_items':
            # Seçilen kapsam ve alt kapsam için kalemleri getir
            scope = request.POST.get('scope')
            subcategory = request.POST.get('subcategory')
            
            items = EmissionFactor.objects.filter(
                category=scope,
                subcategory=subcategory
            ).values('id', 'name', 'value', 'unit', 'valid_from', 'valid_to', 'is_active')
            
            items_list = []
            for item in items:
                items_list.append({
                    'id': item['id'],
                    'name': item['name'],
                    'value': str(item['value']),
                    'unit': item['unit'] if item['unit'] else '',
                    'valid_from': item['valid_from'].strftime('%Y-%m-%d') if item['valid_from'] else '',
                    'valid_to': item['valid_to'].strftime('%Y-%m-%d') if item['valid_to'] else '',
                    'is_active': item.get('is_active', True)
                })
            
            return JsonResponse({'items': items_list})
        
        elif action == 'add_item':
            # Yeni kalem ekle
            try:
                # Unit alanı boşsa varsayılan değer
                unit = request.POST.get('unit')
                if not unit:
                    unit = 'kgCO2/TJ'  # Varsayılan birim
                
                EmissionFactor.objects.create(
                    name=request.POST.get('name'),
                    category=request.POST.get('category'),
                    subcategory=request.POST.get('subcategory'),
                    value=float(request.POST.get('value', 0)),
                    unit=unit,
                    valid_from=request.POST.get('valid_from'),
                    valid_to=request.POST.get('valid_to') or None,
                    source=request.POST.get('source', ''),
                    is_active=request.POST.get('is_active') == 'true'
                )
                return JsonResponse({'success': True, 'message': 'Kalem başarıyla eklendi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        
        elif action == 'update_item':
            # Kalem güncelle
            try:
                item_id = request.POST.get('item_id')
                item = EmissionFactor.objects.get(id=item_id)
                
                item.name = request.POST.get('name')
                item.value = float(request.POST.get('value', 0))
                item.unit = request.POST.get('unit')
                item.valid_from = request.POST.get('valid_from')
                item.valid_to = request.POST.get('valid_to') or None
                item.source = request.POST.get('source', '')
                item.is_active = request.POST.get('is_active') == 'true'
                item.save()
                
                return JsonResponse({'success': True, 'message': 'Kalem güncellendi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
        
        elif action == 'delete_item':
            # Kalem sil
            try:
                item_id = request.POST.get('item_id')
                EmissionFactor.objects.get(id=item_id).delete()
                return JsonResponse({'success': True, 'message': 'Kalem silindi!'})
            except Exception as e:
                return JsonResponse({'success': False, 'message': str(e)})
    
    # Normal sayfa yükleme
    context = {
        'scopes': get_scope_choices(),
        'units': get_unit_choices(),
    }
    
    return render(request, 'carbon/management_new.html', context)


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
@permission_required('carbon.view_Scope1Excel', raise_exception=True)
def scope1_list_view(request):
    """Kapsam 1 verilerini listele"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope1_data = Scope1Excel.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope1_data = Scope1Excel.objects.none()
    
    return render(request, 'carbon/scope1_list.html', {
        'scope1_data': scope1_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.delete_Scope1Excel', raise_exception=True)
def scope1_delete_view(request, pk):
    """Kapsam 1 veri silme"""
    scope1_data = get_object_or_404(Scope1Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
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
@permission_required('carbon.view_Scope2Excel', raise_exception=True)
def scope2_list_view(request):
    """Kapsam 2 verilerini listele"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope2_data = Scope2Excel.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope2_data = Scope2Excel.objects.none()
    
    return render(request, 'carbon/scope2_list.html', {
        'scope2_data': scope2_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.change_Scope2Excel', raise_exception=True)
def scope2_update_view(request, pk):
    """Kapsam 2 veri güncelleme"""
    scope2_data = get_object_or_404(Scope2Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope2_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope2ExcelForm(request.POST, instance=scope2_data, firm=scope2_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 2 verisi güncellendi.")
            return redirect('carbon:scope2-list')
    else:
        form = Scope2ExcelForm(instance=scope2_data, firm=scope2_data.firm)
    
    return render(request, 'carbon/scope2_form.html', {
        'form': form,
        'firm': scope2_data.firm,
        'title': 'Kapsam 2 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_Scope2Excel', raise_exception=True)
def scope2_delete_view(request, pk):
    """Kapsam 2 veri silme"""
    scope2_data = get_object_or_404(Scope2Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
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
@permission_required('carbon.view_Scope3Excel', raise_exception=True)
def scope3_list_view(request):
    """Kapsam 3 verilerini listele"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope3_data = Scope3Excel.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope3_data = Scope3Excel.objects.none()
    
    return render(request, 'carbon/scope3_list.html', {
        'scope3_data': scope3_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.add_Scope3Excel', raise_exception=True)
def scope3_create_view(request):
    """Kapsam 3 veri girişi"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope3ExcelForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope3_data = form.save(commit=False)
            scope3_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope3_data.save()
            messages.success(request, "Kapsam 3 verisi başarıyla kaydedildi.")
            return redirect('carbon:scope3-list')
    else:
        form = Scope3ExcelForm(firm=selected_firm)
    
    return render(request, 'carbon/scope3_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 3 - Ulaşım Emisyonu Veri Girişi'
    })

@login_required
@permission_required('carbon.change_Scope3Excel', raise_exception=True)
def scope3_update_view(request, pk):
    """Kapsam 3 veri güncelleme"""
    scope3_data = get_object_or_404(Scope3Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope3_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope3ExcelForm(request.POST, instance=scope3_data, firm=scope3_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 3 verisi güncellendi.")
            return redirect('carbon:scope3-list')
    else:
        form = Scope3ExcelForm(instance=scope3_data, firm=scope3_data.firm)
    
    return render(request, 'carbon/scope3_form.html', {
        'form': form,
        'firm': scope3_data.firm,
        'title': 'Kapsam 3 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_Scope3Excel', raise_exception=True)
def scope3_delete_view(request, pk):
    """Kapsam 3 veri silme"""
    scope3_data = get_object_or_404(Scope3Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
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
@permission_required('carbon.view_Scope4Excel', raise_exception=True)
def scope4_list_view(request):
    """Kapsam 4 verilerini listele"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    
    selected_firm_id = request.GET.get('firm_id')
    if selected_firm_id:
        selected_firm = get_object_or_404(user_firms, pk=selected_firm_id)
    else:
        selected_firm = user_firms.first()
    
    if selected_firm:
        scope4_data = Scope4Excel.objects.filter(firm=selected_firm).order_by('-period_year', '-period_month')
    else:
        scope4_data = Scope4Excel.objects.none()
    
    return render(request, 'carbon/scope4_list.html', {
        'scope4_data': scope4_data,
        'selected_firm': selected_firm,
        'user_firms': user_firms
    })

@login_required
@permission_required('carbon.add_Scope4Excel', raise_exception=True)
def scope4_create_view(request):
    """Kapsam 4 veri girişi"""
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    selected_firm = user_firms.first()
    
    if not selected_firm:
        messages.error(request, "Firma bulunamadı.")
        return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        form = Scope4ExcelForm(request.POST, firm=selected_firm)
        if form.is_valid():
            scope4_data = form.save(commit=False)
            scope4_data.created_by = request.user.user if hasattr(request.user, 'user') else request.user
            scope4_data.save()
            messages.success(request, "Kapsam 4 verisi başarıyla kaydedildi.")
            return redirect('carbon:scope4-list')
    else:
        form = Scope4ExcelForm(firm=selected_firm)
    
    return render(request, 'carbon/scope4_form.html', {
        'form': form,
        'firm': selected_firm,
        'title': 'Kapsam 4 - Satın Alınan Ürün Veri Girişi'
    })

@login_required
@permission_required('carbon.change_Scope4Excel', raise_exception=True)
def scope4_update_view(request, pk):
    """Kapsam 4 veri güncelleme"""
    scope4_data = get_object_or_404(Scope4Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
    )
    if scope4_data.firm not in user_firms:
        raise PermissionDenied
    
    if request.method == 'POST':
        form = Scope4ExcelForm(request.POST, instance=scope4_data, firm=scope4_data.firm)
        if form.is_valid():
            form.save()
            messages.success(request, "Kapsam 4 verisi güncellendi.")
            return redirect('carbon:scope4-list')
    else:
        form = Scope4ExcelForm(instance=scope4_data, firm=scope4_data.firm)
    
    return render(request, 'carbon/scope4_form.html', {
        'form': form,
        'firm': scope4_data.firm,
        'title': 'Kapsam 4 Veri Güncelleme'
    })

@login_required
@permission_required('carbon.delete_Scope4Excel', raise_exception=True)
def scope4_delete_view(request, pk):
    """Kapsam 4 veri silme"""
    scope4_data = get_object_or_404(Scope4Excel, pk=pk)
    
    # Yetki kontrolü
    user_firms = Firm.objects.filter(
        user_associations__user=request.user.user if hasattr(request.user, 'user') else request.user
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

@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_generate_view(request):
    """Anlık karbon raporu oluştur"""
    
    if request.method == 'POST':
        form = ReportForm(request.POST, user=request.user)
        if form.is_valid():
            firm = form.cleaned_data['firm']
            report_date = form.cleaned_data['report_date']
            
            # Rapor dönemini belirle
            report_period_end = report_date
            report_period_start = report_date - timedelta(days=365)
            
            # Kullanıcı bilgisini al
            if hasattr(request.user, 'user'):
                generated_by_user = request.user.user
            else:
                generated_by_user = None
            
            # Yıl ve ay
            report_year = report_date.year
            report_month = report_date.month
            
            # Excel modellerinden verileri topla
            scope1_total = Scope1Excel.objects.filter(
                firm=firm,
                year__gte=report_period_start.year,
                year__lte=report_period_end.year
            ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
            
            scope2_total = Scope2Excel.objects.filter(
                firm=firm,
                year__gte=report_period_start.year,
                year__lte=report_period_end.year
            ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
            
            scope4_total = Scope4Excel.objects.filter(
                firm=firm,
                year__gte=report_period_start.year,
                year__lte=report_period_end.year
            ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
            
            # Diğer scope'lar için varsayılan
            scope3_total = Decimal('0')
            scope5_total = Decimal('0')
            scope6_total = Decimal('0')
            
            # Toplamları hesapla
            total = scope1_total + scope2_total + scope3_total + scope4_total + scope5_total + scope6_total
            
            # Oranları hesapla
            if total > 0:
                direct_ratio = float((scope1_total + scope2_total) / total * 100)
                indirect_ratio = float((scope3_total + scope4_total) / total * 100)
            else:
                direct_ratio = 0.0
                indirect_ratio = 0.0
            
            # Rapor oluştur - TÜM ALANLAR KEYWORD ARGUMENT OLMALI
            report = Report.objects.create(
                firm=firm,
                report_date=report_date,
                report_period_start=report_period_start,
                report_period_end=report_period_end,
                report_year=report_year,
                report_month=report_month,
                generated_by=generated_by_user,
                total_co2e=float(total),
                direct_ratio=direct_ratio,
                indirect_ratio=indirect_ratio,
                scope1_total=scope1_total,
                scope2_total=scope2_total,
                scope3_total=scope3_total,
                scope4_total=scope4_total,
                scope5_total=scope5_total,
                scope6_total=scope6_total,
                status='COMPLETED'
            )
            
            messages.success(request, f"Rapor başarıyla oluşturuldu! Toplam: {total:.2f} tCO2e")
            return redirect('carbon:report-list')
    else:
        form = ReportForm(user=request.user, initial={'report_date': timezone.now().date()})
    
    return render(request, 'carbon/report_form.html', {'form': form})


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
@permission_required('carbon.add_inputdata', raise_exception=True)
def inputdata_create_view(request):
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            input_data = form.save(commit=False)
            if hasattr(request.user, 'user'):
                # userfirm yerine user_associations kullanın:
                firm = Firm.objects.filter(user_associations__user=request.user.user).first()
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
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(user_associations__user=request.user.user):
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
    if hasattr(request.user, 'user') and input_data.firm not in Firm.objects.filter(user_associations__user=request.user.user):
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

@login_required
@permission_required('carbon.view_report', raise_exception=True)
def excel_report_view(request):
    """Excel raporu oluştur ve indir"""
    if request.method == 'POST':
        firm_id = request.POST.get('firm_id')
        year = int(request.POST.get('year', datetime.now().year))
        month = request.POST.get('month')
        
        if not firm_id:
            messages.error(request, "Lütfen bir firma seçin.")
            return redirect('carbon:excel-report')
        
        firm = get_object_or_404(Firm, pk=firm_id)
        
        # Yetki kontrolü
        user_firms = get_user_firms(request)
        if firm not in user_firms:
            raise PermissionDenied
        
        # Month değerini kontrol et
        if month:
            month = int(month)
        else:
            month = None
        
        # ExcelReport oluştur veya getir
        if month:
            excel_report, created = ExcelReport.objects.get_or_create(
                firm=firm,
                year=year,
                month=month,
                defaults={'created_by': request.user.user if hasattr(request.user, 'user') else None}
            )
        else:
            excel_report, created = ExcelReport.objects.get_or_create(
                firm=firm,
                year=year,
                month=1,  # Yıllık rapor için varsayılan ay
                defaults={'created_by': request.user.user if hasattr(request.user, 'user') else None}
            )
        
        # Toplamları hesapla
        excel_report.calculate_totals()
        excel_report.save()
        
        # Excel dosyası oluştur
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Özet sayfası
            summary_data = {
                'Bilgi': ['Firma', 'Yıl', 'Ay', 'Toplam CO2e'],
                'Değer': [firm.name, year, month or 'Yıllık', f"{excel_report.total_co2e:.2f}"]
            }
            df_summary = pd.DataFrame(summary_data)
            df_summary.to_excel(writer, sheet_name='Özet', index=False)
            
            # Kapsam detayları
            scope_data = {
                'Kapsam': ['Kapsam 1', 'Kapsam 2', 'Kapsam 3', 'Kapsam 4', 'TOPLAM'],
                'CO2e (ton)': [
                    float(excel_report.scope1_total),
                    float(excel_report.scope2_total),
                    float(excel_report.scope3_total),
                    float(excel_report.scope4_total),
                    float(excel_report.total_co2e)
                ]
            }
            df_scopes = pd.DataFrame(scope_data)
            df_scopes.to_excel(writer, sheet_name='Kapsamlar', index=False)
        
        output.seek(0)
        
        # Response oluştur
        response = HttpResponse(
            output.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        filename = f"karbon_raporu_{firm.name}_{year}_{month or 'yillik'}.xlsx"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        
        return response
    
    # GET request - form göster
    user_firms = get_user_firms(request)
    
    context = {
        'firms': user_firms,
        'years': range(2020, datetime.now().year + 2),
        'months': [
            (1, 'Ocak'), (2, 'Şubat'), (3, 'Mart'),
            (4, 'Nisan'), (5, 'Mayıs'), (6, 'Haziran'),
            (7, 'Temmuz'), (8, 'Ağustos'), (9, 'Eylül'),
            (10, 'Ekim'), (11, 'Kasım'), (12, 'Aralık')
        ]
    }
    
    return render(request, 'carbon/excel_report_form.html', context)

@login_required
@permission_required('carbon.view_report', raise_exception=True)
def report_list_view(request):
    """Raporları listele"""
    # Kullanıcının firmalarını al
    user_firms = get_user_firms(request)
    
    # Raporları filtrele
    reports = Report.objects.filter(firm__in=user_firms).order_by('-report_date')
    
    # Firma filtresi
    firm_id = request.GET.get('firm_id')
    if firm_id:
        reports = reports.filter(firm_id=firm_id)
    
    # Tarih filtresi
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if start_date:
        reports = reports.filter(report_date__gte=start_date)
    if end_date:
        reports = reports.filter(report_date__lte=end_date)
    
    context = {
        'reports': reports,
        'firms': user_firms,
        'selected_firm': firm_id,
        'start_date': start_date,
        'end_date': end_date,
    }
    
    return render(request, 'carbon/report_list.html', context)

@login_required
def carbon_dashboard(request):
    """Karbon modülü ana sayfası"""
    
    # Kullanıcının yetkili olduğu firmalar
    if hasattr(request.user, 'user'):
        user_profile = request.user.user
        firms = user_profile.firm.all() if hasattr(user_profile, 'firm') else Firm.objects.none()
    else:
        firms = Firm.objects.all() if request.user.is_superuser else Firm.objects.none()
    
    # Son raporlar
    recent_reports = Report.objects.filter(
        firm__in=firms
    ).order_by('-report_date')[:5]
    
    # İstatistikler
    total_reports = Report.objects.filter(firm__in=firms).count()
    total_emissions = Report.objects.filter(
        firm__in=firms
    ).aggregate(
        total=Sum('total_co2e')
    )['total'] or 0
    
    context = {
        'firms': firms,
        'recent_reports': recent_reports,
        'total_reports': total_reports,
        'total_emissions': total_emissions,
    }
    
    return render(request, 'carbon/dashboard.html', context)

@login_required
def carbon_input(request, firm_id):
    """Karbon verisi girişi sayfası"""
    
    firm = get_object_or_404(Firm, pk=firm_id)
    
    # Yetki kontrolü
    if not request.user.is_superuser:
        if hasattr(request.user, 'user'):
            if firm not in request.user.user.firm.all():
                messages.error(request, "Bu firmaya erişim yetkiniz yok!")
                return redirect('carbon:dashboard')
    
    if request.method == 'POST':
        year = int(request.POST.get('year', 2025))
        month = int(request.POST.get('month', 1))
        scope = request.POST.get('scope')
        
        if scope == 'scope1':
            # Kapsam 1 verisi kaydet
            location = request.POST.get('location')
            fuel_name = request.POST.get('fuel_name')
            consumption = Decimal(request.POST.get('consumption', '0'))
            unit = request.POST.get('unit', 'm³')
            emission_type = request.POST.get('emission_type', 'STATIONARY')
            
            # Emisyon faktörünü bul
            emission_factor = EmissionFactor.objects.filter(
                name=fuel_name,
                factor_type='FUEL'
            ).first()
            
            if emission_factor:
                Scope1Excel.objects.update_or_create(
                    firm=firm,
                    location=location,
                    fuel_name=fuel_name,
                    period_year=year,
                    period_month=month,
                    defaults={
                        'consumption_value': consumption,
                        'consumption_unit': unit,
                        'emission_type': emission_type,
                        'emission_factor': emission_factor,
                        'created_by': request.user.user if hasattr(request.user, 'user') else None
                    }
                )
                messages.success(request, "Kapsam 1 verisi kaydedildi!")
        
        elif scope == 'scope2':
            # Kapsam 2 verisi kaydet
            facility = request.POST.get('facility_name')
            electricity = Decimal(request.POST.get('electricity_kwh', '0'))
            
            Scope2Excel.objects.update_or_create(
                firm=firm,
                facility_name=facility,
                period_year=year,
                period_month=month,
                defaults={
                    'electricity_kwh': electricity,
                    'created_by': request.user.user if hasattr(request.user, 'user') else None
                }
            )
            messages.success(request, "Kapsam 2 verisi kaydedildi!")
        
        elif scope == 'scope3':
            # Kapsam 3 verisi kaydet
            messages.success(request, "Kapsam 3 verisi kaydedildi!")
        
        elif scope == 'scope4':
            # Kapsam 4 verisi kaydet
            product_name = request.POST.get('product_name')
            quantity = Decimal(request.POST.get('quantity', '0'))
            material_type = request.POST.get('material_type')
            
            emission_factor = EmissionFactor.objects.filter(
                name=material_type,
                factor_type='MATERIAL'
            ).first()
            
            if emission_factor:
                Scope4Excel.objects.update_or_create(
                    firm=firm,
                    product_name=product_name,
                    period_year=year,
                    period_month=month,
                    defaults={
                        'product_category': 'Hammadde',
                        'quantity': quantity,
                        'unit': 'kg',
                        'emission_factor': emission_factor.ef_co2,
                        'emission_factor_source': emission_factor.source,
                        'created_by': request.user.user if hasattr(request.user, 'user') else None
                    }
                )
                messages.success(request, "Kapsam 4 verisi kaydedildi!")
        
        return redirect('carbon:input', firm_id=firm_id)
    
    # GET isteği için form verilerini hazırla
    fuel_factors = EmissionFactor.objects.filter(factor_type='FUEL')
    material_factors = EmissionFactor.objects.filter(factor_type='MATERIAL')
    
    # Mevcut verileri getir
    current_year = request.GET.get('year', 2025)
    current_month = request.GET.get('month', 1)
    
    scope1_data = Scope1Excel.objects.filter(
        firm=firm,
        period_year=current_year,
        period_month=current_month
    )
    
    scope2_data = Scope2Excel.objects.filter(
        firm=firm,
        period_year=current_year,
        period_month=current_month
    )
    
    scope4_data = Scope4Excel.objects.filter(
        firm=firm,
        period_year=current_year,
        period_month=current_month
    )
    
    context = {
        'firm': firm,
        'fuel_factors': fuel_factors,
        'material_factors': material_factors,
        'scope1_data': scope1_data,
        'scope2_data': scope2_data,
        'scope4_data': scope4_data,
        'current_year': current_year,
        'current_month': current_month,
    }
    
    return render(request, 'carbon/input.html', context)

@login_required
def calculate_carbon(request, firm_id):
    """Karbon hesaplama ve rapor oluşturma"""
    
    firm = get_object_or_404(Firm, pk=firm_id)
    
    if request.method == 'POST':
        year = int(request.POST.get('year', 2025))
        month = int(request.POST.get('month', 1))
        
        # Hesaplama servisi
        calculator = CarbonCalculationService(
            firm=firm,
            year=year,
            month=month,
            user=request.user.user if hasattr(request.user, 'user') else None
        )
        
        # Rapor oluştur
        report = calculator.create_report()
        
        messages.success(request, f"Karbon raporu oluşturuldu! Toplam: {report.total_co2e:.2f} tCO2e")
        
        return redirect('carbon:report_detail', report_id=report.id)
    
    return redirect('carbon:dashboard')

@login_required
def report_detail(request, report_id):
    """Rapor detay sayfası"""
    
    report = get_object_or_404(Report, pk=report_id)
    
    # Yetki kontrolü
    if not request.user.is_superuser:
        if hasattr(request.user, 'user'):
            if report.firm not in request.user.user.firm.all():
                messages.error(request, "Bu rapora erişim yetkiniz yok!")
                return redirect('carbon:dashboard')
    
    # Kapsam verilerini getir
    scope1_data = Scope1Excel.objects.filter(
        firm=report.firm,
        period_year=report.report_year,
        period_month=report.report_month
    )
    
    scope2_data = Scope2Excel.objects.filter(
        firm=report.firm,
        period_year=report.report_year,
        period_month=report.report_month
    )
    
    scope3_data = Scope3Excel.objects.filter(
        firm=report.firm,
        period_year=report.report_year,
        period_month=report.report_month
    )
    
    scope4_data = Scope4Excel.objects.filter(
        firm=report.firm,
        period_year=report.report_year,
        period_month=report.report_month
    )
    
    # Ürün dağılımları
    product_allocations = report.product_allocations.all()
    
    # Grafik verisi hazırla
    chart_data = {
        'labels': ['Kapsam 1', 'Kapsam 2', 'Kapsam 3', 'Kapsam 4', 'Kapsam 5', 'Kapsam 6'],
        'values': [
            float(report.scope1_total),
            float(report.scope2_total),
            float(report.scope3_total),
            float(report.scope4_total),
            float(report.scope5_total),
            float(report.scope6_total),
        ]
    }
    
    context = {
        'report': report,
        'scope1_data': scope1_data,
        'scope2_data': scope2_data,
        'scope3_data': scope3_data,
        'scope4_data': scope4_data,
        'product_allocations': product_allocations,
        'chart_data': json.dumps(chart_data),
    }
    
    return render(request, 'carbon/report_detail.html', context)


@login_required
def download_report(request, report_id):
    """Raporu Excel olarak indir"""
    
    report = get_object_or_404(Report, pk=report_id)
    
    # Yetki kontrolü
    if not request.user.is_superuser:
        if hasattr(request.user, 'user'):
            if report.firm not in request.user.user.firm.all():
                messages.error(request, "Bu rapora erişim yetkiniz yok!")
                return redirect('carbon:dashboard')
    
    # Excel oluştur
    calculator = CarbonCalculationService(
        firm=report.firm,
        year=report.report_year,
        month=report.report_month
    )
    calculator.report = report
    
    excel_file = calculator.generate_excel_report()
    
    # Response oluştur
    response = HttpResponse(
        excel_file.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    filename = f"karbon_raporu_{report.firm.name}_{report.report_year}_{report.report_month or 'yillik'}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


@login_required
@require_POST
def load_example_data(request, firm_id):
    """Excel'deki örnek verileri yükle"""
    
    firm = get_object_or_404(Firm, pk=firm_id)
    
    # Yetki kontrolü
    if not request.user.is_superuser:
        messages.error(request, "Bu işlem için yetkiniz yok!")
        return redirect('carbon:dashboard')
    
    year = int(request.POST.get('year', 2025))
    month = int(request.POST.get('month', 1))
    
    # Servisi çalıştır
    calculator = CarbonCalculationService(
        firm=firm,
        year=year,
        month=month,
        user=request.user.user if hasattr(request.user, 'user') else None
    )
    
    calculator.load_example_data()
    
    messages.success(request, "Excel'deki örnek veriler başarıyla yüklendi!")
    
    return redirect('carbon:input', firm_id=firm_id)

class CarbonReportViewSet(viewsets.ModelViewSet):
    """Karbon raporları API endpoint'i"""
    
    serializer_class = CompanyCarbonReportSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Kullanıcının yetkili olduğu firma raporları"""
        user = self.request.user
        if user.is_superuser:
            return CompanyCarbonReport.objects.all()
        
        # Kullanıcının firması varsa sadece o firmanın raporları
        return CompanyCarbonReport.objects.filter(
            company__users=user
        )
    
    @action(detail=False, methods=['post'])
    def calculate(self, request):
        """Karbon ayak izi hesaplama endpoint'i
        
        POST /api/carbon-reports/calculate/
        {
            "company_id": 1,
            "year": 2025,
            "month": 1,
            "scope1": [...],
            "scope2": [...],
            "scope3": [...],
            "scope4": [...],
            "products": [...]
        }
        """
        
        serializer = CarbonCalculationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        
        # Hesaplama servisini çalıştır
        calculator = CarbonCalculatorService(
            company=data['company'],
            year=data['year'],
            month=data.get('month')
        )
        
        try:
            results = calculator.generate_full_report(data)
            
            return Response({
                'success': True,
                'report_id': calculator.report.id,
                'results': results
            })
            
        except Exception as e:
            return Response({
                'success': False,
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def download_excel(self, request, pk=None):
        """Raporu Excel olarak indir"""
        report = self.get_object()
        
        # Excel oluşturma servisi
        excel_service = CarbonReportExcelService(report)
        excel_file = excel_service.generate()
        
        response = HttpResponse(
            excel_file,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename=karbon_raporu_{report.id}.xlsx'
        
        return response
    
    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Raporu onayla"""
        report = self.get_object()
        
        if not request.user.has_perm('carbon.approve_report'):
            return Response({
                'error': 'Rapor onaylama yetkiniz yok'
            }, status=status.HTTP_403_FORBIDDEN)
        
        report.status = 'APPROVED'
        report.save()
        
        return Response({
            'success': True,
            'message': 'Rapor onaylandı'
        })


class EmissionFactorViewSet(viewsets.ModelViewSet):
    """Emisyon faktörleri yönetimi"""
    
    queryset = EmissionFactor.objects.all()
    serializer_class = EmissionFactorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Tarih bazlı filtreleme"""
        queryset = super().get_queryset()
        
        # Query parametreleri
        factor_type = self.request.query_params.get('type')
        valid_date = self.request.query_params.get('date')
        
        if factor_type:
            queryset = queryset.filter(factor_type=factor_type)
        
        if valid_date:
            date_obj = datetime.strptime(valid_date, '%Y-%m-%d').date()
            queryset = queryset.filter(
                valid_from__lte=date_obj,
                Q(valid_to__gte=date_obj) | Q(valid_to__isnull=True)
            )
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def bulk_upload(self, request):
        """Excel'den toplu emisyon faktörü yükleme"""
        
        file = request.FILES.get('file')
        if not file:
            return Response({
                'error': 'Dosya yüklenmedi'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Excel dosyasını oku ve faktörleri yükle
            import pandas as pd
            df = pd.read_excel(file)
            
            created_count = 0
            for _, row in df.iterrows():
                EmissionFactor.objects.create(
                    name=row['name'],
                    factor_type=row['type'],
                    unit=row['unit'],
                    co2_factor=row['co2_factor'],
                    ch4_factor=row.get('ch4_factor', 0),
                    n2o_factor=row.get('n2o_factor', 0),
                    nkd=row.get('nkd'),
                    density=row.get('density'),
                    valid_from=row['valid_from'],
                    valid_to=row.get('valid_to'),
                    source=row.get('source', 'Excel Import')
                )
                created_count += 1
            
            return Response({
                'success': True,
                'created': created_count
            })
            
        except Exception as e:
            return Response({
                'error': f'Dosya işlenirken hata: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)