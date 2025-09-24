# carbon/admin.py
from django.contrib import admin
from .models import (
    SubScope, 
    DynamicCarbonInput, 
    CarbonCoefficient,
    GWPValues,
    FuelType,
    ExcelReport
)


@admin.register(SubScope)
class SubScopeAdmin(admin.ModelAdmin):
    """Alt kapsam yönetimi"""
    list_display = ['code', 'name', 'scope', 'description']
    list_filter = ['scope']
    search_fields = ['code', 'name', 'description']
    ordering = ['scope', 'code']


@admin.register(DynamicCarbonInput)
class DynamicCarbonInputAdmin(admin.ModelAdmin):
    """Karbon veri girişi yönetimi"""
    list_display = ['firm', 'datetime', 'scope', 'subscope', 'co2e_total', 'created_at']
    list_filter = ['scope', 'firm', 'subscope', 'datetime']
    search_fields = ['firm__name']
    date_hierarchy = 'datetime'
    readonly_fields = ['created_at', 'updated_at', 'created_by']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('firm', 'datetime', 'scope', 'subscope')
        }),
        ('Veri', {
            'fields': ('data', 'co2e_total')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Kaydeden kullanıcıyı otomatik ata"""
        if not change:  # Yeni kayıt
            obj.created_by = request.user.user if hasattr(request.user, 'user') else request.user
        super().save_model(request, obj, form, change)


@admin.register(CarbonCoefficient)
class CarbonCoefficientAdmin(admin.ModelAdmin):
    """Karbon katsayıları yönetimi"""
    list_display = ['name', 'scope', 'subscope', 'coefficient_type', 'value', 'unit', 'valid_from', 'valid_to']
    list_filter = ['scope', 'subscope', 'coefficient_type', 'valid_from']
    search_fields = ['name', 'source', 'notes']
    date_hierarchy = 'valid_from'
    ordering = ['scope', 'subscope', 'coefficient_type', 'name', '-valid_from']
    
    fieldsets = (
        ('Kapsam Bilgileri', {
            'fields': ('scope', 'subscope', 'coefficient_type')
        }),
        ('Katsayı Detayları', {
            'fields': ('name', 'value', 'unit')
        }),
        ('Geçerlilik', {
            'fields': ('valid_from', 'valid_to', 'source')
        }),
        ('Ek Bilgiler', {
            'fields': ('notes', 'created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'created_by']
    
    def save_model(self, request, obj, form, change):
        """Kaydeden kullanıcıyı otomatik ata"""
        if not change:
            obj.created_by = request.user.user if hasattr(request.user, 'user') else request.user
        super().save_model(request, obj, form, change)


@admin.register(GWPValues)
class GWPValuesAdmin(admin.ModelAdmin):
    """GWP değerleri yönetimi"""
    list_display = ['valid_from', 'ch4_gwp', 'n2o_gwp', 'source']
    list_filter = ['valid_from', 'source']
    ordering = ['-valid_from']
    
    fieldsets = (
        ('GWP Değerleri', {
            'fields': ('ch4_gwp', 'n2o_gwp')
        }),
        ('Kaynak Bilgileri', {
            'fields': ('valid_from', 'source')
        }),
    )


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    """Yakıt türleri yönetimi"""
    list_display = ['code', 'name', 'category', 'ncv', 'ef_co2', 'ef_ch4', 'ef_n2o', 'valid_from']
    list_filter = ['category', 'valid_from']
    search_fields = ['code', 'name', 'notes']
    ordering = ['category', 'name']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('code', 'name', 'category', 'unit')
        }),
        ('Emisyon Faktörleri', {
            'fields': ('ncv', 'ef_co2', 'ef_ch4', 'ef_n2o', 'density')
        }),
        ('Geçerlilik', {
            'fields': ('valid_from', 'valid_to', 'source')
        }),
        ('Ek Bilgiler', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ExcelReport)
class ExcelReportAdmin(admin.ModelAdmin):
    """Excel raporları yönetimi"""
    list_display = ['firm', 'year', 'month', 'total_co2e', 'generated_at']
    list_filter = ['firm', 'year', 'month']
    search_fields = ['firm__name']
    date_hierarchy = 'generated_at'
    ordering = ['-year', '-month']
    
    readonly_fields = ['generated_at', 'total_co2e', 'scope1_total', 'scope2_total', 
                      'scope3_total', 'scope4_total']
    
    fieldsets = (
        ('Rapor Bilgileri', {
            'fields': ('firm', 'year', 'month')
        }),
        ('Emisyon Toplamları', {
            'fields': ('scope1_total', 'scope2_total', 'scope3_total', 
                      'scope4_total', 'total_co2e'),
            'classes': ('wide',)
        }),
        ('Metadata', {
            'fields': ('generated_by', 'generated_at', 'notes'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Raporu oluşturan kullanıcıyı ata ve toplamları hesapla"""
        if not change:
            obj.generated_by = request.user.user if hasattr(request.user, 'user') else request.user
        obj.calculate_totals()  # Toplamları hesapla
        super().save_model(request, obj, form, change)