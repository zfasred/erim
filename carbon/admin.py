from django.contrib import admin
from .models import CoefficientType, EmissionFactor, InputCategory, InputData, SubScope, DynamicCarbonInput


@admin.register(SubScope)
class SubScopeAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'scope']
    list_filter = ['scope']
    ordering = ['scope', 'code']

@admin.register(DynamicCarbonInput)
class DynamicCarbonInputAdmin(admin.ModelAdmin):
    list_display = ['firm', 'datetime', 'scope', 'subscope', 'co2e_total', 'created_at']
    list_filter = ['scope', 'firm', 'datetime']
    date_hierarchy = 'datetime'
    readonly_fields = ['co2e_total', 'created_at', 'updated_at']


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

