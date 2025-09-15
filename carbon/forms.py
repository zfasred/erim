# carbon/forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import (
    GWPValues,
    DynamicCarbonInput, 
    SubScope,
    ExcelReport,
    CarbonCoefficient, CoefficientType, EmissionFactor, FuelType,
    InputCategory, InputData, Report
)
from core.models import User as CoreUser, Firm

class CarbonCoefficientForm(forms.ModelForm):
    """Karbon katsayıları için form"""
    
    class Meta:
        model = CarbonCoefficient
        fields = ['scope', 'subscope', 'coefficient_type', 'name', 'value', 
                 'unit', 'valid_from', 'valid_to', 'source', 'notes']
        widgets = {
            'valid_from': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'valid_to': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'value': forms.NumberInput(attrs={'step': '0.0000000001'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'scope': forms.Select(attrs={'id': 'id_scope_coefficient'}),
            'subscope': forms.Select(attrs={'id': 'id_subscope_coefficient'}),
        }
        labels = {
            'scope': 'Kapsam',
            'subscope': 'Alt Kapsam',
            'coefficient_type': 'Katsayı Türü',
            'name': 'İsim (Yakıt/Malzeme)',
            'value': 'Değer',
            'unit': 'Birim',
            'valid_from': 'Geçerlilik Başlangıcı',
            'valid_to': 'Geçerlilik Bitişi',
            'source': 'Kaynak',
            'notes': 'Notlar',
        }
        help_texts = {
            'name': 'Genel katsayılar için "Genel" yazın veya spesifik isim girin (ör: Doğalgaz, Otel, Çelik)',
            'valid_to': 'Boş bırakılırsa süresiz geçerli olur',
            'source': 'Katsayı kaynağı (ör: IPCC 2023, DEFRA 2024)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Tarih alanlarının input formatını ayarla
        self.fields['valid_from'].input_formats = ['%Y-%m-%d']
        self.fields['valid_to'].input_formats = ['%Y-%m-%d']
        
        # Alt kapsam seçeneklerini ayarla
        if self.data.get('scope'):
            # POST request'te scope var ise (form gönderilmiş)
            scope = self.data.get('scope')
            subscope_choices = [('', '-- Alt Kapsam Seçin --')]
            for code, label in CarbonCoefficient.SUBSCOPE_CHOICES:
                if code.startswith(scope + '.'):
                    subscope_choices.append((code, label))
            self.fields['subscope'].choices = subscope_choices
            
        elif self.instance and self.instance.pk:
            if self.instance.valid_from:
                self.initial['valid_from'] = self.instance.valid_from.strftime('%Y-%m-%d')
            if self.instance.valid_to:
                self.initial['valid_to'] = self.instance.valid_to.strftime('%Y-%m-%d')
            # Düzenleme modunda
            scope = self.instance.scope
            subscope_choices = []
            for code, label in CarbonCoefficient.SUBSCOPE_CHOICES:
                if code.startswith(scope + '.'):
                    subscope_choices.append((code, label))
            self.fields['subscope'].choices = subscope_choices
            
        else:
            # Yeni kayıt modunda ve GET request
            self.fields['subscope'].choices = [('', '-- Önce Kapsam Seçin --')]
        
        # Katsayı türü seçeneklerini ayarla (isteğe bağlı - daha iyi UX için)
        if self.data.get('subscope') or (self.instance and self.instance.subscope):
            subscope = self.data.get('subscope') if self.data.get('subscope') else self.instance.subscope
            
            coefficient_types_map = {
                '1.1': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_M3'],
                '1.2': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_TON_LT'],
                '1.3': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
                '1.4': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
                '1.5': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
                '2.1': ['EF_TCO2_MWH'],
                '3.1': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
                '3.2': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
                '3.3': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT'],
                '3.4': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_TON_LT'],
                '3.5': ['EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD', 'YOGUNLUK_KG_LT', 'YOGUNLUK_TON_LT', 'EF_KG_CO2E_ODA'],
                '4.1': ['EF_KG_CO2_KG'],
                '4.2': ['EF_KG_CO2_KG', 'EF_TCO2E_KG'],
                '4.3': ['EF_KG_CO2E_KWH', 'EF_KG_CO2E_M3', 'EF_KG_CO2_TON', 'EF_KG_CO2_M3', 'EF_CO2', 'EF_CH4', 'EF_N2O', 'NKD'],
            }
            
            if subscope in coefficient_types_map:
                allowed_types = coefficient_types_map[subscope]
                coefficient_choices = []
                for code, label in CarbonCoefficient.COEFFICIENT_TYPE_CHOICES:
                    if code in allowed_types:
                        coefficient_choices.append((code, label))
                self.fields['coefficient_type'].choices = coefficient_choices


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


class ReportForm(forms.Form):  # ModelForm değil, normal Form
    firm = forms.ModelChoiceField(
        queryset=Firm.objects.all(),
        label="Firma Seçin",
        required=True
    )
    report_date = forms.DateField(
        label="Rapor Tarihi",
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today,  # Varsayılan olarak bugün
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        # Kullanıcının erişebileceği firmaları filtrele
        if user and not user.is_superuser:
            if hasattr(user, 'user'):
                self.fields['firm'].queryset = Firm.objects.filter(
                    user_associations__user=user.user
                )
            else:
                self.fields['firm'].queryset = Firm.objects.filter(
                    user_associations__user=user
                )