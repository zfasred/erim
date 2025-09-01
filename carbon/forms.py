from django import forms
from .models import CoefficientType, EmissionFactor
from .models import InputCategory, InputData
from core.models import User as CoreUser, Firm

class UserFirmAccessForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CoreUser.objects.all().order_by('username'), label="Kullanıcı Seçin")
    firm = forms.ModelChoiceField(queryset=Firm.objects.all().order_by('name'), label="Firma Seçin")

class CoefficientTypeForm(forms.ModelForm):
    class Meta:
        model = CoefficientType
        fields = ['name', 'unit', 'description']

# carbon/forms.py

class EmissionFactorForm(forms.ModelForm):
    class Meta:
        model = EmissionFactor
        fields = ['type', 'name', 'category', 'value', 'source', 'valid_from', 'valid_to']
        widgets = {
            # Widget'a hem HTML tipi hem de render formatını söylüyoruz
            'valid_from': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'valid_to': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

class InputCategoryForm(forms.ModelForm):
    class Meta:
        model = InputCategory
        fields = ['name', 'scope']

class InputDataForm(forms.ModelForm):
    class Meta:
        model = InputData
        # Bu formda 'firm' alanı olmayacak, onu view içinde biz atayacağız.
        fields = ['category', 'value', 'unit', 'period_start', 'period_end', 'location']
        widgets = {
            'period_start': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'period_end': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Kategori seçim listesini isme göre sırala
        self.fields['category'].queryset = InputCategory.objects.order_by('name')

class ReportForm(forms.Form):
    report_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Rapor Zaman Noktası")
    # Additional fields if needed, e.g., scope selection