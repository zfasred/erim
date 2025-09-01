from django.contrib.auth.models import User as AuthUser
from django.utils import timezone
import os
from django.conf import settings
from django.db import models


class Blood(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=15)

    class Meta:
        managed = False
        db_table = 'blood_'
        verbose_name = "Kan Grubu"
        verbose_name_plural = "Kan Grupları"

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'city_'
        verbose_name = "Şehir"
        verbose_name_plural = "Şehirler"

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    firm = models.ForeignKey('Firm', models.PROTECT, related_name='departments')
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_'
        verbose_name = "Birim"
        verbose_name_plural = "Birimler"

    def __str__(self):
        return f"{self.name} ({self.firm.name})"


class District(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'district_'
        verbose_name = "İlçe"
        verbose_name_plural = "İlçeler"

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Education(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=15)

    class Meta:
        managed = False
        db_table = 'education_'
        verbose_name = "Eğitim Durumu"
        verbose_name_plural = "Eğitim Durumları"

    def __str__(self):
        return f"{self.name}"


class Firm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, verbose_name="Firma Adı")
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Şehir")
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True, verbose_name="İlçe")
    tax_office = models.ForeignKey('TaxOffice', on_delete=models.PROTECT, blank=True, null=True, verbose_name="Vergi Daire")
    nace = models.ForeignKey('Nace', on_delete=models.PROTECT, blank=True, null=True, verbose_name="NACE kodu")
    create = models.DateField(db_column='create_', blank=True, null=True, verbose_name="Oluşturma Tarihi")
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True, verbose_name="Silinme Tarihi")
    address = models.CharField(db_column='address_', max_length=255, blank=True, null=True, verbose_name="Adres")
    telephone = models.CharField(db_column='telephone_', max_length=255, blank=True, null=True, verbose_name="Telefon")
    fax = models.CharField(db_column='fax_', max_length=255, blank=True, null=True, verbose_name="Faks")
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True, verbose_name="e-Posta")
    type_firm = models.CharField(max_length=255, blank=True, null=True, verbose_name="Firma Türü")
    tax = models.CharField(db_column='tax_', max_length=255, blank=True, null=True, verbose_name="Vergi Numara")
    web = models.CharField(db_column='web_', max_length=255, blank=True, null=True, verbose_name="İnternet Site")
    sgk_sicil = models.CharField(max_length=255, blank=True, null=True, verbose_name="SGK Sicil No")
    payment = models.CharField(db_column='payment_', max_length=255, blank=True, null=True, verbose_name="Ödeme Tipi")
    ceo_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili")
    ceo_email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili e-Posta")
    ceo_cell = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yetkili Telefon")
    #logo_media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Firma Logo")
    logo_media = models.FileField(upload_to='logo_firm/', blank=True, null=True, verbose_name="Firma Logosu")
    active = models.BooleanField(db_column='active_')

    def save(self, *args, **kwargs):
        # Eğer bu, veritabanında zaten var olan bir kayıt ise (yani güncelleme yapılıyorsa)
        if self.pk:
            try:
                # Veritabanındaki eski halini çek
                eski_kayit = Firm.objects.get(pk=self.pk)
                # Eğer eski kaydın logosu varSA ve yeni logo ile aynı DEĞİLSE
                if eski_kayit.logo_media and eski_kayit.logo_media != self.logo_media:
                    # Eski dosyanın yolunu al ve sil
                    eski_dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(eski_kayit.logo_media))
                    if os.path.isfile(eski_dosya_yolu):
                        os.remove(eski_dosya_yolu)
            except Firm.DoesNotExist:
                pass # Kayıt henüz veritabanında yok, bir şey yapma

        # Django'nun asıl save metodunu çalıştırarak kaydı tamamla
        super(Firm, self).save(*args, **kwargs)

    def delete_hard(self, *args, **kwargs):
        # Logo dosyasını diskten sil
        if self.logo_media:
            dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(self.logo_media))
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)
        # Django'nun orjinal, kalıcı silme metodunu çağır
        super(Firm, self).delete(*args, **kwargs)

    def delete_soft(self, *args, **kwargs):
        self.delete = timezone.now()
        self.save()

    class Meta:
        managed = False
        db_table = 'firm_'
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    short = models.CharField(db_column='short_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language_'
        verbose_name = "Dil"
        verbose_name_plural = "Diller"

    def __str__(self):
        return f"{self.name} ({self.short})"


class Media(models.Model):
    id = models.BigAutoField(primary_key=True)
    create = models.DateTimeField(db_column='create_', blank=True, null=True)
    media_type = models.ForeignKey('MediaType', models.PROTECT, blank=True, null=True)
    path = models.ForeignKey('Path', models.PROTECT, blank=True, null=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True)
    active = models.BooleanField(db_column='active_')

    class Meta:
        managed = False
        db_table = 'media_'
        verbose_name = "Medya"
        verbose_name_plural = "Medyalar"

    def __str__(self):
        path_name = self.path.name if self.path else 'Yol Yok'
        media_type_name = self.media_type.name if self.media_type else 'Tip Yok'
        return f"{self.name} ({path_name} {media_type_name})"


class MediaType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_type'
        verbose_name = "Medya Türü"
        verbose_name_plural = "Medya Türleri"

    def __str__(self):
        return f"{self.name}"


class Nace(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    code = models.CharField(db_column='code_', max_length=15)
    description = models.CharField(db_column='description_', max_length=511)

    class Meta:
        managed = False
        db_table = 'nace_'
        verbose_name = "NACE Kodu"
        verbose_name_plural = "NACE Kodları"

    def __str__(self):
        return f"{self.code} ({self.name})"


class Path(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)

    class Meta:
        managed = False
        db_table = 'path_'
        verbose_name = "Dizin Yolu"
        verbose_name_plural = "Dizin Yolları"

    def __str__(self):
        return f"{self.name}"


class Personnel(models.Model):

    GENDER_CHOICES = [
        (True, 'Erkek'),
        (False, 'Kadın'),
    ]
    MILITARY_CHOICES = [
        (True, 'Yaptı/Muaf'),
        (False, 'Yapmadı'),
    ]
    MARITAL_CHOICES = [
        (True, 'Evli'),
        (False, 'Bekar'),
    ]

    id = models.BigAutoField(primary_key=True)
    firm = models.ForeignKey(db_column='firm_id', to='Firm', on_delete=models.CASCADE, verbose_name="Firma")
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True, verbose_name="Ad")
    surname = models.CharField(db_column='surname_', max_length=255, blank=True, null=True, verbose_name="Soyad")
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True, verbose_name="TC Kimlik Numara")
    address = models.CharField(db_column='address_', max_length=255, blank=True, null=True, verbose_name="Adres")
    cell = models.CharField(db_column='cell_', max_length=15, blank=True, null=True, verbose_name="Telefon")
    birthday = models.DateTimeField(db_column='birthday_', blank=True, null=True, verbose_name="Doğum Tarihi")
    driving_license = models.CharField(max_length=15, blank=True, null=True, verbose_name="Sürücü Belge")
    status = models.CharField(db_column='status_', max_length=255, blank=True, null=True, verbose_name="Durum")
    education = models.ForeignKey(Education, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Eğitim")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Birim")
    children = models.IntegerField(db_column='children_', blank=True, null=True, verbose_name="Çocuk Sayısı")
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True, verbose_name="e-Posta")
    blood = models.ForeignKey(Blood, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Kan Grubu")
    military = models.BooleanField(db_column='military_', choices=MILITARY_CHOICES, default=True, verbose_name="Askerlik Durumu")
    gender = models.BooleanField(db_column='gender_', choices=GENDER_CHOICES, default=True, verbose_name="Cinsiyet")
    marital = models.BooleanField(db_column='marital_', choices=MARITAL_CHOICES, default=False, verbose_name="Medeni Durum")
    commencement = models.DateField(db_column='commencement_', blank=True, null=True, verbose_name="İşe Başlama Tarihi")
    termination = models.DateField(db_column='termination_', blank=True, null=True, verbose_name="İşten Ayrılma Tarihi")
    delete = models.DateTimeField(db_column='delete_', blank=True, null=True, verbose_name="Silinme Tarihi")
    picture = models.FileField(upload_to='picture_personnel/', blank=True, null=True, verbose_name="Personel Resmi", db_column='picture_')

    related_personnel = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        verbose_name="Önceki Kayıt",
        db_column='related_personnel_id'
    )

    class Meta:
        managed = False
        db_table = 'personnel_'
        verbose_name = "Personel"
        verbose_name_plural = "Personeller"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.tckno})"

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                eski_kayit = Personnel.objects.get(pk=self.pk)
                if eski_kayit.picture and eski_kayit.picture != self.picture:
                    eski_dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(eski_kayit.picture))
                    if os.path.isfile(eski_dosya_yolu):
                        os.remove(eski_dosya_yolu)
            except Personnel.DoesNotExist:
                pass
        super(Personnel, self).save(*args, **kwargs)

    def delete_soft(self):
        self.delete = timezone.now()
        self.save()

    def delete_hard(self, *args, **kwargs):
        if self.picture:
            dosya_yolu = os.path.join(settings.MEDIA_ROOT, str(self.picture))
            if os.path.isfile(dosya_yolu):
                os.remove(dosya_yolu)
        super(Personnel, self).delete(*args, **kwargs)


class TaxOffice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255)
    city = models.ForeignKey(City, models.PROTECT)
    district = models.ForeignKey(District, models.PROTECT)

    class Meta:
        managed = False
        db_table = 'tax_office'
        verbose_name = "Vergi Daire"
        verbose_name_plural = "Vergi Daireleri"

    def __str__(self):
        return f"{self.name} ({self.city.name} {self.district.name})"


class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    user_group = models.ForeignKey('UserGroup', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kullanıcı Grubu")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Dil")
    username = models.CharField(db_column='name_', max_length=255, blank=True, null=True, verbose_name="Rumuz (kullanıcı adı)")
    tckno = models.CharField(db_column='tckno_', max_length=11, blank=True, null=True, verbose_name="TC Kimlik No")
    certificate_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sertifika Numarası")
    title = models.CharField(db_column='title_', max_length=255, blank=True, null=True, verbose_name="Unvan")
    email = models.CharField(db_column='email_', max_length=255, blank=True, null=True, verbose_name="e-Posta")
    pasword = models.CharField(db_column='password_', max_length=32, blank=True, null=True, verbose_name="Parola")
    logo_media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kullanıcı Resmi", db_column='logo_media')
    picture = models.FileField(upload_to='picture_user/', blank=True, null=True, verbose_name="Kullanıcı Resmi")
    first_name = models.CharField(db_column='first_name', max_length=255, blank=True, null=True, verbose_name="Adı")
    last_name = models.CharField(db_column='last_name', max_length=255, blank=True, null=True, verbose_name="Soyadı")
    active = models.BooleanField(db_column='active_', default=True)
    is_staff = models.BooleanField('is_staff', default=True)
    is_superuser = models.BooleanField('is_superuser', default=False)

    class Meta:
        managed = False
        db_table = 'user_'
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        return f"{self.username} ({self.tckno})"


class UserFirm(models.Model):
    # Django'ya birincil anahtarın 'user_id' ve 'firm_id' birleşimi olduğunu söylüyoruz.
    #pk = models.CompositePrimaryKey('user_id', 'firm_id')

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.PROTECT, related_name='firm_associations')
    firm = models.ForeignKey(Firm, models.PROTECT, related_name='user_associations')
    create = models.DateTimeField(db_column='create_', auto_now_add=True)

    class Meta:
        # unique_together'a gerek yok, çünkü CompositePrimaryKey zaten bu işi yapıyor.
        unique_together = ('user', 'firm')
        managed = False
        db_table = 'user_firm'
        verbose_name = "Kullanıcı-Firma Ataması"
        verbose_name_plural = "Kullanıcı-Firma Atamaları"

    def __str__(self):
        # Bu __str__ metodu da doğru, olduğu gibi kalabilir.
        return f"{self.user.username} ({self.firm.name})"


class UserGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name_', max_length=255, blank=True, null=True)
    description = models.CharField(db_column='description_', max_length=511, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'
        verbose_name = "Kullanıcı Grubu"
        verbose_name_plural = "Kullanıcı Grupları"

    def __str__(self):
        return f"{self.name} ({self.description})"