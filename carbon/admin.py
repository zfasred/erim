from django.contrib import admin
from .models import CoefficientType, EmissionFactor, InputCategory, InputData, Report

@admin.register(CoefficientType)
class CoefficientTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')

@admin.register(EmissionFactor)
class EmissionFactorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'value', 'valid_from', 'valid_to')
    list_filter = ('category', 'valid_from')
    search_fields = ('name',)

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