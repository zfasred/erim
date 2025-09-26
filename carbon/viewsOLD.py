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
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
import json
import pandas as pd

from .models import (
    DynamicCarbonInput,
    SubScope,
    CarbonCoefficient,
    GWPValues,
    ExcelReport,
    FuelType
)

from .forms import (
    DynamicCarbonInputForm,
    CarbonCoefficientForm,
    UserFirmAccessForm,
    ReportGenerateForm,
    ExcelReportForm,
    BulkUploadForm,
    ReportForm
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
def api_get_coefficient_names(request):
    """Belirli kapsam ve alt kapsam için tanımlı isimleri getir"""
    
    scope = request.GET.get('scope')
    subscope = request.GET.get('subscope')
    
    if not scope or not subscope:
        return JsonResponse({'names': []})
    
    # O kapsam/alt kapsam için unique isimleri getir
    names = CarbonCoefficient.objects.filter(
        scope=scope,
        subscope=subscope
    ).values_list('name', flat=True).distinct()
    
    # Set kullanarak tekrarları temizle
    unique_names = list(set(names))
    names_list = [{'value': name, 'text': name} for name in sorted(unique_names)]
    
    return JsonResponse({'names': names_list})


@login_required
def api_report_data(request):
    """Rapor verilerini getir ve HESAPLA"""
    
    firm_id = request.GET.get('firm')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    
    if not all([firm_id, start_date, end_date]):
        return JsonResponse({'error': 'Eksik parametreler'}, status=400)
    
    from django.utils import timezone
    start = timezone.make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
    end = timezone.make_aware(datetime.strptime(end_date, '%Y-%m-%d'))
    end = end.replace(hour=23, minute=59, second=59)
    
    # Verileri çek
    inputs = DynamicCarbonInput.objects.filter(
        firm_id=firm_id,
        datetime__gte=start,
        datetime__lte=end
    )
    
    # Kapsam bazlı gruplama
    scope_totals = {}
    scope_details = {}
    
    for inp in inputs:
        scope_key = f"scope_{inp.scope}"
        subscope_key = inp.subscope.code
        
        # CO2 hesapla - RAPOR ANINDA
        co2e_value = calculate_emission_for_report(
            inp.scope, 
            inp.subscope.code, 
            inp.data,
            inp.datetime  # Tarih bazlı katsayı için
        )
        
        # Toplam hesapla
        if scope_key not in scope_totals:
            scope_totals[scope_key] = 0
            scope_details[scope_key] = {}
        
        # Alt kapsam detayları
        if subscope_key not in scope_details[scope_key]:
            scope_details[scope_key][subscope_key] = {
                'name': inp.subscope.name,
                'items': [],
                'total': 0
            }
        
        # Veriyi ekle
        scope_details[scope_key][subscope_key]['items'].append({
            'date': inp.datetime.strftime('%d.%m.%Y'),
            'data': inp.data,
            'co2e': co2e_value  # Hesaplanan değer
        })
        
        scope_details[scope_key][subscope_key]['total'] += co2e_value
        scope_totals[scope_key] += co2e_value
    
    # Genel toplam
    total_emission = sum(scope_totals.values())
    
    response_data = {
        'scope_totals': scope_totals,
        'scope_details': scope_details,
        'total_emission': total_emission
    }
    
    return JsonResponse(response_data)


def calculate_emission_for_report(scope, subscope, data, date):
    """Rapor için emisyon hesaplama - CO2e toplamı"""
    
    try:
        # Kapsam 1.1 - Sabit Yanma
        if scope == 1 and subscope == '1.1':
            consumption = float(data.get('consumption', 0))
            coefficient_set = data.get('coefficient_set')
            
            if not coefficient_set:
                return 0
            
            coefficients = CarbonCoefficient.objects.filter(
                scope='1',
                subscope='1.1',
                name=coefficient_set,
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            )
            
            yogunluk = 0
            nkd = 0
            ef_co2 = 0
            ef_ch4 = 0
            ef_n2o = 0
            
            for coef in coefficients:
                if coef.coefficient_type == 'YOGUNLUK_KG_M3':
                    yogunluk = float(coef.value)
                elif coef.coefficient_type == 'NKD':
                    nkd = float(coef.value)
                elif coef.coefficient_type == 'EF_CO2':
                    ef_co2 = float(coef.value)
                elif coef.coefficient_type == 'EF_CH4':
                    ef_ch4 = float(coef.value)
                elif coef.coefficient_type == 'EF_N2O':
                    ef_n2o = float(coef.value)
            
            if yogunluk and nkd:
                co2_ton = consumption * yogunluk * nkd * ef_co2 * 0.000000001
                ch4_ton = consumption * yogunluk * nkd * ef_ch4 * 0.000000001
                n2o_ton = consumption * yogunluk * nkd * ef_n2o * 0.000000001
                co2e_total = co2_ton + (ch4_ton * 27.9) + (n2o_ton * 273)
                return co2e_total
                
        # Kapsam 1.2 - Mobil Yanma
        elif scope == 1 and subscope == '1.2':
            consumption = float(data.get('consumption', 0))
            coefficient_set = data.get('coefficient_set')
            
            if not coefficient_set:
                return 0
                
            coefficients = CarbonCoefficient.objects.filter(
                scope='1',
                subscope='1.2',
                name=coefficient_set,
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            )
            
            yogunluk = 0
            nkd = 0
            ef_co2 = 0
            ef_ch4 = 0
            ef_n2o = 0
            
            for coef in coefficients:
                if coef.coefficient_type == 'YOGUNLUK_TON_LT':
                    yogunluk = float(coef.value)
                elif coef.coefficient_type == 'NKD':
                    nkd = float(coef.value)
                elif coef.coefficient_type == 'EF_CO2':
                    ef_co2 = float(coef.value)
                elif coef.coefficient_type == 'EF_CH4':
                    ef_ch4 = float(coef.value)
                elif coef.coefficient_type == 'EF_N2O':
                    ef_n2o = float(coef.value)
            
            if yogunluk and nkd:
                co2_ton = consumption * yogunluk * 1000 * nkd * ef_co2 * 0.000000001
                ch4_ton = consumption * yogunluk * 1000 * nkd * ef_ch4 * 0.000000001
                n2o_ton = consumption * yogunluk * 1000 * nkd * ef_n2o * 0.000000001
                co2e_total = co2_ton + (ch4_ton * 27.9) + (n2o_ton * 273)
                return co2e_total
                
        # Kapsam 1.4 - Kaçak Emisyonlar
        elif scope == 1 and subscope == '1.4':
            gwp = float(data.get('gwp', 0))  # KIP değeri
            leak_rate = float(data.get('leak_rate', 0))  # Kaçak oranı (katsayı olarak, yüzde değil)
            gas_capacity = float(data.get('gas_capacity', 0))  
            quantity = float(data.get('quantity', 0))
            
            # Excel formülü: (Gaz Kapasitesi × Adet) × KIP / 1000 × Kaçak Oranı
            result = (gas_capacity * quantity) * gwp / 1000 * leak_rate
            return result
                
        # Kapsam 2.1 - Elektrik
        elif scope == 2 and subscope == '2.1':
            consumption = float(data.get('consumption', 0))
            coefficient_set = data.get('coefficient_set')
            
            if not coefficient_set:
                return 0
                
            ef_coef = CarbonCoefficient.objects.filter(
                scope='2',
                subscope='2.1',
                name=coefficient_set,
                coefficient_type='EF_TCO2_MWH',
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            ).first()
            
            if ef_coef:
                ef = float(ef_coef.value)
                result = consumption * ef / 1000
                return result

        # Kapsam 3.1, 3.2, 3.3, 3.4 - Taşımacılık 
        elif scope == 3 and subscope in ['3.1', '3.2', '3.3', '3.4']:
            consumption = float(data.get('consumption', 0))
            coefficient_set = data.get('coefficient_set')
            
            if not coefficient_set:
                return 0
                
            coefficients = CarbonCoefficient.objects.filter(
                scope='3',
                subscope=subscope,
                name=coefficient_set,
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            )
            
            yogunluk = 0
            nkd = 0
            ef_co2 = 0
            ef_ch4 = 0
            ef_n2o = 0
            
            for coef in coefficients:
                # HER İKİ YOĞUNLUK TİPİNİ DE KONTROL ET
                if coef.coefficient_type == 'YOGUNLUK_TON_LT':
                    yogunluk = float(coef.value)
                elif coef.coefficient_type == 'YOGUNLUK_KG_LT':
                    yogunluk = float(coef.value) / 1000  # kg/lt'yi ton/lt'ye çevir
                elif coef.coefficient_type == 'NKD':
                    nkd = float(coef.value)
                elif coef.coefficient_type == 'EF_CO2':
                    ef_co2 = float(coef.value)
                elif coef.coefficient_type == 'EF_CH4':
                    ef_ch4 = float(coef.value)
                elif coef.coefficient_type == 'EF_N2O':
                    ef_n2o = float(coef.value)
            
            if yogunluk and nkd:
                co2_ton = consumption * yogunluk * nkd * ef_co2 * 0.000001
                ch4_ton = consumption * yogunluk * nkd * ef_ch4 * 0.000001
                n2o_ton = consumption * yogunluk * nkd * ef_n2o * 0.000001
                co2e_total = co2_ton + (ch4_ton * 27.9) + (n2o_ton * 273)
                return co2e_total
                
            return 0

        # Kapsam 3.5 - İş Seyahatleri
        elif scope == 3 and subscope == '3.5':
            consumption = float(data.get('consumption', 0))
            coefficient_set = data.get('coefficient_set')  # Şehir adı: Tokyo, Dubai vs.
            travel_type = data.get('travel_type', '')  # flight, vehicle, hotel
            
            if not coefficient_set:
                return 0
            
            # Travel type'a göre doğru katsayı setini belirle
            if travel_type == 'flight':
                search_name = 'Uçak'
            elif travel_type == 'vehicle':
                search_name = 'Taşıt'
            elif travel_type == 'hotel':
                # Otel için şehir adını kullan
                search_name = coefficient_set
            else:
                return 0
            
            coefficients = CarbonCoefficient.objects.filter(
                scope='3',
                subscope='3.5',
                name=search_name,
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            )
            
            if travel_type == 'hotel':
                # Otel için özel hesaplama
                ef_hotel = coefficients.filter(coefficient_type='EF_KG_CO2E_ODA').first()
                if ef_hotel:
                    # consumption = oda*gün sayısı
                    result = consumption * float(ef_hotel.value) / 1000  # kg -> ton
                    return result
            else:
                # Uçak ve Taşıt için normal hesaplama
                yogunluk = 0
                nkd = 0
                ef_co2 = 0
                ef_ch4 = 0
                ef_n2o = 0
                
                for coef in coefficients:
                    if 'YOGUNLUK' in coef.coefficient_type:
                        yogunluk = float(coef.value)
                    elif coef.coefficient_type == 'NKD':
                        nkd = float(coef.value)
                    elif coef.coefficient_type == 'EF_CO2':
                        ef_co2 = float(coef.value)
                    elif coef.coefficient_type == 'EF_CH4':
                        ef_ch4 = float(coef.value)
                    elif coef.coefficient_type == 'EF_N2O':
                        ef_n2o = float(coef.value)
                
                if yogunluk and nkd:
                    if travel_type == 'flight':
                        # Uçak için özel formül
                        co2_ton = (consumption * ef_co2 * nkd * yogunluk * 0.000000001) / 250 * 4
                        ch4_ton = (consumption * ef_ch4 * nkd * yogunluk * 0.000000001) / 250 * 4
                        n2o_ton = (consumption * ef_n2o * nkd * yogunluk * 0.000000001) / 250 * 4
                    else:
                        # Taşıt için formül
                        co2_ton = consumption * yogunluk * nkd * ef_co2 * 0.000001
                        ch4_ton = consumption * yogunluk * nkd * ef_ch4 * 0.000001
                        n2o_ton = consumption * yogunluk * nkd * ef_n2o * 0.000001
                        
                    co2e_total = co2_ton + (ch4_ton * 27.9) + (n2o_ton * 273)
                    return co2e_total

        # Kapsam 4.1 - Satın Alınan Mal ve Hizmetler
        elif scope == 4 and subscope == '4.1':
            amount = float(data.get('amount', 0))  # kg
            material_type = data.get('material_type', '')  # Malzeme ID'si
            coefficient_set = data.get('coefficient_set', '')
            name = data.get('name', '')
            
            # Eğer coefficient_set yoksa, material_type'dan bulmayı dene
            if not coefficient_set and material_type:
                # material_type bir ID olabilir, onu katsayı ismine çevir
                material_coef = CarbonCoefficient.objects.filter(
                    id=material_type
                ).first()
                if material_coef:
                    coefficient_set = material_coef.name
            
            if not coefficient_set:
                return 0
            
            # Katsayıyı bul
            ef_coef = CarbonCoefficient.objects.filter(
                scope='4',
                subscope='4.1',
                name=coefficient_set,
                coefficient_type='EF_KG_CO2_KG',
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            ).first()
            
            if ef_coef:
                ef = float(ef_coef.value)
                result = amount * ef / 1000
                return result
                
            return 0

        # Kapsam 4.2 - Sermaye Malları
        elif scope == 4 and subscope == '4.2':
            amount = float(data.get('amount', 0))  # kg
            coefficient_set = data.get('coefficient_set', '')
            
            if not coefficient_set:
                return 0
            
            # İki tür katsayı olabilir: Materyal ve Proses
            material_ef = 0
            process_ef = 0
            
            coefficients = CarbonCoefficient.objects.filter(
                scope='4',
                subscope='4.2',
                name=coefficient_set,
                valid_from__lte=date
            ).filter(
                Q(valid_to__gte=date) | Q(valid_to__isnull=True)
            )
            
            for coef in coefficients:
                if coef.coefficient_type == 'EF_KG_CO2_KG':
                    material_ef = float(coef.value)
                elif coef.coefficient_type == 'EF_TCO2E_KG':
                    process_ef = float(coef.value)
            
            # Toplam emisyon
            material_emission = amount * material_ef / 1000 if material_ef else 0
            process_emission = amount * process_ef / 1000 if process_ef else 0
            
            result = material_emission + process_emission
            return result

        # Kapsam 4.3 - Kullanılan Hizmetler  
        elif scope == 4 and subscope == '4.3':
            service_type = data.get('service_type', '')
            consumption = float(data.get('consumption', 0))
            amount = float(data.get('amount', 0))  # Eski kayıtlar için
            coefficient_set = data.get('coefficient_set', '')
            
            # Eski kayıtlarda consumption yerine amount olabilir
            if not consumption and amount:
                consumption = amount
            
            if not coefficient_set:
                return 0
            
            if service_type == 'water':
                # Su temini için
                ef_coef = CarbonCoefficient.objects.filter(
                    scope='4',
                    subscope='4.3',
                    name=coefficient_set,
                    coefficient_type='EF_KG_CO2E_M3',
                    valid_from__lte=date
                ).filter(
                    Q(valid_to__gte=date) | Q(valid_to__isnull=True)
                ).first()
                
                if ef_coef:
                    ef = float(ef_coef.value)
                    result = consumption * ef / 1000
                    return result
                    
            elif service_type == 'electricity_loss':
                # Elektrik kayıp-kaçak için - TEK katsayı tipi
                ef_coef = CarbonCoefficient.objects.filter(
                    scope='4',
                    subscope='4.3',
                    name=coefficient_set,
                    coefficient_type='EF_KG_CO2E_KWH',
                    valid_from__lte=date
                ).filter(
                    Q(valid_to__gte=date) | Q(valid_to__isnull=True)
                ).first()
                
                if ef_coef:
                    ef = float(ef_coef.value)
                    # MWh × kgCO2e/kWh = kgCO2e, sonra tona çevir
                    result = consumption * ef / 1000
                    return result
                
            elif service_type == 'solid_waste':
                # Katı atık için
                ef_coef = CarbonCoefficient.objects.filter(
                    scope='4',
                    subscope='4.3',
                    name=coefficient_set,
                    coefficient_type='EF_KG_CO2_TON',
                    valid_from__lte=date
                ).filter(
                    Q(valid_to__gte=date) | Q(valid_to__isnull=True)
                ).first()
                
                if ef_coef:
                    ef = float(ef_coef.value)
                    # kg × (kgCO2/ton) / 1,000,000 = tCO2e
                    result = consumption * ef / 1000000
                    return result
                    
            elif service_type == 'wastewater':
                # Atıksu için - EF_KG_CO2_M3 tipinde
                ef_coef = CarbonCoefficient.objects.filter(
                    scope='4',
                    subscope='4.3',
                    name=coefficient_set,
                    coefficient_type='EF_KG_CO2_M3',
                    valid_from__lte=date
                ).filter(
                    Q(valid_to__gte=date) | Q(valid_to__isnull=True)
                ).first()
                
                if ef_coef:
                    ef = float(ef_coef.value)
                    result = consumption * ef / 1000
                    return result
                    
            elif service_type == 'service':
                # Hizmetler için - yakıt bazlı hesaplama
                yogunluk = 0
                nkd = 0
                ef_co2 = 0
                ef_ch4 = 0
                ef_n2o = 0
                
                coefficients = CarbonCoefficient.objects.filter(
                    scope='4',
                    subscope='4.3',
                    name=coefficient_set,
                    valid_from__lte=date
                ).filter(
                    Q(valid_to__gte=date) | Q(valid_to__isnull=True)
                )
                
                for coef in coefficients:
                    if coef.coefficient_type == 'YOGUNLUK_TON_LT':
                        yogunluk = float(coef.value)
                    elif coef.coefficient_type == 'NKD':
                        nkd = float(coef.value)
                    elif coef.coefficient_type == 'EF_CO2':
                        ef_co2 = float(coef.value)
                    elif coef.coefficient_type == 'EF_CH4':
                        ef_ch4 = float(coef.value)
                    elif coef.coefficient_type == 'EF_N2O':
                        ef_n2o = float(coef.value)
                
                if yogunluk and nkd:
                    # Litre bazlı hesaplama (10^-6)
                    co2_ton = consumption * yogunluk * nkd * ef_co2 * 0.000001
                    ch4_ton = consumption * yogunluk * nkd * ef_ch4 * 0.000001
                    n2o_ton = consumption * yogunluk * nkd * ef_n2o * 0.000001
                    co2e_total = co2_ton + (ch4_ton * 27.9) + (n2o_ton * 273)
                    return co2e_total
            
            return 0



    except Exception as e:
        print(f"Hesaplama hatası: {e}")
        
    return 0  # VARSAYILAN DÖNÜŞ DEĞERİ


@login_required
def api_get_input(request, input_id):
    """Tek bir girişin detaylarını getir"""
    try:
        input_obj = DynamicCarbonInput.objects.get(id=input_id)
        
        # Yetki kontrolü
        if hasattr(request.user, 'user'):
            user_firms = Firm.objects.filter(user_associations__user=request.user.user)
        else:
            user_firms = Firm.objects.filter(user_associations__user=request.user)
            
        if input_obj.firm not in user_firms and not request.user.is_superuser:
            return JsonResponse({'success': False, 'message': 'Yetkiniz yok'})
        
        data = {
            'id': input_obj.id,
            'firm': input_obj.firm.id,
            'datetime': input_obj.datetime.strftime('%Y-%m-%dT%H:%M'),
            'scope': input_obj.scope,
            'subscope': input_obj.subscope.code,
            'data': input_obj.data
        }
        return JsonResponse(data)
    except DynamicCarbonInput.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Kayıt bulunamadı'})

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
    """Son girişleri getir - filtreleme ile"""

    firm_id = request.GET.get('firm')
    scope = request.GET.get('scope')
    subscope = request.GET.get('subscope')

    # Temel filtre
    inputs = DynamicCarbonInput.objects.filter(firm_id=firm_id)

    # Ek filtreler
    if scope:
        inputs = inputs.filter(scope=scope)
    if subscope:
        inputs = inputs.filter(subscope__code=subscope)

    # Sıralama ve limit
    inputs = inputs.order_by('-id')[:100]  # Makul bir limit

    data = []
    for inp in inputs:
        data.append({
            'id': inp.id,
            'datetime': inp.datetime.isoformat(),
            'scope': inp.scope,
            'subscope': inp.subscope.code,
            'subscope_name': inp.subscope.name,
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
    valid_from = request.GET.get('valid_from')  # YENİ
    valid_to = request.GET.get('valid_to')      # YENİ
    
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
    
    # TARİH FİLTRESİ - YENİ EKLENDİ
    if valid_from and valid_to:
        # Her iki tarih de girilmişse: Kesişim mantığı
        from django.db.models import Q
        coefficients = coefficients.filter(
            Q(valid_to__gte=valid_from) | Q(valid_to__isnull=True),
            valid_from__lte=valid_to
        )
    elif valid_from:
        # Sadece başlangıç tarihi girilmişse
        from django.db.models import Q
        coefficients = coefficients.filter(
            Q(valid_to__gte=valid_from) | Q(valid_to__isnull=True)
        )
    elif valid_to:
        # Sadece bitiş tarihi girilmişse
        coefficients = coefficients.filter(valid_from__lte=valid_to)
    
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
        'selected_valid_from': valid_from,  # YENİ
        'selected_valid_to': valid_to,      # YENİ
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
        '4.3': ['EF_KG_CO2E_KWH', 'EF_KG_CO2E_M3', 'EF_KG_CO2_TON', 'EF_KG_CO2_M3', 'EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_TON_LT'],
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
@require_http_methods(["POST", "PUT", "DELETE"])
def api_dynamic_input(request, input_id=None):
    """Dinamik veri girişi kaydet, güncelle veya sil"""
    
    # PUT - Güncelleme
    if request.method == 'PUT' and input_id:
        try:
            input_obj = DynamicCarbonInput.objects.get(id=input_id)
            
            # Yetki kontrolü
            if hasattr(request.user, 'user'):
                user_firms = Firm.objects.filter(user_associations__user=request.user.user)
            else:
                user_firms = Firm.objects.filter(user_associations__user=request.user)
            
            if input_obj.firm not in user_firms and not request.user.is_superuser:
                return JsonResponse({'success': False, 'message': 'Yetkiniz yok'})
            
            # Güncelle
            data = json.loads(request.body)
            input_obj.datetime = data['datetime']
            input_obj.data = data['data']
            input_obj.save()
            
            return JsonResponse({'success': True, 'message': 'Güncellendi'})
            
        except DynamicCarbonInput.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Kayıt bulunamadı'})
    
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

        subscope_names = {
            '1.1': 'Sabit Yanma',
            '1.2': 'Mobil Yanma', 
            '1.3': 'Proses Emisyonları',
            '1.4': 'Kaçak Emisyonlar',
            '1.5': 'AFOLU',
            '2.1': 'Elektrik Tüketimi',
            '3.1': 'Satın Alınan Mal ve Hizmet Taşımacılığı',
            '3.2': 'Satılan Mal ve Hizmet Taşımacılığı',
            '3.3': 'Kiralanan Varlıklar',
            '3.4': 'İşe Gidiş Geliş',
            '3.5': 'İş Seyahatleri',
            '4.1': 'Satın Alınan Mal ve Hizmetler',
            '4.2': 'Sermaye Malları',
            '4.3': 'Atık'
        }
        
        # Alt kapsam bul veya oluştur
        subscope, _ = SubScope.objects.get_or_create(
            scope=data['scope'],
            code=data['subscope'],
            defaults={'name': subscope_names.get(data['subscope'], f"Alt Kapsam {data['subscope']}")}
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
    
    # TARİH FİLTRESİ - DÜZELTME BURADA!
    if valid_from and valid_to:
        from django.db.models import Q
        coefficients = coefficients.filter(
            Q(valid_to__gte=valid_from) | Q(valid_to__isnull=True),
            valid_from__lte=valid_to
        )
    elif valid_from:
        from django.db.models import Q
        coefficients = coefficients.filter(
            Q(valid_to__gte=valid_from) | Q(valid_to__isnull=True)
        )
    elif valid_to:
        coefficients = coefficients.filter(valid_from__lte=valid_to)
    
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
def fueltype_create_view(request):
    return redirect('carbon:management-list')

@login_required
def fueltype_update_view(request, pk):
    return redirect('carbon:management-list')

@login_required
def fueltype_delete_view(request, pk):
    return redirect('carbon:management-list')

@login_required
@permission_required('carbon.view_input_carbon', raise_exception=True)
def input_list_view(request):
    """Karbon girdi sayfası - yeni dinamik sisteme yönlendir"""
    return redirect('carbon:dynamic-input')

@login_required
@permission_required('carbon.view_report_carbon', raise_exception=True)
def report_list_view(request):
    """Karbon rapor sayfası"""
    
    # Kullanıcının erişebileceği firmalar
    if request.user.is_superuser:
        user_firms = Firm.objects.all()
    elif hasattr(request.user, 'user'):
        user_firms = Firm.objects.filter(user_associations__user=request.user.user)
    else:
        user_firms = Firm.objects.filter(user_associations__user=request.user)
    
    # Bugünün tarihi
    from datetime import date
    today = date.today()
    
    context = {
        'user_firms': user_firms,
        'today': today,
    }
    
    return render(request, 'carbon/report.html', context)
