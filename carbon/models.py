# carbon/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Firm, User
import json
from decimal import Decimal

class CarbonCoefficient(models.Model):
    """Karbon katsayıları - tüm kapsamlar için merkezi yönetim"""
    
    SCOPE_CHOICES = [
        ('1', 'KAPSAM 1'),
        ('2', 'KAPSAM 2'), 
        ('3', 'KAPSAM 3'),
        ('4', 'KAPSAM 4'),
    ]
    
    SUBSCOPE_CHOICES = [
        # Kapsam 1
        ('1.1', 'Kapsam 1.1'),
        ('1.2', 'Kapsam 1.2'),
        ('1.3', 'Kapsam 1.3'),
        ('1.4', 'Kapsam 1.4'),
        ('1.5', 'Kapsam 1.5'),
        # Kapsam 2
        ('2.1', 'Kapsam 2.1'),
        # Kapsam 3
        ('3.1', 'Kapsam 3.1'),
        ('3.2', 'Kapsam 3.2'),
        ('3.3', 'Kapsam 3.3'),
        ('3.4', 'Kapsam 3.4'),
        ('3.5', 'Kapsam 3.5'),
        # Kapsam 4
        ('4.1', 'Kapsam 4.1'),
        ('4.2', 'Kapsam 4.2'),
        ('4.3', 'Kapsam 4.3'),
    ]
    
    COEFFICIENT_TYPE_CHOICES = [
        ('EF_CO2', 'EF (kgCO2/TJ)'),
        ('EF_CH4', 'EF (kgCH4/TJ)'),
        ('EF_N2O', 'EF (kgN2O/TJ)'),
        ('NKD', 'NKD (TJ/Gg)'),
        ('YOGUNLUK_KG_M3', 'Yoğunluk (kg/m³)'),
        ('YOGUNLUK_TON_LT', 'Yoğunluk (ton/lt)'),
        ('YOGUNLUK_KG_LT', 'Yoğunluk (kg/lt)'),
        ('EF_TCO2_MWH', 'EF (tCO2/MWh)'),
        ('EF_KG_CO2_KG', 'EF (kgCO2/kg)'),
        ('EF_TCO2E_KG', 'EF (tCO2e/kg)'),
        ('EF_KG_CO2E_KWH', 'EF (kgCO2e/kWh)'),
        ('EF_KG_CO2E_M3', 'EF (kgCO2e/m³)'),
        ('EF_KG_CO2_TON', 'EF (kgCO2/ton)'),
        ('EF_KG_CO2_M3', 'EF (kgCO2/m³)'),
        ('EF_KG_CO2E_ODA', 'EF (kgCO2e/oda)'),
    ]
    
    # Ana alanlar
    scope = models.CharField(max_length=1, choices=SCOPE_CHOICES, verbose_name="Kapsam")
    subscope = models.CharField(max_length=5, choices=SUBSCOPE_CHOICES, verbose_name="Alt Kapsam")
    coefficient_type = models.CharField(max_length=20, choices=COEFFICIENT_TYPE_CHOICES, verbose_name="Katsayı Türü")
    
    # İsim alanı - "Genel" veya spesifik değerler (Doğalgaz, Otel, Çelik vs.)
    name = models.CharField(max_length=100, default="Genel", verbose_name="İsim")
    
    # Değer ve birim
    value = models.DecimalField(max_digits=20, decimal_places=10, verbose_name="Değer")
    unit = models.CharField(max_length=50, verbose_name="Birim")
    
    # Tarih bazlı geçerlilik
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    
    # Ek bilgiler
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak (ör: IPCC, DEFRA)")
    notes = models.TextField(blank=True, verbose_name="Notlar")
    
    # Zaman damgaları
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_coefficients")

    class Meta:
        verbose_name = "Karbon Katsayısı"
        verbose_name_plural = "Karbon Katsayıları"
        ordering = ['scope', 'subscope', 'coefficient_type', 'name', '-valid_from']
        # Aynı katsayı kombinasyonu için çakışan tarih aralıklarını engellemek isteyebiliriz
        unique_together = [['scope', 'subscope', 'coefficient_type', 'name', 'valid_from']]

    def __str__(self):
        return f"{self.get_subscope_display()} - {self.get_coefficient_type_display()} - {self.name}"
    
    def is_active(self, date=None):
        """Belirli bir tarihte bu katsayının geçerli olup olmadığını kontrol eder"""
        if date is None:
            from django.utils import timezone
            date = timezone.now().date()
        
        if self.valid_from > date:
            return False
        if self.valid_to and self.valid_to < date:
            return False
        return True


class CoefficientType(models.Model):
    """Katsayı türlerini tanımlar (EF_CO2, EF_CH4, EF_N2O, NCV vb.)"""
    name = models.CharField(max_length=100, verbose_name="Katsayı Türü")
    unit = models.CharField(max_length=50, verbose_name="Birim")
    description = models.TextField(blank=True, verbose_name="Açıklama")

    class Meta:
        verbose_name = "Katsayı Türü"
        verbose_name_plural = "Katsayı Türleri"
        permissions = [
            ("view_management_carbon", "Karbon Yönetim Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.name} ({self.unit})"


class FuelType(models.Model):
    density = models.DecimalField(
        max_digits=10, decimal_places=4,
        null=True, blank=True,
        verbose_name="Yoğunluk (kg/m³ veya kg/L)"
    )
    unit = models.CharField(
        max_length=20,
        default="m³",
        verbose_name="Birim"
    )
    """Yakıt türleri ve özellikleri"""
    FUEL_CATEGORY_CHOICES = [
        ('solid', 'Katı Yakıt'),
        ('liquid', 'Sıvı Yakıt'),
        ('gas', 'Gaz Yakıt'),
    ]
    
    code = models.CharField(max_length=50, unique=True, verbose_name="Yakıt Kodu")
    name = models.CharField(max_length=100, verbose_name="Yakıt Adı")
    category = models.CharField(max_length=20, choices=FUEL_CATEGORY_CHOICES, verbose_name="Kategori")
    
    # Net Calorific Value (Net Kalorifik Değer)
    ncv = models.DecimalField(max_digits=12, decimal_places=6, verbose_name="NKD (TJ/Gg)")
    
    # Emission Factors
    ef_co2 = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF CO2 (kgCO2/TJ)")
    ef_ch4 = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF CH4 (kgCH4/TJ)")
    ef_n2o = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF N2O (kgN2O/TJ)")
    
    # Zaman bazlı geçerlilik
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak")
    notes = models.TextField(blank=True, verbose_name="Notlar")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yakıt Türü"
        verbose_name_plural = "Yakıt Türleri"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class EmissionFactor(models.Model):
    """Emisyon faktörleri - tüm kapsamlar için"""
    CATEGORY_CHOICES = [
        ('KAPSAM_1', 'Kapsam 1 - Doğrudan Emisyonlar'),
        ('KAPSAM_2', 'Kapsam 2 - Dolaylı Emisyonlar (Enerji)'),
        ('KAPSAM_3', 'Kapsam 3 - Dolaylı Emisyonlar (Ulaşım)'),
        ('KAPSAM_4', 'Kapsam 4 - Kullanılan Ürünler'),
        ('KAPSAM_5', 'Kapsam 5 - Üretilen Ürünler'),
        ('KAPSAM_6', 'Kapsam 6 - Diğer'),
    ]
    
    SUBCATEGORY_CHOICES = [
        # Kapsam 1
        ('1.1', 'Sabit Yanma'),
        ('1.2', 'Mobil Yanma'),
        ('1.3', 'Proses Emisyonları'),
        ('1.4', 'Kaçak Emisyonlar'),
        ('1.5', 'LULUCF'),
        # Kapsam 2
        ('2.1', 'Elektrik'),
        ('2.2', 'Isıtma/Soğutma'),
        ('2.3', 'Buhar'),
        # Kapsam 3
        ('3.1', 'Upstream Nakliye'),
        ('3.2', 'Downstream Nakliye'),
        ('3.3', 'Çalışan Ulaşımı'),
        ('3.4', 'İş Seyahatleri'),
        # Kapsam 4
        ('4.1', 'Satın Alınan Ürünler'),
        ('4.2', 'Sermaye Malları'),
        ('4.3', 'Atık Yönetimi'),
        ('4.4', 'Kiralık Varlıklar'),
    ]

    type = models.ForeignKey(CoefficientType, on_delete=models.CASCADE, verbose_name="Katsayı Türü")
    name = models.CharField(max_length=255, verbose_name="Faktör Adı")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Kapsam")
    subcategory = models.CharField(max_length=10, choices=SUBCATEGORY_CHOICES, blank=True, verbose_name="Alt Kategori")
    
    value = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Değer")
    unit = models.CharField(max_length=50, verbose_name="Birim")
    
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak")
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    
    notes = models.TextField(blank=True, verbose_name="Notlar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Emisyon Faktörü"
        verbose_name_plural = "Emisyon Faktörleri"
        ordering = ['-valid_from', 'category', 'name']
        permissions = [
            #("can_manage_user_firm_access", "Karbon için kullanıcı ve firma ilişkisi kurabilir"),
            ("view_management_carbon", "Karbon Yönetim Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) - {self.value} {self.unit}"
    
    def get_active_at_date(self, target_date):
        """Belirli bir tarihte geçerli olan faktör değerini döndürür"""
        if self.valid_from <= target_date:
            if self.valid_to is None or self.valid_to >= target_date:
                return self.value
        return None


# Mevcut modellerinizi koruyorum ama geliştirilmiş versiyonlarla birlikte kullanabilirsiniz
class InputCategory(models.Model):
    """Girdi kategorileri - backward compatibility için"""
    name = models.CharField(max_length=100, verbose_name="Girdi Kategorisi")
    scope = models.CharField(max_length=50, choices=EmissionFactor.CATEGORY_CHOICES, verbose_name="Kapsam")

    class Meta:
        verbose_name = "Girdi Kategorisi"
        verbose_name_plural = "Girdi Kategorileri"

    def __str__(self):
        return self.name


class InputData(models.Model):
    """Genel veri girişi - backward compatibility için"""
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    category = models.ForeignKey(InputCategory, on_delete=models.CASCADE, verbose_name="Kategori")
    value = models.FloatField(verbose_name="Değer (FV/Tüketim)")
    unit = models.CharField(max_length=50, verbose_name="Birim")
    period_start = models.DateField(verbose_name="Dönem Başlangıcı")
    period_end = models.DateField(verbose_name="Dönem Bitişi")
    location = models.CharField(max_length=100, blank=True, verbose_name="Lokasyon")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan Kullanıcı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")

    class Meta:
        verbose_name = "Karbon Girdi Verisi"
        verbose_name_plural = "Karbon Girdi Verileri"
        ordering = ['-period_start']
        permissions = [
            ("view_input_carbon", "Karbon Girdi Verisi Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.firm.name} - {self.category.name} ({self.period_start})"


# 1. GWP DEĞERLERİ İÇİN MODEL
class GWPValues(models.Model):
    """Global Warming Potential değerleri"""
    ch4_gwp = models.DecimalField(
        max_digits=6, decimal_places=2, 
        default=Decimal('27.9'),
        verbose_name="CH4 GWP Değeri"
    )
    n2o_gwp = models.DecimalField(
        max_digits=6, decimal_places=2,
        default=Decimal('273'),
        verbose_name="N2O GWP Değeri"
    )
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    source = models.CharField(max_length=100, default="IPCC AR5")
    
    class Meta:
        verbose_name = "GWP Değerleri"
        verbose_name_plural = "GWP Değerleri"
        
    def __str__(self):
        return f"GWP Değerleri ({self.valid_from})"


# 5. EXCEL RAPORU MODELİ
class ExcelReport(models.Model):
    """Excel benzeri rapor"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay")
    
    scope1_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Kapsam 1 Toplam"
    )
    scope2_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Kapsam 2 Toplam"
    )
    scope3_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Kapsam 3 Toplam"
    )
    scope4_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Kapsam 4 Toplam"
    )
    
    total_co2e = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="TOPLAM CO2e"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Excel Raporu"
        verbose_name_plural = "Excel Raporları"
    
    def calculate_totals(self):
        """Tüm kapsamların toplamını hesapla"""
        from django.db.models import Sum
        
        scope1 = Scope1Excel.objects.filter(
            firm=self.firm, year=self.year, month=self.month
        ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
        
        scope2 = Scope2Excel.objects.filter(
            firm=self.firm, year=self.year, month=self.month
        ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
        
        scope4 = Scope4Excel.objects.filter(
            firm=self.firm, year=self.year, month=self.month
        ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
        
        self.scope1_total = scope1
        self.scope2_total = scope2
        self.scope4_total = scope4
        
        self.total_co2e = scope1 + scope2 + self.scope3_total + scope4
    
    def save(self, *args, **kwargs):
        self.calculate_totals()
        super().save(*args, **kwargs)


class SubScope(models.Model):
    """Alt kapsam tanımları"""
    scope = models.IntegerField(choices=[
        (1, 'Kapsam 1'),
        (2, 'Kapsam 2'),
        (3, 'Kapsam 3'),
        (4, 'Kapsam 4'),
    ])
    code = models.CharField(max_length=10)  # "1.1", "1.2" vb.
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        unique_together = ['scope', 'code']
        ordering = ['scope', 'code']
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class DynamicCarbonInput(models.Model):
    """Tek model tüm girişler için"""
    firm = models.ForeignKey('core.Firm', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    scope = models.IntegerField()
    subscope = models.ForeignKey(SubScope, on_delete=models.PROTECT)
    
    # JSON field ile dinamik veri saklama
    data = models.JSONField()
    
    # Hesaplanan değerler
    co2e_total = models.DecimalField(max_digits=15, decimal_places=6, default=0)
    
    # Metadata
    created_by = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['firm', 'datetime']),
            models.Index(fields=['scope', 'subscope']),
        ]