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
        ('KAPSAM_2', 'Kapsam 2 - Enerji Dolaylı'),
        ('KAPSAM_3', 'Kapsam 3 - Ulaşım'),
        ('KAPSAM_4', 'Kapsam 4 - Satın Alınan Ürünler'),
        ('KAPSAM_5', 'Kapsam 5 - Ürün Kullanımı'),
        ('KAPSAM_6', 'Kapsam 6 - Diğer'),
    ]

    
    FACTOR_TYPE = [
        ('FUEL', 'Yakıt'),
        ('ELECTRICITY', 'Elektrik'),
        ('MATERIAL', 'Malzeme'),
        ('TRANSPORT', 'Ulaşım'),
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


    factor_type = models.CharField(max_length=20, choices=FACTOR_TYPE, verbose_name="Faktör Türü")

    type = models.ForeignKey(CoefficientType, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Katsayı Türü")
    name = models.CharField(max_length=255, verbose_name="Faktör Adı")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Kapsam")
    subcategory = models.CharField(max_length=50, blank=True, null=True, verbose_name="Alt Kategori")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    
    value = models.DecimalField(max_digits=15, decimal_places=6, verbose_name="Değer")
    unit = models.CharField(max_length=50, blank=True, null=True, verbose_name="Birim")
    
    source = models.CharField(max_length=200, blank=True, verbose_name="Kaynak")
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    
    notes = models.TextField(blank=True, verbose_name="Notlar")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Excel'deki değerler
    ef_co2 = models.DecimalField(max_digits=12, decimal_places=6, verbose_name="CO2 Faktörü (kgCO2/TJ)")
    ef_ch4 = models.DecimalField(max_digits=12, decimal_places=6, default=0, verbose_name="CH4 Faktörü (kgCH4/TJ)")
    ef_n2o = models.DecimalField(max_digits=12, decimal_places=6, default=0, verbose_name="N2O Faktörü (kgN2O/TJ)")
    
    # Yardımcı değerler (Excel'deki NKD ve Yoğunluk)
    ncv = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, 
                             verbose_name="Net Kalorifik Değer (TJ/Gg)")
    density = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, 
                                 verbose_name="Yoğunluk (kg/m³ veya kg/L)")
    
    # Mevcut alanlarınız
    value = models.FloatField(verbose_name="Değer")  # Backward compatibility
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    source = models.CharField(max_length=100, blank=True, verbose_name="Kaynak")
    type = models.ForeignKey('CoefficientType', on_delete=models.CASCADE, 
                            verbose_name="Katsayı Türü", null=True)

    class Meta:
        verbose_name = "Emisyon Faktörü"
        verbose_name_plural = "Emisyon Faktörleri"
        ordering = ['-valid_from', 'category', 'subcategory', 'name']
        unique_together = ['name', 'category', 'subcategory', 'valid_from']  # Güncellendi
        permissions = [
            ("view_management_carbon", "Karbon Yönetim Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) - {self.value} {self.unit} ({self.valid_from})"
    
    def get_active_at_date(self, target_date):
        """Belirli bir tarihte geçerli olan faktör değerini döndürür"""
        if self.valid_from <= target_date:
            if self.valid_to is None or self.valid_to >= target_date:
                return self.value
        return None

# 2. GWP DEĞERLERİ İÇİN YENİ MODEL
class GWPFactor(models.Model):
    """Global Warming Potential Faktörleri"""
    gas = models.CharField(max_length=20, unique=True, verbose_name="Gaz")
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="GWP Değeri")
    source = models.CharField(max_length=100, default="IPCC AR5", verbose_name="Kaynak")
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")
    
    class Meta:
        verbose_name = "GWP Faktörü"
        verbose_name_plural = "GWP Faktörleri"
    
    def __str__(self):
        return f"{self.gas}: {self.value}"

class Scope1Data(models.Model):
    """Kapsam 1 - Doğrudan Emisyonlar (Excel'deki gibi)"""
    
    EMISSION_TYPE = [
        ('STATIONARY', 'Sabit Yanma'),
        ('MOBILE', 'Mobil Yanma'),
        ('PROCESS', 'Proses Emisyonları'),
    ]
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    emission_type = models.CharField(max_length=20, choices=EMISSION_TYPE, verbose_name="Emisyon Tipi")
    
    # Lokasyon/Tesis bilgisi (Excel'deki ASANSÖR D2, DÖKÜMHANE D3 gibi)
    location = models.CharField(max_length=100, verbose_name="Lokasyon/Tesis")
    
    # Yakıt bilgileri
    fuel_name = models.CharField(max_length=100, verbose_name="Yakıt Adı")
    consumption_value = models.DecimalField(max_digits=15, decimal_places=4, 
                                           verbose_name="Tüketim Değeri (FV)")
    consumption_unit = models.CharField(max_length=20, verbose_name="Birim (m³, litre vb.)")
    
    # Emisyon faktörü bağlantısı
    emission_factor = models.ForeignKey(EmissionFactor, on_delete=models.PROTECT, 
                                       verbose_name="Emisyon Faktörü")
    
    # Hesaplanan emisyonlar (Excel formülasyonu ile)
    co2_emission = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="CO2 Emisyonu (ton)")
    ch4_emission = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="CH4 Emisyonu (ton)")
    n2o_emission = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="N2O Emisyonu (ton)")
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                    verbose_name="Toplam CO2e (ton)")
    
    # GWP değerleri (hesaplama anındaki)
    gwp_ch4 = models.DecimalField(max_digits=6, decimal_places=2, default=27.9, 
                                 verbose_name="CH4 GWP")
    gwp_n2o = models.DecimalField(max_digits=6, decimal_places=2, default=273, 
                                 verbose_name="N2O GWP")
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", 
                                      validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
                                  verbose_name="Oluşturan")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 1 Verisi"
        verbose_name_plural = "Kapsam 1 Verileri"
        ordering = ['-period_year', '-period_month', 'location']
        unique_together = ['firm', 'location', 'fuel_name', 'period_year', 'period_month']
    
    def calculate_emissions(self):
        """Excel formülasyonuna göre emisyon hesaplama
        Formül: (FV * EF * NKD * Yoğunluk) * 10^-9
        CO2e = CO2 + (CH4 * 27.9) + (N2O * 273)
        """
        
        ef = self.emission_factor
        multiplier = Decimal('0.000000001')  # 10^-9
        
        if ef.ncv and ef.density:
            # CO2 hesaplama
            self.co2_emission = (
                self.consumption_value * ef.ef_co2 * ef.ncv * ef.density * multiplier
            )
            
            # CH4 hesaplama
            self.ch4_emission = (
                self.consumption_value * ef.ef_ch4 * ef.ncv * ef.density * multiplier
            )
            
            # N2O hesaplama
            self.n2o_emission = (
                self.consumption_value * ef.ef_n2o * ef.ncv * ef.density * multiplier
            )
            
            # Toplam CO2e hesaplama
            self.total_co2e = (
                self.co2_emission + 
                (self.ch4_emission * self.gwp_ch4) + 
                (self.n2o_emission * self.gwp_n2o)
            )
        
        return self.total_co2e
    
    def save(self, *args, **kwargs):
        # GWP değerlerini güncelle
        try:
            gwp_ch4 = GWPFactor.objects.filter(gas='CH4').latest('valid_from')
            self.gwp_ch4 = gwp_ch4.value
        except:
            pass  # Default değeri kullan
        
        try:
            gwp_n2o = GWPFactor.objects.filter(gas='N2O').latest('valid_from')
            self.gwp_n2o = gwp_n2o.value
        except:
            pass  # Default değeri kullan
        
        # Emisyonları hesapla
        self.calculate_emissions()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firm.name} - {self.location} - {self.fuel_name} ({self.period_year}/{self.period_month})"



class Scope2Data(models.Model):
    """Kapsam 2 - İthal Edilen Enerji"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    
    # Tesis/Bölüm bilgisi (Excel'deki gibi)
    facility_name = models.CharField(max_length=100, verbose_name="Tesis/Bölüm")
    
    # Elektrik tüketimi
    electricity_kwh = models.DecimalField(max_digits=15, decimal_places=2, 
                                         verbose_name="Elektrik Tüketimi (kWh)")
    electricity_mwh = models.DecimalField(max_digits=15, decimal_places=4, 
                                         verbose_name="Elektrik Tüketimi (MWh)")
    
    # Emisyon faktörü (Türkiye için 0.442 tCO2/MWh)
    emission_factor = models.DecimalField(max_digits=10, decimal_places=6, 
                                         default=0.442, 
                                         verbose_name="EF (tCO2/MWh)")
    emission_factor_source = models.CharField(max_length=100, 
                                             default="Türkiye Elektrik Şebekesi", 
                                             verbose_name="EF Kaynağı")
    
    # Hesaplanan emisyon
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                    verbose_name="Toplam CO2e (ton)")
    
    # Dönem bilgileri
    period_year = models.IntegerField(verbose_name="Yıl")
    period_month = models.IntegerField(verbose_name="Ay", 
                                      validators=[MinValueValidator(1), MaxValueValidator(12)])
    
    # Metadata
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Kapsam 2 Verisi"
        verbose_name_plural = "Kapsam 2 Verileri"
        ordering = ['-period_year', '-period_month', 'facility_name']
        unique_together = ['firm', 'facility_name', 'period_year', 'period_month']
    
    def calculate_emissions(self):
        """Elektrik emisyonunu hesapla
        Formül: MWh * EF
        """
        # kWh'yi MWh'ye çevir
        self.electricity_mwh = self.electricity_kwh / Decimal('1000')
        
        # CO2e hesapla
        self.total_co2e = self.electricity_mwh * self.emission_factor
        
        return self.total_co2e
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firm.name} - {self.facility_name} - {self.period_year}/{self.period_month}"
    

class ProductCarbonAllocation(models.Model):
    """Ürün Bazlı Karbon Dağılımı (Excel'deki ÜRÜN HESABI sheet'i)"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    
    # Ürün bilgileri
    product_name = models.CharField(max_length=100, verbose_name="Ürün Adı")
    annual_production = models.IntegerField(verbose_name="Yıllık Üretim Adedi")
    annual_weight_kg = models.DecimalField(max_digits=15, decimal_places=2, 
                                          verbose_name="Yıllık Üretim (kg)")
    
    # Yüzde ve dağılım
    weight_percentage = models.DecimalField(max_digits=5, decimal_places=2, 
                                           verbose_name="Ağırlık Yüzdesi (%)")
    allocated_co2e = models.DecimalField(max_digits=15, decimal_places=6, 
                                        verbose_name="Tahsis Edilen CO2e (ton)")
    co2e_per_unit = models.DecimalField(max_digits=10, decimal_places=8, 
                                       verbose_name="Birim Başına CO2e (ton/adet)")
    
    # İlişkili rapor
    report = models.ForeignKey('Report', on_delete=models.CASCADE, 
                              related_name='product_allocations', 
                              verbose_name="İlişkili Rapor")
    
    # Dönem
    period_year = models.IntegerField(verbose_name="Yıl")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Ürün Karbon Dağılımı"
        verbose_name_plural = "Ürün Karbon Dağılımları"
        ordering = ['-period_year', 'product_name']
    
    def calculate_allocation(self, total_weight_kg, total_co2e):
        """Ürüne düşen karbon payını hesapla"""
        # Ağırlık yüzdesi
        self.weight_percentage = (self.annual_weight_kg / total_weight_kg) * 100
        
        # Tahsis edilen CO2e
        self.allocated_co2e = total_co2e * (self.weight_percentage / 100)
        
        # Birim başına CO2e
        if self.annual_production > 0:
            self.co2e_per_unit = self.allocated_co2e / self.annual_production
        else:
            self.co2e_per_unit = 0
        
        return self.co2e_per_unit
    
    def __str__(self):
        return f"{self.product_name} - {self.co2e_per_unit:.6f} tCO2e/adet ({self.period_year})"


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
    """Geliştirilmiş Karbon Raporu"""
    
    # Mevcut alanlar...
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    report_date = models.DateField(verbose_name="Rapor Tarihi")
    
    # Dönem bilgileri
    report_period_start = models.DateField(verbose_name="Rapor Dönemi Başlangıç")
    report_period_end = models.DateField(verbose_name="Rapor Dönemi Bitiş")
    report_year = models.IntegerField(verbose_name="Rapor Yılı")
    report_month = models.IntegerField(null=True, blank=True, verbose_name="Rapor Ayı")
    
    # Kapsam toplamları (Excel'deki TOPLAM KARBON MİKTARI sheet'i)
    scope1_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 1 Toplam (tCO2e)")
    scope2_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 2 Toplam (tCO2e)")
    scope3_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 3 Toplam (tCO2e)")
    scope4_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 4 Toplam (tCO2e)")
    scope5_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 5 Toplam (tCO2e)")
    scope6_total = models.DecimalField(max_digits=15, decimal_places=6, default=0, 
                                      verbose_name="Kapsam 6 Toplam (tCO2e)")
    
    total_co2e = models.DecimalField(max_digits=15, decimal_places=6, 
                                    verbose_name="Toplam CO2e (ton)")
    
    # Oranlar
    direct_ratio = models.FloatField(verbose_name="Doğrudan Emisyon Oranı (%)")
    indirect_ratio = models.FloatField(verbose_name="Dolaylı Emisyon Oranı (%)")
    
    # Detaylı hesaplamalar JSON formatında
    json_details = models.JSONField(blank=True, null=True, 
                                   verbose_name="Detaylı Hesaplamalar")
    
    # Durum
    STATUS_CHOICES = [
        ('DRAFT', 'Taslak'),
        ('COMPLETED', 'Tamamlandı'),
        ('APPROVED', 'Onaylandı'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, 
                            default='DRAFT', verbose_name="Rapor Durumu")
    
    # Metadata
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
                                    verbose_name="Oluşturan")
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, 
                                   related_name='approved_reports', 
                                   verbose_name="Onaylayan")
    approved_at = models.DateTimeField(null=True, blank=True, verbose_name="Onay Tarihi")
    
    class Meta:
        verbose_name = "Karbon Raporu"
        verbose_name_plural = "Karbon Raporları"
        ordering = ['-report_date', '-report_year', '-report_month']
        unique_together = ['firm', 'report_year', 'report_month']
        permissions = [
            ("view_report_carbon", "Karbon Rapor Görüntüleme"),
            ("approve_report_carbon", "Karbon Rapor Onaylama"),
        ]
    
    def calculate_totals(self):
        """Tüm kapsam toplamlarını hesapla"""
        from django.db.models import Sum
        
        # Kapsam 1
        scope1_qs = Scope1Data.objects.filter(
            firm=self.firm,
            period_year=self.report_year,
            period_month=self.report_month
        )
        self.scope1_total = scope1_qs.aggregate(
            total=Sum('total_co2e')
        )['total'] or Decimal('0')
        
        # Kapsam 2
        scope2_qs = Scope2Data.objects.filter(
            firm=self.firm,
            period_year=self.report_year,
            period_month=self.report_month
        )
        self.scope2_total = scope2_qs.aggregate(
            total=Sum('total_co2e')
        )['total'] or Decimal('0')
        
        # Kapsam 3
        scope3_qs = Scope3Data.objects.filter(
            firm=self.firm,
            period_year=self.report_year,
            period_month=self.report_month
        )
        self.scope3_total = scope3_qs.aggregate(
            total=Sum('total_co2e')
        )['total'] or Decimal('0')
        
        # Kapsam 4
        scope4_qs = Scope4Data.objects.filter(
            firm=self.firm,
            period_year=self.report_year,
            period_month=self.report_month
        )
        self.scope4_total = scope4_qs.aggregate(
            total=Sum('total_co2e')
        )['total'] or Decimal('0')
        
        # Toplam
        self.total_co2e = (
            self.scope1_total + self.scope2_total + self.scope3_total + 
            self.scope4_total + self.scope5_total + self.scope6_total
        )
        
        # Oranları hesapla
        if self.total_co2e > 0:
            direct_emissions = self.scope1_total + self.scope2_total
            indirect_emissions = (
                self.scope3_total + self.scope4_total + 
                self.scope5_total + self.scope6_total
            )
            
            self.direct_ratio = float((direct_emissions / self.total_co2e) * 100)
            self.indirect_ratio = float((indirect_emissions / self.total_co2e) * 100)
        else:
            self.direct_ratio = 0
            self.indirect_ratio = 0
        
        return self.total_co2e
    
    def allocate_to_products(self):
        """Karbon emisyonunu ürünlere dağıt"""
        # Ürün ağırlıklarını topla
        products = ProductCarbonAllocation.objects.filter(
            firm=self.firm,
            period_year=self.report_year
        )
        
        total_weight = products.aggregate(
            total=Sum('annual_weight_kg')
        )['total'] or Decimal('1')
        
        # Her ürüne dağıt
        for product in products:
            product.calculate_allocation(total_weight, self.total_co2e)
            product.report = self
            product.save()
    
    def save(self, *args, **kwargs):
        # Rapor yılını ayarla
        if not self.report_year and self.report_period_end:
            self.report_year = self.report_period_end.year
        
        # Totalleri hesapla
        if self.pk:  # Eğer kayıt varsa
            self.calculate_totals()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        month_str = f"/{self.report_month}" if self.report_month else " (Yıllık)"
        return f"{self.firm.name} - {self.report_year}{month_str} Karbon Raporu"


# 1. GWP DEĞERLERİ İÇİN SABİT MODEL
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

# 2. YAKIT TÜRLERİ İÇİN DETAYLI MODEL
class FuelType(models.Model):
    """Excel'deki yakıt türleri ve katsayıları"""
    name = models.CharField(max_length=100, verbose_name="Yakıt Adı")
    
    # Excel'deki değerler
    ef_co2 = models.DecimalField(
        max_digits=12, decimal_places=2,
        verbose_name="EF CO2 (kgCO2/TJ)"
    )
    ef_ch4 = models.DecimalField(
        max_digits=12, decimal_places=4,
        verbose_name="EF CH4 (kgCH4/TJ)"
    )
    ef_n2o = models.DecimalField(
        max_digits=12, decimal_places=4,
        verbose_name="EF N2O (kgN2O/TJ)"
    )
    nkd = models.DecimalField(
        max_digits=10, decimal_places=4,
        verbose_name="NKD (TJ/Gg)"
    )
    density = models.DecimalField(
        max_digits=10, decimal_places=4,
        verbose_name="Yoğunluk (kg/m³ veya kg/L)"
    )
    unit = models.CharField(max_length=20, verbose_name="Birim")
    
    class Meta:
        verbose_name = "Yakıt Türü"
        verbose_name_plural = "Yakıt Türleri"
    
    def __str__(self):
        return self.name

# 3. KAPSAM 1 - EXCEL'DEKİ GİBİ
class Scope1Excel(models.Model):
    """Kapsam 1 - Excel formülasyonuyla"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, verbose_name="Lokasyon (ASANSÖR D2, vb.)")
    fuel_type = models.ForeignKey(FuelType, on_delete=models.PROTECT)
    
    # Tüketim değeri (FV)
    consumption_value = models.DecimalField(
        max_digits=15, decimal_places=2,
        verbose_name="Tüketim Değeri (FV)"
    )
    
    # Hesaplanan değerler (Excel formülü ile)
    co2_emission = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="CO2 Emisyonu (ton)"
    )
    ch4_emission = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="CH4 Emisyonu (ton)"
    )
    n2o_emission = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="N2O Emisyonu (ton)"
    )
    co2e_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Toplam CO2e (ton)"
    )
    
    # Dönem
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay")
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Kapsam 1 (Excel)"
        verbose_name_plural = "Kapsam 1 Verileri (Excel)"
    
    def calculate_emissions(self):
        """Excel'deki formülü uygula
        Formül: (FV * EF * NKD * Yoğunluk) * 10^-9
        """
        multiplier = Decimal('0.000000001')  # 10^-9
        
        # CO2 hesaplama
        self.co2_emission = (
            self.consumption_value * 
            self.fuel_type.ef_co2 * 
            self.fuel_type.nkd * 
            self.fuel_type.density * 
            multiplier
        )
        
        # CH4 hesaplama
        self.ch4_emission = (
            self.consumption_value * 
            self.fuel_type.ef_ch4 * 
            self.fuel_type.nkd * 
            self.fuel_type.density * 
            multiplier
        )
        
        # N2O hesaplama
        self.n2o_emission = (
            self.consumption_value * 
            self.fuel_type.ef_n2o * 
            self.fuel_type.nkd * 
            self.fuel_type.density * 
            multiplier
        )
        
        # GWP değerlerini al
        gwp = GWPValues.objects.first()
        if gwp:
            ch4_gwp = gwp.ch4_gwp
            n2o_gwp = gwp.n2o_gwp
        else:
            ch4_gwp = Decimal('27.9')
            n2o_gwp = Decimal('273')
        
        # Toplam CO2e = CO2 + (CH4 * 27.9) + (N2O * 273)
        self.co2e_total = (
            self.co2_emission + 
            (self.ch4_emission * ch4_gwp) + 
            (self.n2o_emission * n2o_gwp)
        )
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firm.name} - {self.location} - {self.fuel_type.name}"

# 4. KAPSAM 2 - EXCEL'DEKİ GİBİ
class Scope2Excel(models.Model):
    """Kapsam 2 - Elektrik tüketimi"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    facility = models.CharField(max_length=100, verbose_name="Tesis/Bölüm")
    
    # Elektrik tüketimi
    electricity_kwh = models.DecimalField(
        max_digits=15, decimal_places=2,
        verbose_name="Elektrik (kWh)"
    )
    electricity_mwh = models.DecimalField(
        max_digits=15, decimal_places=4,
        verbose_name="Elektrik (MWh)", 
        blank=True, null=True
    )
    
    # Emisyon faktörü (Türkiye için 0.442)
    emission_factor = models.DecimalField(
        max_digits=10, decimal_places=4,
        default=Decimal('0.442'),
        verbose_name="EF (tCO2/MWh)"
    )
    
    # Hesaplanan emisyon
    co2e_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Toplam CO2e (ton)"
    )
    
    # Dönem
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay")
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Kapsam 2 (Excel)"
        verbose_name_plural = "Kapsam 2 Verileri (Excel)"
    
    def calculate_emissions(self):
        """Excel'deki formülü uygula
        Formül: MWh * EF
        """
        # kWh'yi MWh'ye çevir
        self.electricity_mwh = self.electricity_kwh / Decimal('1000')
        
        # CO2e hesapla
        self.co2e_total = self.electricity_mwh * self.emission_factor
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firm.name} - {self.facility}"

# 5. KAPSAM 4 - EXCEL'DEKİ GİBİ
class Scope4Excel(models.Model):
    """Kapsam 4 - Satın alınan malzemeler"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100, verbose_name="Malzeme Adı")
    
    quantity_kg = models.DecimalField(
        max_digits=15, decimal_places=2,
        verbose_name="Miktar (kg)"
    )
    
    emission_factor = models.DecimalField(
        max_digits=10, decimal_places=4,
        verbose_name="EF (kgCO2e/kg)"
    )
    
    co2e_total = models.DecimalField(
        max_digits=15, decimal_places=9,
        default=0, verbose_name="Toplam CO2e (ton)"
    )
    
    # Dönem
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay")
    
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Kapsam 4 (Excel)"
        verbose_name_plural = "Kapsam 4 Verileri (Excel)"
    
    def calculate_emissions(self):
        """Excel'deki formülü uygula
        Formül: Miktar(kg) * EF / 1000 (ton'a çevrim)
        """
        self.co2e_total = (self.quantity_kg * self.emission_factor) / Decimal('1000')
    
    def save(self, *args, **kwargs):
        self.calculate_emissions()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.firm.name} - {self.material_name}"


# 6. EXCEL RAPORU İÇİN GÜNCELLEME
class ExcelReport(models.Model):
    """Excel'deki gibi toplamları tutan rapor"""
    
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="Yıl")
    month = models.IntegerField(verbose_name="Ay")
    
    # Kapsam toplamları (Excel'deki gibi)
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
        
        # Kapsam 1
        scope1 = Scope1Excel.objects.filter(
            firm=self.firm, year=self.year, month=self.month
        ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
        
        # Kapsam 2
        scope2 = Scope2Excel.objects.filter(
            firm=self.firm, year=self.year, month=self.month
        ).aggregate(total=Sum('co2e_total'))['total'] or Decimal('0')
        
        # Kapsam 4
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
    
    def __str__(self):
        return f"{self.firm.name} - {self.year}/{self.month} Raporu"

