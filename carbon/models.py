# carbon/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
from core.models import User, Firm

# ============================================
# ANA MODELLER
# ============================================

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
        verbose_name = "Alt Kapsam"
        verbose_name_plural = "Alt Kapsamlar"
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class DynamicCarbonInput(models.Model):
    """Tüm kapsam verileri için tek model"""
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    datetime = models.DateTimeField(verbose_name="Tarih/Zaman")
    scope = models.IntegerField(verbose_name="Kapsam")
    subscope = models.ForeignKey(SubScope, on_delete=models.PROTECT, verbose_name="Alt Kapsam")
    
    # JSON field ile dinamik veri saklama
    data = models.JSONField(verbose_name="Veri")
    
    # Hesaplanan değerler
    co2e_total = models.DecimalField(
        max_digits=15, 
        decimal_places=6, 
        default=0,
        verbose_name="Toplam CO2e"
    )
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['firm', 'datetime']),
            models.Index(fields=['scope', 'subscope']),
        ]
        ordering = ['-datetime']
        verbose_name = "Karbon Verisi"
        verbose_name_plural = "Karbon Verileri"
        
    def __str__(self):
        return f"{self.firm.name} - Kapsam {self.scope} - {self.datetime.date()}"
    
    def calculate_emissions(self):
        """Emisyon hesaplama - override edilebilir"""
        # Burada subscope'a göre farklı hesaplama mantıkları uygulanabilir
        pass


class CarbonCoefficient(models.Model):
    """Tüm karbon katsayıları için tek model"""
    
    # Kapsam tanımları
    SCOPE_CHOICES = [
        ('1', 'Kapsam 1'),
        ('2', 'Kapsam 2'),
        ('3', 'Kapsam 3'),
        ('4', 'Kapsam 4'),
    ]
    
    # Alt kapsam tanımları
    SUBSCOPE_CHOICES = [
        ('1.1', '1.1 - Sabit Yanma'),
        ('1.2', '1.2 - Mobil Yanma'),
        ('1.3', '1.3 - Proses Emisyonları'),
        ('1.4', '1.4 - Kaçak Emisyonlar'),
        ('1.5', '1.5 - AFOLU'),
        ('2.1', '2.1 - Elektrik Tüketimi'),
        ('3.1', '3.1 - Satın Alınan Mal ve Hizmet Taşımacılığı'),
        ('3.2', '3.2 - Satılan Mal ve Hizmet Taşımacılığı'),
        ('3.3', '3.3 - Kiralanan Varlıklar'),
        ('3.4', '3.4 - İşe Gidiş Geliş'),
        ('3.5', '3.5 - İş Seyahatleri'),
        ('4.1', '4.1 - Satın Alınan Mal ve Hizmetler'),
        ('4.2', '4.2 - Sermaye Malları'),
        ('4.3', '4.3 - Atık'),
    ]
    
    # Katsayı türleri
    COEFFICIENT_TYPE_CHOICES = [
        ('EF_CO2', 'CO2 Emisyon Faktörü'),
        ('EF_CH4', 'CH4 Emisyon Faktörü'),
        ('EF_N2O', 'N2O Emisyon Faktörü'),
        ('NKD', 'Net Kalorifik Değer'),
        ('YOGUNLUK_KG_M3', 'Yoğunluk (kg/m³)'),
        ('YOGUNLUK_KG_LT', 'Yoğunluk (kg/L)'),
        ('YOGUNLUK_TON_LT', 'Yoğunluk (ton/L)'),
        ('EF_TCO2_MWH', 'Emisyon Faktörü (tCO2/MWh)'),
        ('EF_KG_CO2E_ODA', 'Emisyon Faktörü (kgCO2e/oda.gece)'),
        ('EF_KG_CO2_KG', 'Emisyon Faktörü (kgCO2/kg)'),
        ('EF_TCO2E_KG', 'Emisyon Faktörü (tCO2e/kg)'),
        ('EF_KG_CO2E_KWH', 'Emisyon Faktörü (kgCO2e/kWh)'),
        ('EF_KG_CO2E_M3', 'Emisyon Faktörü (kgCO2e/m³)'),
        ('EF_KG_CO2_TON', 'Emisyon Faktörü (kgCO2/ton)'),
        ('EF_KG_CO2_M3', 'Emisyon Faktörü (kgCO2/m³)'),
    ]
    
    scope = models.CharField(max_length=1, choices=SCOPE_CHOICES, verbose_name="Kapsam")
    subscope = models.CharField(max_length=3, choices=SUBSCOPE_CHOICES, verbose_name="Alt Kapsam")
    coefficient_type = models.CharField(
        max_length=20, 
        choices=COEFFICIENT_TYPE_CHOICES,
        verbose_name="Katsayı Türü"
    )
    
    name = models.CharField(max_length=255, verbose_name="İsim")
    value = models.DecimalField(max_digits=20, decimal_places=10, verbose_name="Değer")
    unit = models.CharField(max_length=50, verbose_name="Birim")
    
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak")
    notes = models.TextField(blank=True, verbose_name="Notlar")
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['scope', 'subscope', 'coefficient_type', 'name', '-valid_from']
        verbose_name = "Karbon Katsayısı"
        verbose_name_plural = "Karbon Katsayıları"
        indexes = [
            models.Index(fields=['scope', 'subscope']),
            models.Index(fields=['coefficient_type']),
            models.Index(fields=['valid_from', 'valid_to']),
        ]
    
    def __str__(self):
        return f"{self.get_subscope_display()} - {self.name} - {self.get_coefficient_type_display()}"
    
    @property
    def is_active(self):
        """Bu katsayının şu anda geçerli olup olmadığını kontrol eder"""
        from django.utils import timezone
        today = timezone.now().date()
        
        if self.valid_from > today:
            return False
        if self.valid_to and self.valid_to < today:
            return False
        return True
    
    def is_active_at_date(self, date):
        """Belirli bir tarihte bu katsayının geçerli olup olmadığını kontrol eder"""
        if self.valid_from > date:
            return False
        if self.valid_to and self.valid_to < date:
            return False
        return True
    
    def clean(self):
        """Model validasyonu"""
        if self.valid_to and self.valid_from > self.valid_to:
            raise ValidationError("Geçerlilik bitişi başlangıçtan önce olamaz.")
        
        # Aynı dönem için çakışma kontrolü
        overlapping = CarbonCoefficient.objects.filter(
            scope=self.scope,
            subscope=self.subscope,
            coefficient_type=self.coefficient_type,
            name=self.name
        ).exclude(pk=self.pk)
        
        if self.valid_to:
            overlapping = overlapping.filter(
                models.Q(valid_from__lte=self.valid_to) & 
                (models.Q(valid_to__gte=self.valid_from) | models.Q(valid_to__isnull=True))
            )
        else:
            overlapping = overlapping.filter(
                models.Q(valid_to__gte=self.valid_from) | models.Q(valid_to__isnull=True)
            )
        
        if overlapping.exists():
            raise ValidationError("Bu tarih aralığında aynı katsayı zaten mevcut.")
    
    @classmethod
    def get_active_coefficient(cls, scope, subscope, coefficient_type, name, date=None):
        """Belirli bir tarihte geçerli katsayıyı getir"""
        from datetime import date as dt
        if date is None:
            date = dt.today()
        
        return cls.objects.filter(
            scope=scope,
            subscope=subscope,
            coefficient_type=coefficient_type,
            name=name,
            valid_from__lte=date
        ).filter(
            models.Q(valid_to__gte=date) | models.Q(valid_to__isnull=True)
        ).first()


# ============================================
# YARDIMCI MODELLER
# ============================================

class GWPValues(models.Model):
    """Global Warming Potential değerleri"""
    ch4_gwp = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        default=Decimal('27.9'),
        verbose_name="CH4 GWP Değeri"
    )
    n2o_gwp = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default=Decimal('273'),
        verbose_name="N2O GWP Değeri"
    )
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    source = models.CharField(max_length=100, default="IPCC AR5", verbose_name="Kaynak")
    
    class Meta:
        verbose_name = "GWP Değeri"
        verbose_name_plural = "GWP Değerleri"
        ordering = ['-valid_from']
        
    def __str__(self):
        return f"GWP Değerleri ({self.valid_from})"


class FuelType(models.Model):
    """Yakıt türleri - Opsiyonel, CarbonCoefficient ile birleştirilebilir"""
    CATEGORY_CHOICES = [
        ('solid', 'Katı Yakıt'),
        ('liquid', 'Sıvı Yakıt'),
        ('gas', 'Gaz Yakıt'),
    ]
    
    code = models.CharField(max_length=50, unique=True, verbose_name="Yakıt Kodu")
    name = models.CharField(max_length=100, verbose_name="Yakıt Adı")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategori")
    ncv = models.DecimalField(max_digits=12, decimal_places=6, verbose_name="NKD (TJ/Gg)")
    ef_co2 = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF CO2 (kgCO2/TJ)")
    ef_ch4 = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF CH4 (kgCH4/TJ)")
    ef_n2o = models.DecimalField(max_digits=12, decimal_places=4, verbose_name="EF N2O (kgN2O/TJ)")
    density = models.DecimalField(
        max_digits=10, 
        decimal_places=4, 
        null=True, 
        blank=True,
        verbose_name="Yoğunluk (kg/m³ veya kg/L)"
    )
    unit = models.CharField(max_length=20, default='m³', verbose_name="Birim")
    
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(blank=True, null=True, verbose_name="Geçerlilik Bitişi")
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak")
    notes = models.TextField(blank=True, verbose_name="Notlar")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Yakıt Türü"
        verbose_name_plural = "Yakıt Türleri"
        ordering = ['name']
        
    def __str__(self):
        return f"{self.code} - {self.name}"


class ExcelReport(models.Model):
    """Excel benzeri raporlar için"""
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay", null=True, blank=True)
    
    scope1_total = models.DecimalField(
        max_digits=15, decimal_places=6,
        default=0, verbose_name="Kapsam 1 Toplam"
    )
    scope2_total = models.DecimalField(
        max_digits=15, decimal_places=6,
        default=0, verbose_name="Kapsam 2 Toplam"
    )
    scope3_total = models.DecimalField(
        max_digits=15, decimal_places=6,
        default=0, verbose_name="Kapsam 3 Toplam"
    )
    scope4_total = models.DecimalField(
        max_digits=15, decimal_places=6,
        default=0, verbose_name="Kapsam 4 Toplam"
    )
    
    total_co2e = models.DecimalField(
        max_digits=15, decimal_places=6,
        default=0, verbose_name="TOPLAM CO2e"
    )
    
    # Metadata
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    notes = models.TextField(blank=True, verbose_name="Notlar")
    
    class Meta:
        verbose_name = "Excel Raporu"
        verbose_name_plural = "Excel Raporları"
        ordering = ['-year', '-month']
        unique_together = ['firm', 'year', 'month']
    
    def __str__(self):
        if self.month:
            return f"{self.firm.name} - {self.year}/{self.month:02d}"
        return f"{self.firm.name} - {self.year} (Yıllık)"
    
    def calculate_totals(self):
        """Tüm kapsamların toplamını hesapla"""
        from django.db.models import Sum
        
        # Tarih aralığını belirle
        from datetime import datetime, date
        if self.month:
            from calendar import monthrange
            start_date = datetime(self.year, self.month, 1)
            last_day = monthrange(self.year, self.month)[1]
            end_date = datetime(self.year, self.month, last_day, 23, 59, 59)
        else:
            start_date = datetime(self.year, 1, 1)
            end_date = datetime(self.year, 12, 31, 23, 59, 59)
        
        # Her kapsam için toplamları hesapla
        for scope_num in [1, 2, 3, 4]:
            scope_total = DynamicCarbonInput.objects.filter(
                firm=self.firm,
                scope=scope_num,
                datetime__range=(start_date, end_date)
            ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
            
            setattr(self, f'scope{scope_num}_total', scope_total)
        
        # Genel toplamı hesapla
        self.total_co2e = (
            self.scope1_total + self.scope2_total + 
            self.scope3_total + self.scope4_total
        )
    
    def save(self, *args, **kwargs):
        """Kaydetmeden önce toplamları hesapla"""
        self.calculate_totals()
        super().save(*args, **kwargs)