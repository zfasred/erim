# core/forms.py
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User as AuthUser
from .models import Firm, City, Personnel, Department, Education, Blood, User, UserGroup, Language, Media
from collections import OrderedDict


class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = [
            'name', 'city', 'district', 'tax_office', 'nace', 'create', 'address', 'telephone', 'fax', 'email', 'type_firm', 'tax', 'web', 'sgk_sicil', 'payment', 'ceo_name', 'ceo_email', 'ceo_cell', 'logo_media', 'active'
        ]
        widgets = {
            'create': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.order_by('name')

        instance = kwargs.get('instance')
        if instance and instance.delete:
            self.fields['delete'] = forms.DateTimeField(
                label="Silinme Tarihi ve Saati",
                initial=instance.delete,
                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
                required=False
            )


class FirmSoftDeleteForm(forms.Form):
    delete_date = forms.DateTimeField(
        initial=timezone.now,
        label="Silinme Tarihi ve Saati",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
    )


class PersonnelForm(forms.ModelForm):
    previous_tckno = forms.CharField(
        label="Önceki Kaydı Bul (TCKNO ile)",
        required=False,
        help_text="Eğer bu personel daha önce başka bir firmada kayıtlıysa, TCKNO'sunu buraya yazarak iki kaydı bağlayabilirsiniz."
    )

    class Meta:
        model = Personnel
        # Formdan 'delete' ve 'related_personnel' alanlarını hariç tutuyoruz
        fields = [
        'name', 'surname', 'tckno', 'address', 'cell', 'birthday', 'driving_license', 'status', 'education', 'department', 'children', 'email', 'blood', 'military', 'gender', 'firm', 'department', 'commencement', 'termination', 'marital', 'picture', 'related_personnel'
        ]
        exclude = ['delete']
        #exclude = ['delete', 'related_personnel']
        widgets = {
            # Tüm tarih alanları için takvim widget'ı
            'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'commencement': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'termination': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),

            # Cinsiyet ve Askerlik için radyo butonları
            'gender': forms.RadioSelect,
            'military': forms.RadioSelect,
            'marital': forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Seçim listelerini sırala
        self.fields['firm'].queryset = Firm.objects.filter(delete__isnull=True).order_by('name')
        self.fields['department'].queryset = Department.objects.order_by('name')
        self.fields['education'].queryset = Education.objects.order_by('id')
        self.fields['blood'].queryset = Blood.objects.order_by('id')

        instance = kwargs.get('instance')
        # Eğer bu yeni bir personel kaydı ise
        if not instance or not instance.pk:
            self.fields.pop('termination')

        # Eğer personel "soft delete" yapılmışsa
        if instance and instance.delete:
            self.fields['delete'] = forms.DateTimeField(
                label="Silinme Tarihi ve Saati",
                initial=instance.delete,
                widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
                required=False
            )

    # Form kaydedilirken TCKNO ile bulduğumuz personeli `related_personnel` alanına atayacağız.
    def save(self, commit=True):
        # ... (Bu metot aynı kalabilir) ...
        instance = super().save(commit=False)
        previous_tckno = self.cleaned_data.get('previous_tckno')
        if previous_tckno:
            try:
                previous_personnel = Personnel.objects.get(tckno=previous_tckno)
                instance.related_personnel = previous_personnel
            except Personnel.DoesNotExist:
                pass
        if commit:
            instance.save()
        return instance


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'firm']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Firma listesinde sadece aktif olanları gösterelim
        self.fields['firm'].queryset = Firm.objects.filter(delete__isnull=True).order_by('name')


class UserProfileForm(forms.ModelForm):
    # Django'nun standart auth.User modelinden gelen alanlar
    username = forms.CharField(label="Rumuz (kullanıcı adı)", required=True)
    email = forms.EmailField(label="E-Posta", required=False)
    password = forms.CharField(label="Şifre", widget=forms.PasswordInput, required=False, help_text="Yeni kullanıcı için veya şifre değiştirmek için doldurun. Değiştirmek istemiyorsanız boş bırakın.")

    class Meta:
        model = User # Bizim profil modelimiz
        # Profil modelimizden gelen alanlar
        fields = ['username', 'tckno', 'title', 'picture', 'user_group', 'language', 'active', 'first_name', 'last_name', 'is_staff']
        labels = {
            'username': 'Rumuz (kullanıcı adı)',
            'title': 'Unvan',
            'tckno': 'TC Kimlik No',
            'picture': 'Profil Resmi',
            'user_group': 'Kullanıcı Grubu',
            'language': 'Dil',
            'active': 'Aktif',
            'first_name': 'Adı',
            'last_name': 'Soyadı',
            'is_staff': 'Çalışan mı?',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eğer bu, var olan bir kullanıcıyı düzenleme formuysa (instance varsa)
        if self.instance and self.instance.pk and hasattr(self.instance, 'auth_user'):
            # Formdaki username ve email alanlarını, bağlı olduğu auth_user'dan gelen verilerle doldur
            self.fields['username'].initial = self.instance.auth_user.username
            self.fields['email'].initial = self.instance.auth_user.email

        self.fields['user_group'].queryset = UserGroup.objects.order_by('name')
        self.fields['language'].queryset = Language.objects.order_by('name')

        if not self.instance or not self.instance.pk:
            try:
                default_group = UserGroup.objects.get(name='Yönetici')
                self.fields['user_group'].initial = default_group
            except UserGroup.DoesNotExist:
                if UserGroup.objects.exists():
                    self.fields['user_group'].initial = UserGroup.objects.first()
            try:
                default_language = Language.objects.get(name='Türkçe')
                self.fields['language'].initial = default_language
            except Language.DoesNotExist:
                if Language.objects.exists():
                    self.fields['language'].initial = Language.objects.first()
        self.fields = OrderedDict([
            ('username', self.fields['username']),
            ('password', self.fields['password']),
            ('first_name', self.fields['first_name']),
            ('last_name', self.fields['last_name']),
            ('tckno', self.fields['tckno']),
            ('title', self.fields['title']),
            ('email', self.fields['email']),
            ('language', self.fields['language']),
            ('active', self.fields['active']),
            ('picture', self.fields['picture']),
            ('is_staff', self.fields['is_staff']),
            ('user_group', self.fields['user_group']),
        ])


'''
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # Modeldeki alanları listeliyoruz. 'logo_media' yerine 'picture' geldi.
        fields = [
            'name', 'tckno', 'certificate_number', 'title', 'email', 
            'user_group', 'language', 'picture', 'active'
        ]
        # Formda görünecek Türkçe etiketler
        labels = {
            'name': 'Ad Soyad',
            'tckno': 'TC Kimlik No',
            'certificate_number': 'Sertifika Numarası',
            'title': 'Unvan',
            'email': 'e-Posta Adresi',
            'user_group': 'Kullanıcı Grubu',
            'language': 'Dil',
            'picture': 'Kullanıcı Resmi',
            'active': 'Aktif',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_group'].queryset = UserGroup.objects.order_by('name')
        self.fields['language'].queryset = Language.objects.order_by('name')
'''