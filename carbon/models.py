# carbon/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Firm, User
import json
from decimal import Decimal

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
            ("can_manage_user_firm_access", "Karbon için kullanıcı ve firma ilişkisi kurabilir"),
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


class Scope1Data(models.Model):
    """Kapsam 1 - Doğrudan Emisyonlar Veri Girişi"""
    
    COMBUSTION_TYPE = [
        ('stationary', 'Sabit Yanma'),
        ('mobile', 'Mobil Yanma'),
    ]
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    combustion_type = models.CharField(max_length=20, choices=COMBUSTION_TYPE, verbose_name="Yanma Türü")
    
    # Lokasyon bilgisi (ASANSÖR D2, DÖKÜMHANE D3, FRENBU gibi)
    location = models.CharField(max_length=100, verbose_name="Lokasyon/Tesis")
    
    # Yakıt bilgileri
    fuel_type = models.ForeignKey(FuelType, on_delete=models.PROTECT, verbose_name="Yakıt Türü")
    
    # Tüketim değeri (FV - Fuel Value)
    consumption_value = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="Tüketim Değeri")
    consumption_unit = models.CharField(max_length=20, verbose_name="Birim", default="m³")
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Hesaplanan emisyonlar (otomatik hesaplanacak)
    co2_emission = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="CO2 Emisyonu (ton)")
    ch4_emission = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="CH4 Emisyonu (ton)")
    n2o_emission = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="N2O Emisyonu (ton)")
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="Toplam CO2e (ton)")
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 1 Verisi"
        verbose_name_plural = "Kapsam 1 Verileri"
        ordering = ['-period_year', '-period_month', 'location']
        unique_together = ['firm', 'location', 'fuel_type', 'period_year', 'period_month']
    
    def __str__(self):
        return f"{self.firm.name} - {self.location} - {self.period_year}/{self.period_month}"
    
    def calculate_emissions(self):
        """Emisyonları hesapla"""
        # GWP değerleri (IPCC AR6)
        GWP_CH4 = Decimal('27.9')
        GWP_N2O = Decimal('273')
        
        # Formül: Emission = FV × NCV × EF × 10^-9
        if self.fuel_type:
            # CO2 emisyonu
            self.co2_emission = (
                Decimal(str(self.consumption_value)) * 
                self.fuel_type.ncv * 
                self.fuel_type.ef_co2 * 
                Decimal('0.000000001')
            )
            
            # CH4 emisyonu
            self.ch4_emission = (
                Decimal(str(self.consumption_value)) * 
                self.fuel_type.ncv * 
                self.fuel_type.ef_ch4 * 
                Decimal('0.000000001')
            )
            
            # N2O emisyonu
            self.n2o_emission = (
                Decimal(str(self.consumption_value)) * 
                self.fuel_type.ncv * 
                self.fuel_type.ef_n2o * 
                Decimal('0.000000001')
            )
            
            # Toplam CO2e
            self.total_co2e = (
                self.co2_emission + 
                (self.ch4_emission * GWP_CH4) + 
                (self.n2o_emission * GWP_N2O)
            )
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)


class Scope2Data(models.Model):
    """Kapsam 2 - Elektrik ve Enerji Tüketimi"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    location = models.CharField(max_length=100, verbose_name="Lokasyon/Tesis")
    
    # Elektrik tüketimi
    electricity_kwh = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Elektrik Tüketimi (kWh)")
    
    # Grid emisyon faktörü (zaman bazlı olacak)
    grid_emission_factor = models.DecimalField(
        max_digits=10, decimal_places=6, 
        default=0.442,  # Türkiye ortalaması
        verbose_name="Grid Emisyon Faktörü (tCO2/MWh)"
    )
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Hesaplanan emisyon
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="Toplam CO2e (ton)")
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 2 Verisi"
        verbose_name_plural = "Kapsam 2 Verileri"
        ordering = ['-period_year', '-period_month', 'location']
        unique_together = ['firm', 'location', 'period_year', 'period_month']
    
    def __str__(self):
        return f"{self.firm.name} - {self.location} - {self.period_year}/{self.period_month}"
    
    def calculate_emissions(self):
        """Elektrik emisyonlarını hesapla"""
        # Formül: CO2e = kWh * (1/1000) * EF
        electricity_mwh = Decimal(str(self.electricity_kwh)) / Decimal('1000')
        self.total_co2e = electricity_mwh * self.grid_emission_factor
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)


class Scope3Data(models.Model):
    """Kapsam 3 - Ulaşım Emisyonları"""
    
    TRANSPORT_TYPE = [
        ('upstream', 'Tedarik Zinciri Nakliyesi'),
        ('downstream', 'Dağıtım Nakliyesi'),
        ('employee', 'Çalışan Ulaşımı'),
        ('business', 'İş Seyahatleri'),
    ]
    
    TRANSPORT_MODE = [
        ('road', 'Karayolu'),
        ('rail', 'Demiryolu'),
        ('air', 'Havayolu'),
        ('sea', 'Denizyolu'),
    ]
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPE, verbose_name="Nakliye Türü")
    transport_mode = models.CharField(max_length=20, choices=TRANSPORT_MODE, verbose_name="Ulaşım Şekli")
    
    # Araç ve yakıt bilgileri
    vehicle_type = models.CharField(max_length=100, blank=True, verbose_name="Araç Tipi")
    fuel_type = models.ForeignKey(FuelType, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Yakıt Türü")
    
    # Mesafe veya yakıt tüketimi
    distance_km = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, verbose_name="Mesafe (km)")
    fuel_consumption_lt = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True, verbose_name="Yakıt Tüketimi (lt)")
    
    # Yük bilgisi (ton-km hesabı için)
    cargo_weight_ton = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True, verbose_name="Yük Ağırlığı (ton)")
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Hesaplanan emisyon
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="Toplam CO2e (ton)")
    
    # Metadata
    notes = models.TextField(blank=True, verbose_name="Notlar")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 3 Verisi"
        verbose_name_plural = "Kapsam 3 Verileri"
        ordering = ['-period_year', '-period_month', 'transport_type']
    
    def __str__(self):
        return f"{self.firm.name} - {self.get_transport_type_display()} - {self.period_year}/{self.period_month}"


class Scope4Data(models.Model):
    """Kapsam 4 - Satın Alınan Ürünler ve Hizmetler"""
    
    PRODUCT_CATEGORY = [
        ('raw_material', 'Hammadde'),
        ('semi_finished', 'Yarı Mamul'),
        ('service', 'Hizmet'),
        ('capital_good', 'Sermaye Malı'),
        ('consumable', 'Sarf Malzemesi'),
        ('waste', 'Atık Yönetimi'),
    ]
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    product_category = models.CharField(max_length=20, choices=PRODUCT_CATEGORY, verbose_name="Ürün Kategorisi")
    
    # Ürün bilgileri
    product_name = models.CharField(max_length=200, verbose_name="Ürün/Hizmet Adı")
    supplier = models.CharField(max_length=200, blank=True, verbose_name="Tedarikçi")
    
    # Miktar ve birim
    quantity = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="Miktar")
    unit = models.CharField(max_length=20, verbose_name="Birim")  # kg, adet, m³, vb.
    
    # Emisyon faktörü (ürüne özel)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="Emisyon Faktörü (kgCO2e/birim)")
    emission_factor_source = models.CharField(max_length=200, blank=True, verbose_name="EF Kaynağı")
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Hesaplanan emisyon
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, null=True, blank=True, verbose_name="Toplam CO2e (ton)")
    
    # Metadata
    notes = models.TextField(blank=True, verbose_name="Notlar")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 4 Verisi"
        verbose_name_plural = "Kapsam 4 Verileri"
        ordering = ['-period_year', '-period_month', 'product_category', 'product_name']
    
    def __str__(self):
        return f"{self.firm.name} - {self.product_name} - {self.period_year}/{self.period_month}"
    
    def calculate_emissions(self):
        """Satın alınan ürün emisyonlarını hesapla"""
        # Formül: CO2e = Miktar × EF / 1000 (kg'dan ton'a çevrim)
        self.total_co2e = (Decimal(str(self.quantity)) * self.emission_factor) / Decimal('1000')
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)


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


class Report(models.Model):
    """Karbon raporları"""
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    report_date = models.DateField(verbose_name="Rapor Tarihi")
    
    # Kapsam bazlı toplamlar
    scope1_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 1 Toplam (tCO2e)")
    scope2_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 2 Toplam (tCO2e)")
    scope3_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 3 Toplam (tCO2e)")
    scope4_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 4 Toplam (tCO2e)")
    scope5_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 5 Toplam (tCO2e)")
    scope6_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, verbose_name="Kapsam 6 Toplam (tCO2e)")
    
    # Genel toplamlar
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Toplam CO2e (ton)")
    direct_ratio = models.FloatField(verbose_name="Doğrudan Emisyon Oranı (%)")
    indirect_ratio = models.FloatField(verbose_name="Dolaylı Emisyon Oranı (%)")
    
    # Detaylı hesaplamalar JSON formatında
    json_details = models.JSONField(blank=True, null=True, verbose_name="Detaylı Hesaplamalar")
    
    # Metadata
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan Kullanıcı")
    
    # Rapor parametreleri
    report_period_start = models.DateField(verbose_name="Rapor Dönemi Başlangıç")
    report_period_end = models.DateField(verbose_name="Rapor Dönemi Bitiş")
    
    class Meta:
        verbose_name = "Karbon Raporu"
        verbose_name_plural = "Karbon Raporları"
        ordering = ['-report_date']
        permissions = [
            ("view_report_carbon", "Karbon Rapor Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.firm.name} - Rapor ({self.report_date})"
    
    def calculate_totals(self):
        """Tüm kapsamların toplamlarını hesapla"""
        from datetime import datetime
        from django.db.models import Sum
        
        # Dönem filtresi
        year = self.report_period_end.year
        month = self.report_period_end.month
        
        # Kapsam 1
        scope1_data = Scope1Data.objects.filter(
            firm=self.firm,
            period_year=year,
            period_month__lte=month
        ).aggregate(
            total=Sum('total_co2e')
        )
        self.scope1_total = scope1_data['total'] or 0
        
        # Kapsam 2
        scope2_data = Scope2Data.objects.filter(
            firm=self.firm,
            period_year=year,
            period_month__lte=month
        ).aggregate(
            total=Sum('total_co2e')
        )
        self.scope2_total = scope2_data['total'] or 0
        
        # Kapsam 3
        scope3_data = Scope3Data.objects.filter(
            firm=self.firm,
            period_year=year,
            period_month__lte=month
        ).aggregate(
            total=Sum('total_co2e')
        )
        self.scope3_total = scope3_data['total'] or 0
        
        # Kapsam 4
        scope4_data = Scope4Data.objects.filter(
            firm=self.firm,
            period_year=year,
            period_month__lte=month
        ).aggregate(
            total=Sum('total_co2e')
        )
        self.scope4_total = scope4_data['total'] or 0
        
        # Toplam hesaplama
        self.total_co2e = (
            self.scope1_total + 
            self.scope2_total + 
            self.scope3_total + 
            self.scope4_total + 
            self.scope5_total + 
            self.scope6_total
        )
        
        # Doğrudan ve dolaylı oranlar
        if self.total_co2e > 0:
            direct = float(self.scope1_total)
            indirect = float(self.scope2_total + self.scope3_total + self.scope4_total + self.scope5_total + self.scope6_total)
            self.direct_ratio = (direct / float(self.total_co2e)) * 100
            self.indirect_ratio = (indirect / float(self.total_co2e)) * 100
        else:
            self.direct_ratio = 0
            self.indirect_ratio = 0