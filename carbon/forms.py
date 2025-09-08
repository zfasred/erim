# carbon/forms.py - Düzeltilmiş
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from decimal import Decimal
from .models import (
    CoefficientType, EmissionFactor, FuelType,
    Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport,
    InputCategory, InputData, Report
)
from core.models import User as CoreUser, Firm

# Excel model formları
class Scope1ExcelForm(forms.ModelForm):
    class Meta:
        model = Scope1Excel
        fields = ['location', 'fuel_type', 'consumption_value', 'year', 'month']
        widgets = {
            'consumption_value': forms.NumberInput(attrs={'step': '0.01'}),
            'year': forms.NumberInput(attrs={'min': '2020', 'max': '2030'}),
            'month': forms.NumberInput(attrs={'min': '1', 'max': '12'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        if self.firm and not self.instance.pk:
            self.instance.firm = self.firm

class Scope2ExcelForm(forms.ModelForm):
    class Meta:
        model = Scope2Excel
        fields = ['facility', 'electricity_kwh', 'year', 'month']
        widgets = {
            'electricity_kwh': forms.NumberInput(attrs={'step': '0.01'}),
            'year': forms.NumberInput(attrs={'min': '2020', 'max': '2030'}),
            'month': forms.NumberInput(attrs={'min': '1', 'max': '12'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        if self.firm and not self.instance.pk:
            self.instance.firm = self.firm

class Scope4ExcelForm(forms.ModelForm):
    class Meta:
        model = Scope4Excel
        fields = ['material_name', 'quantity_kg', 'emission_factor', 'year', 'month']
        widgets = {
            'quantity_kg': forms.NumberInput(attrs={'step': '0.01'}),
            'emission_factor': forms.NumberInput(attrs={'step': '0.000001'}),
            'year': forms.NumberInput(attrs={'min': '2020', 'max': '2030'}),
            'month': forms.NumberInput(attrs={'min': '1', 'max': '12'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        if self.firm and not self.instance.pk:
            self.instance.firm = self.firm

# Diğer formlar
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

class FuelTypeForm(forms.ModelForm):
    class Meta:
        model = FuelType
        fields = '__all__'
        exclude = ['created_at', 'updated_at']
        widgets = {
            'valid_from': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'valid_to': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

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

class ReportGenerateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_period_start', 'report_period_end']
        widgets = {
            'report_period_start': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'report_period_end': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        self.firm = kwargs.pop('firm', None)
        super().__init__(*args, **kwargs)
        
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

class BulkUploadForm(forms.Form):
    scope = forms.ChoiceField(
        choices=[
            ('scope1', 'Kapsam 1'),
            ('scope2', 'Kapsam 2'),
            ('scope4', 'Kapsam 4'),
        ],
        label="Veri Tipi"
    )
    excel_file = forms.FileField(
        label="Excel Dosyası",
        help_text="Lütfen şablon formatında Excel dosyası yükleyin",
        widget=forms.FileInput(attrs={'accept': '.xlsx,.xls'})
    )
    
    def clean_excel_file(self):
        file = self.cleaned_data['excel_file']
        if not file.name.endswith(('.xlsx', '.xls')):
            raise ValidationError("Sadece Excel dosyaları (.xlsx, .xls) kabul edilmektedir.")
        
        if file.size > 10 * 1024 * 1024:
            raise ValidationError("Dosya boyutu 10 MB'ı geçemez.")
        
        return file

# Dummy formlar - Geçici olarak eski kodların çalışması için
# İleride kaldırılabilir
class Scope1DataForm(Scope1ExcelForm):
    pass

class Scope2DataForm(Scope2ExcelForm):
    pass

class Scope3DataForm(forms.Form):
    pass

class Scope4DataForm(Scope4ExcelForm):
    pass