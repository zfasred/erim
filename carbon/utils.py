# carbon/utils.py

from django.db.models import Sum, Count
from datetime import datetime, timedelta
from .models import DynamicCarbonInput

def get_period_data(firm, start_date, end_date, scope=None, subscope=None):
    """
    Belirli tarih aralığındaki verileri çeker
    
    Args:
        firm: Firma objesi
        start_date: Başlangıç tarihi
        end_date: Bitiş tarihi
        scope: Kapsam numarası (opsiyonel)
        subscope: Alt kapsam kodu (opsiyonel)
    
    Returns:
        Dict: total_co2e ve count değerleri
    """
    query = DynamicCarbonInput.objects.filter(
        firm=firm,
        datetime__range=(start_date, end_date)
    )
    
    if scope:
        query = query.filter(scope=scope)
    if subscope:
        query = query.filter(subscope__code=subscope)
    
    return query.aggregate(
        total_co2e=Sum('co2e_total'),
        count=Count('id')
    )

def get_monthly_comparison(firm, year, month):
    """
    Aylık karşılaştırma verisi
    """
    from calendar import monthrange
    
    # Bu ay
    start_date = datetime(year, month, 1)
    last_day = monthrange(year, month)[1]
    end_date = datetime(year, month, last_day, 23, 59, 59)
    
    current_month = get_period_data(firm, start_date, end_date)
    
    # Geçen ay
    if month == 1:
        prev_month = 12
        prev_year = year - 1
    else:
        prev_month = month - 1
        prev_year = year
    
    prev_start = datetime(prev_year, prev_month, 1)
    prev_last_day = monthrange(prev_year, prev_month)[1]
    prev_end = datetime(prev_year, prev_month, prev_last_day, 23, 59, 59)
    
    previous_month = get_period_data(firm, prev_start, prev_end)
    
    return {
        'current': current_month,
        'previous': previous_month,
        'change': calculate_percentage_change(
            previous_month.get('total_co2e', 0),
            current_month.get('total_co2e', 0)
        )
    }

def calculate_percentage_change(old_value, new_value):
    """Yüzde değişim hesapla"""
    if old_value == 0:
        return 100 if new_value > 0 else 0
    return ((new_value - old_value) / old_value) * 100

def get_scope_distribution(firm, start_date, end_date):
    """Kapsam bazlı dağılım"""
    result = {}
    
    for scope in range(1, 5):
        data = get_period_data(firm, start_date, end_date, scope=scope)
        result[f'scope_{scope}'] = data.get('total_co2e', 0) or 0
    
    total = sum(result.values())
    
    # Yüzdeleri hesapla
    percentages = {}
    for key, value in result.items():
        percentages[f'{key}_percentage'] = (value / total * 100) if total > 0 else 0
    
    result.update(percentages)
    result['total'] = total
    
    return result