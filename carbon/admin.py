# carbon/admin.py
from django.contrib import admin
from .models import (
    CoefficientType, EmissionFactor, InputCategory, InputData, Report, 
    FuelType, GWPValues, Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport
)

# FuelType admin
@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'ncv', 'ef_co2', 'valid_from', 'valid_to']
    list_filter = ['category', 'valid_from']
    search_fields = ['code', 'name']
    ordering = ['category', 'name']

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

# CoefficientType admin
@admin.register(CoefficientType)
class CoefficientTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

# EmissionFactor admin
@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'value', 'valid_from', 'valid_to']
    list_filter = ['type', 'valid_from']
    search_fields = ['name']

# InputCategory admin
@admin.register(InputCategory)
class InputCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'scope']
    list_filter = ['scope']
    search_fields = ['name']

# InputData admin
@admin.register(InputData)
class InputDataAdmin(admin.ModelAdmin):
    list_display = ['firm', 'category', 'value', 'unit', 'period_start', 'period_end']
    list_filter = ['firm', 'category', 'period_start']
    search_fields = ['firm__name']
    date_hierarchy = 'period_start'

# Report admin
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['firm', 'report_date', 'total_co2e', 'status', 'generated_at']
    list_filter = ['status', 'report_date', 'firm']
    search_fields = ['firm__name']
    date_hierarchy = 'report_date'
    readonly_fields = ['generated_at', 'generated_by']