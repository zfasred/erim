# carbon/forms.py
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import (
    DynamicCarbonInput, 
    SubScope,
    ExcelReport,
    CarbonCoefficient,
    GWPValues,
    FuelType
)
from core.models import User as CoreUser, Firm


class DynamicCarbonInputForm(forms.ModelForm):
    """Dinamik karbon veri girişi formu"""
    
    class Meta:
        model = DynamicCarbonInput
        fields = ['firm', 'datetime', 'scope', 'subscope', 'data']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'firm': 'Firma',
            'datetime': 'Tarih/Saat',
            'scope': 'Kapsam',
            'subscope': 'Alt Kapsam',
            'data': 'Veri (JSON)',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Alt kapsam seçeneklerini scope'a göre filtrele
        if self.data.get('scope'):
            scope = self.data.get('scope')
            self.fields['subscope'].queryset = SubScope.objects.filter(scope=scope)
        elif self.instance.pk:
            self.fields['subscope'].queryset = SubScope.objects.filter(scope=self.instance.scope)
    
    def clean_data(self):
        """JSON veriyi doğrula"""
        import json
        data = self.cleaned_data.get('data')
        
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise ValidationError("Geçersiz JSON formatı")
        
        return data


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
            scope = self.data.get('scope')
            subscope_choices = [('', '-- Alt Kapsam Seçin --')]
            for code, label in CarbonCoefficient.SUBSCOPE_CHOICES:
                if code.startswith(scope + '.'):
                    subscope_choices.append((code, label))
            self.fields['subscope'].choices = subscope_choices
        elif self.instance.pk:
            scope = self.instance.scope
            subscope_choices = [('', '-- Alt Kapsam Seçin --')]
            for code, label in CarbonCoefficient.SUBSCOPE_CHOICES:
                if code.startswith(scope + '.'):
                    subscope_choices.append((code, label))
            self.fields['subscope'].choices = subscope_choices


class UserFirmAccessForm(forms.Form):
    """Kullanıcı-Firma ilişkisi formu"""
    user = forms.ModelChoiceField(
        queryset=CoreUser.objects.all(),
        label="Kullanıcı Seçin",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    firm = forms.ModelChoiceField(
        queryset=Firm.objects.all(),
        label="Firma Seçin",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class ReportGenerateForm(forms.Form):
    """Rapor oluşturma formu"""
    firm = forms.ModelChoiceField(
        queryset=Firm.objects.all(),
        label="Firma",
        required=True
    )
    start_date = forms.DateField(
        label="Başlangıç Tarihi",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    end_date = forms.DateField(
        label="Bitiş Tarihi", 
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError("Başlangıç tarihi bitiş tarihinden sonra olamaz.")
        
        return cleaned_data


class BulkUploadForm(forms.Form):
    """Toplu veri yükleme formu"""
    SCOPE_CHOICES = [
        ('1', 'Kapsam 1 - Doğrudan Emisyonlar'),
        ('2', 'Kapsam 2 - Elektrik'),
        ('3', 'Kapsam 3 - Ulaşım'),
        ('4', 'Kapsam 4 - Satın Alınan Ürünler'),
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


class ExcelReportForm(forms.ModelForm):
    """Excel raporu oluşturma formu"""
    
    class Meta:
        model = ExcelReport
        fields = ['firm', 'year', 'month', 'notes']
        widgets = {
            'month': forms.Select(choices=[(i, i) for i in range(1, 13)]),
            'year': forms.NumberInput(attrs={'min': 2020, 'max': 2050}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'firm': 'Firma',
            'year': 'Yıl',
            'month': 'Ay (Boş bırakılırsa yıllık rapor)',
            'notes': 'Notlar',
        }


class FuelTypeForm(forms.ModelForm):
    """Yakıt türü formu"""
    
    class Meta:
        model = FuelType
        fields = ['code', 'name', 'category', 'ncv', 'ef_co2', 'ef_ch4', 'ef_n2o', 
                 'density', 'unit', 'valid_from', 'valid_to', 'source', 'notes']
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


class GWPValuesForm(forms.ModelForm):
    """GWP değerleri formu"""
    
    class Meta:
        model = GWPValues
        fields = ['ch4_gwp', 'n2o_gwp', 'valid_from', 'source']
        widgets = {
            'valid_from': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }


class ReportForm(forms.Form):
    """Eski rapor formu - backward compatibility"""
    firm = forms.ModelChoiceField(
        queryset=Firm.objects.all(),
        label="Firma Seçin",
        required=True
    )
    report_date = forms.DateField(
        label="Rapor Tarihi",
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today,
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and not user.is_superuser:
            if hasattr(user, 'user'):
                self.fields['firm'].queryset = Firm.objects.filter(
                    user_associations__user=user.user
                )
            else:
                self.fields['firm'].queryset = Firm.objects.filter(
                    user_associations__user=user
                )