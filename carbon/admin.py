from django.contrib import admin
from .models import CoefficientType, EmissionFactor, InputCategory, InputData, Report, FuelType, GWPValues, Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport


# YAKIT TÜRLERİ
@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'ef_co2', 'ef_ch4', 'ef_n2o', 'nkd', 'density', 'unit']
    search_fields = ['name']

# GWP DEĞERLERİ
@admin.register(GWPValues)
class GWPValuesAdmin(admin.ModelAdmin):
    list_display = ['ch4_gwp', 'n2o_gwp', 'valid_from', 'source']

# KAPSAM 1
@admin.register(Scope1Excel)
class Scope1ExcelAdmin(admin.ModelAdmin):
    list_display = ['firm', 'location', 'fuel_type', 'consumption_value', 
                    'co2_emission', 'ch4_emission', 'n2o_emission', 'co2e_total']
    list_filter = ['firm', 'fuel_type', 'year', 'month']
    readonly_fields = ['co2_emission', 'ch4_emission', 'n2o_emission', 'co2e_total']

# KAPSAM 2
@admin.register(Scope2Excel)
class Scope2ExcelAdmin(admin.ModelAdmin):
    list_display = ['firm', 'facility', 'electricity_kwh', 'electricity_mwh', 'co2e_total']
    list_filter = ['firm', 'year', 'month']
    readonly_fields = ['electricity_mwh', 'co2e_total']

# KAPSAM 4
@admin.register(Scope4Excel)
class Scope4ExcelAdmin(admin.ModelAdmin):
    list_display = ['firm', 'material_name', 'quantity_kg', 'emission_factor', 'co2e_total']
    list_filter = ['firm', 'year', 'month']
    readonly_fields = ['co2e_total']

# EXCEL RAPORU
@admin.register(ExcelReport)
class ExcelReportAdmin(admin.ModelAdmin):
    list_display = ['firm', 'year', 'month', 'scope1_total', 'scope2_total', 
                    'scope4_total', 'total_co2e']
    list_filter = ['firm', 'year', 'month']
    readonly_fields = ['scope1_total', 'scope2_total', 'scope3_total', 
                      'scope4_total', 'total_co2e']
    
    def save_model(self, request, obj, form, change):
        """Kaydetmeden önce toplamları hesapla"""
        obj.calculate_totals()
        super().save_model(request, obj, form, change)


@admin.register(CoefficientType)
class CoefficientTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'category', 
        'subcategory',  # YENİ
        'value', 
        'unit',
        'valid_from', 
        'valid_to',
        'is_active'  # YENİ
    )
    
    list_filter = (
        'category',
        'subcategory',  # YENİ
        'is_active',  # YENİ
        'valid_from'
    )
    
    search_fields = ('name', 'category', 'subcategory')
    
    list_editable = ('is_active',)  # YENİ - Listeden direkt düzenlenebilir
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'category', 'subcategory', 'value', 'unit')
        }),
        ('Geçerlilik', {
            'fields': ('valid_from', 'valid_to', 'is_active')
        }),
        ('Ek Bilgiler', {
            'fields': ('source', 'type'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """Admin listesinde varsayılan sıralama"""
        qs = super().get_queryset(request)
        return qs.order_by('-is_active', 'category', 'subcategory', 'name')

@admin.register(InputCategory)
class InputCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'scope')

@admin.register(InputData)
class InputDataAdmin(admin.ModelAdmin):
    list_display = ('firm', 'category', 'value', 'period_start')
    list_filter = ('firm', 'category')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('firm', 'report_date', 'total_co2e')
    list_filter = ('firm', 'report_date')