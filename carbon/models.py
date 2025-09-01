from django.db import models
from core.models import Firm, User  # Import existing models from core for firm and user associations

class CoefficientType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Katsayı Türü")  # e.g., 'EF_CO2', 'NKD', 'KIP'
    unit = models.CharField(max_length=50, verbose_name="Birim")  # e.g., 'kgCO2/TJ'
    description = models.TextField(blank=True, verbose_name="Açıklama")

    class Meta:
        verbose_name = "Katsayı Türü"
        verbose_name_plural = "Katsayı Türleri"
        permissions = [
            ("view_management_carbon", "Karbon Yönetim Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return self.name

class EmissionFactor(models.Model):
    CATEGORY_CHOICES = [
        ('KAPSAM_1', 'Kapsam 1'),
        ('KAPSAM_2', 'Kapsam 2'),
        ('KAPSAM_3', 'Kapsam 3'),
        ('KAPSAM_4', 'Kapsam 4'),
        ('KAPSAM_5', 'Kapsam 5'),
        ('KAPSAM_6', 'Kapsam 6'),
    ]

    type = models.ForeignKey(CoefficientType, on_delete=models.CASCADE, verbose_name="Katsayı Türü", default=1)  # Use the ID from Step 3 as default
    name = models.CharField(max_length=255, verbose_name="Faktör Adı")  # e.g., 'Motorin', 'Elektrik'
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Kategori/Kapsam")
    value = models.FloatField(verbose_name="Değer (Katsayı)")
    source = models.CharField(max_length=100, blank=True, verbose_name="Kaynak")  # e.g., 'IPCC', 'DEFRA'
    valid_from = models.DateField(verbose_name="Geçerlilik Başlangıcı")
    valid_to = models.DateField(null=True, blank=True, verbose_name="Geçerlilik Bitişi")

    class Meta:
        verbose_name = "Emisyon Faktörü"
        verbose_name_plural = "Emisyon Faktörleri"
        ordering = ['-valid_from', 'name']
        permissions = [
            ("can_manage_user_firm_access", "Karbon için kullanıcı ve firma ilişkisi kurabilir"),
            ("view_management_carbon", "Karbon Yönetim Görüntüleme Hakkı"),
        ]

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.value} {self.type.unit}"

class InputCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Girdi Kategorisi")  # e.g., 'Sabit Yanma', 'Ulaşım'
    scope = models.CharField(max_length=50, choices=EmissionFactor.CATEGORY_CHOICES, verbose_name="Kapsam")

    class Meta:
        verbose_name = "Girdi Kategorisi"
        verbose_name_plural = "Girdi Kategorileri"

    def __str__(self):
        return self.name

class InputData(models.Model):
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    category = models.ForeignKey(InputCategory, on_delete=models.CASCADE, verbose_name="Kategori")
    value = models.FloatField(verbose_name="Değer (FV/Tüketim)")
    unit = models.CharField(max_length=50, verbose_name="Birim")  # e.g., 'm³', 'kWh'
    period_start = models.DateField(verbose_name="Dönem Başlangıcı")
    period_end = models.DateField(verbose_name="Dönem Bitişi")
    location = models.CharField(max_length=100, blank=True, verbose_name="Lokasyon")  # e.g., 'ASANSÖR D2'
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
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name="Firma")
    report_date = models.DateField(verbose_name="Rapor Zaman Noktası")
    total_co2e = models.FloatField(verbose_name="Toplam CO2e (ton)")
    direct_ratio = models.FloatField(verbose_name="Doğrudan Emisyon Oranı (%)")
    indirect_ratio = models.FloatField(verbose_name="Dolaylı Emisyon Oranı (%)")
    json_details = models.JSONField(blank=True, null=True, verbose_name="Detaylı Hesaplamalar (JSON)")
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    generated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Oluşturan Kullanıcı")

    class Meta:
        verbose_name = "Karbon Raporu"
        verbose_name_plural = "Karbon Raporları"
        ordering = ['-report_date']
        permissions = [
            ("view_report_carbon", "Karbon Rapor Görüntüleme Hakkı"),
        ] 

    def __str__(self):
        return f"{self.firm.name} - Rapor ({self.report_date})"