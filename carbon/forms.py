# carbon/forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import (
    CoefficientType, EmissionFactor, FuelType,
    Scope1Data, Scope2Data, Scope3Data, Scope4Data,
    InputCategory, InputData, Report
)
from core.models import User as CoreUser, Firm

# Mevcut formlarınız
class UserFirmAccessForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=CoreUser.objects.all().order_by('username'), 
        label="Kullanıcı Seçin"
    )
    firm = forms.ModelChoiceField(
        queryset=Firm.objects.all().order_by('name'), 
        label="Firma Seçin"
    )

class CoefficientTypeForm(forms.ModelForm):
    class Meta:
        model = CoefficientType
        fields = ['name', 'unit', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class EmissionFactorForm(forms.ModelForm):
    class Meta:
        model = EmissionFactor
        fields = ['type', 'name', 'category', 'subcategory', 'value', 'unit', 'source', 'valid_from', 'valid_to', 'notes']
        widgets = {
            'valid_from': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'valid_to': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        valid_from = cleaned_data.get('valid_from')
        valid_to = cleaned_data.get('valid_to')
        
        if valid_from and valid_to:
            if valid_to <= valid_from:
                raise ValidationError("Geçerlilik bitiş tarihi başlangıç tarihinden sonra olmalıdır.")
        
        return cleaned_data

# Yeni formlar
class FuelTypeForm(forms.ModelForm):
    class Meta:
        model = FuelType
        fields = ['code', 'name', 'category', 'ncv', 'ef_co2', 'ef_ch4', 'ef_n2o', 
                 'valid_from', 'valid_to', 'source', 'notes']
        widgets = {
            'valid_from': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'valid_to': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'ncv': 'Net Kalorifik Değer (TJ/Gg)',
            'ef_co2': 'CO2 Emisyon Faktörü (kgCO2/TJ)',
            'ef_ch4': 'CH4 Emisyon Faktörü (kgCH4/TJ)',
            'ef_n2o': 'N2O Emisyon Faktörü (kgN2O/TJ)',
        }

class Scope1DataForm(forms.ModelForm):
    class Meta:
        model = Scope1Data
        fields = ['combustion_type', 'location', 'fuel_type', 'consumption_value', 
                 'consumption_unit', 'period_year', 'period_month']
        widgets = {
            'period_year': forms.NumberInput(attrs={'min': 2020, 'max': 2050}),
            'period_month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
        }
        labels = {
            'location': 'Lokasyon/Tesis (ör: ASANSÖR D2, DÖKÜMHANE D3)',
            'consumption_value': 'Tüketim Değeri',
            'consumption_unit': 'Birim (ör: m³, lt, kg)',
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
        # Yakıt türlerini kategoriye göre grupla
        self.fields['fuel_type'].queryset = FuelType.objects.filter(
            valid_from__lte=date.today()
        ).filter(
            models.Q(valid_to__gte=date.today()) | models.Q(valid_to__isnull=True)
        ).order_by('category', 'name')
        
        # Varsayılan değerler
        if not self.instance.pk:
            self.fields['period_year'].initial = date.today().year
            self.fields['period_month'].initial = date.today().month
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.firm:
            instance.firm = self.firm
        if commit:
            instance.save()
        return instance

class Scope2DataForm(forms.ModelForm):
    class Meta:
        model = Scope2Data
        fields = ['location', 'electricity_kwh', 'grid_emission_factor', 
                 'period_year', 'period_month']
        widgets = {
            'period_year': forms.NumberInput(attrs={'min': 2020, 'max': 2050}),
            'period_month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'electricity_kwh': forms.NumberInput(attrs={'step': '0.01'}),
            'grid_emission_factor': forms.NumberInput(attrs={'step': '0.000001'}),
        }
        labels = {
            'location': 'Lokasyon/Tesis (ör: ASANSÖR D2, DÖKÜMHANE D3)',
            'electricity_kwh': 'Elektrik Tüketimi (kWh)',
            'grid_emission_factor': 'Grid Emisyon Faktörü (tCO2/MWh)',
        }
        help_texts = {
            'grid_emission_factor': 'Türkiye ortalaması: 0.442 tCO2/MWh',
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
        # Varsayılan değerler
        if not self.instance.pk:
            self.fields['period_year'].initial = date.today().year
            self.fields['period_month'].initial = date.today().month
            self.fields['grid_emission_factor'].initial = 0.442  # Türkiye ortalaması
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.firm:
            instance.firm = self.firm
        if commit:
            instance.save()
        return instance

class Scope3DataForm(forms.ModelForm):
    class Meta:
        model = Scope3Data
        fields = ['transport_type', 'transport_mode', 'vehicle_type', 'fuel_type',
                 'distance_km', 'fuel_consumption_lt', 'cargo_weight_ton',
                 'period_year', 'period_month', 'notes']
        widgets = {
            'period_year': forms.NumberInput(attrs={'min': 2020, 'max': 2050}),
            'period_month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'distance_km': forms.NumberInput(attrs={'step': '0.01'}),
            'fuel_consumption_lt': forms.NumberInput(attrs={'step': '0.001'}),
            'cargo_weight_ton': forms.NumberInput(attrs={'step': '0.001'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
        # Yakıt türlerini sadece liquid kategorisinden seç
        self.fields['fuel_type'].queryset = FuelType.objects.filter(
            category='liquid',
            valid_from__lte=date.today()
        ).filter(
            models.Q(valid_to__gte=date.today()) | models.Q(valid_to__isnull=True)
        )
        self.fields['fuel_type'].required = False
        
        # Varsayılan değerler
        if not self.instance.pk:
            self.fields['period_year'].initial = date.today().year
            self.fields['period_month'].initial = date.today().month
    
    def clean(self):
        cleaned_data = super().clean()
        distance = cleaned_data.get('distance_km')
        fuel_consumption = cleaned_data.get('fuel_consumption_lt')
        
        if not distance and not fuel_consumption:
            raise ValidationError("Mesafe veya yakıt tüketiminden en az biri girilmelidir.")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.firm:
            instance.firm = self.firm
        if commit:
            instance.save()
        return instance

class Scope4DataForm(forms.ModelForm):
    class Meta:
        model = Scope4Data
        fields = ['product_category', 'product_name', 'supplier', 'quantity', 'unit',
                 'emission_factor', 'emission_factor_source', 'period_year', 'period_month', 'notes']
        widgets = {
            'period_year': forms.NumberInput(attrs={'min': 2020, 'max': 2050}),
            'period_month': forms.NumberInput(attrs={'min': 1, 'max': 12}),
            'quantity': forms.NumberInput(attrs={'step': '0.001'}),
            'emission_factor': forms.NumberInput(attrs={'step': '0.000001'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'product_name': 'Ürün/Hizmet Adı',
            'supplier': 'Tedarikçi (opsiyonel)',
            'quantity': 'Miktar',
            'unit': 'Birim (kg, adet, m³, vb.)',
            'emission_factor': 'Emisyon Faktörü (kgCO2e/birim)',
            'emission_factor_source': 'EF Kaynağı (ör: DEFRA, EPA)',
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
        # Varsayılan değerler
        if not self.instance.pk:
            self.fields['period_year'].initial = date.today().year
            self.fields['period_month'].initial = date.today().month
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.firm:
            instance.firm = self.firm
        if commit:
            instance.save()
        return instance

# Toplu veri yükleme formu
class BulkUploadForm(forms.Form):
    SCOPE_CHOICES = [
        ('scope1', 'Kapsam 1 - Doğrudan Emisyonlar'),
        ('scope2', 'Kapsam 2 - Elektrik'),
        ('scope3', 'Kapsam 3 - Ulaşım'),
        ('scope4', 'Kapsam 4 - Satın Alınan Ürünler'),
    ]
    
    scope = forms.ChoiceField(choices=SCOPE_CHOICES, label="Kapsam Seçin")
    excel_file = forms.FileField(
        label="Excel Dosyası",
        help_text="Lütfen şablon formatında bir Excel dosyası yükleyin.",
        widget=forms.FileInput(attrs={'accept': '.xlsx,.xls'})
    )
    
    def clean_excel_file(self):
        file = self.cleaned_data['excel_file']
        if not file.name.endswith(('.xlsx', '.xls')):
            raise ValidationError("Sadece Excel dosyaları (.xlsx, .xls) kabul edilmektedir.")
        
        # Dosya boyutu kontrolü (10 MB)
        if file.size > 10 * 1024 * 1024:
            raise ValidationError("Dosya boyutu 10 MB'ı geçemez.")
        
        return file

# Rapor oluşturma formu
class ReportGenerateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_period_start', 'report_period_end']
        widgets = {
            'report_period_start': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'report_period_end': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        labels = {
            'report_period_start': 'Rapor Dönemi Başlangıç',
            'report_period_end': 'Rapor Dönemi Bitiş',
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
        # Varsayılan değerler - bu yılın başı ve bugün
        if not self.instance.pk:
            self.fields['report_period_start'].initial = date(date.today().year, 1, 1)
            self.fields['report_period_end'].initial = date.today()
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('report_period_start')
        end_date = cleaned_data.get('report_period_end')
        
        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError("Bitiş tarihi başlangıç tarihinden önce olamaz.")
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.report_date = date.today()
        if self.firm:
            instance.firm = self.firm
        if commit:
            instance.calculate_totals()  # Toplamları hesapla
            instance.save()
        return instance

# Mevcut formlarınız (backward compatibility için)
class InputCategoryForm(forms.ModelForm):
    class Meta:
        model = InputCategory
        fields = ['name', 'scope']

class InputDataForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['category', 'value', 'unit', 'period_start', 'period_end', 'location']
        widgets = {
            'period_start': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'period_end': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = InputCategory.objects.order_by('name')

class ReportForm(forms.Form):
    report_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="Rapor Zaman Noktası"
    )