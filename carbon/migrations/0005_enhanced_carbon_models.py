# carbon/migrations/0005_enhanced_carbon_models.py
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('carbon', '0004_alter_coefficienttype_options_and_more'),
        ('core', '0001_initial'),
    ]

    operations = [
        # FuelType modeli
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Yakıt Kodu')),
                ('name', models.CharField(max_length=100, verbose_name='Yakıt Adı')),
                ('category', models.CharField(choices=[('solid', 'Katı Yakıt'), ('liquid', 'Sıvı Yakıt'), ('gas', 'Gaz Yakıt')], max_length=20, verbose_name='Kategori')),
                ('ncv', models.DecimalField(decimal_places=6, max_digits=12, verbose_name='NKD (TJ/Gg)')),
                ('ef_co2', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='EF CO2 (kgCO2/TJ)')),
                ('ef_ch4', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='EF CH4 (kgCH4/TJ)')),
                ('ef_n2o', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='EF N2O (kgN2O/TJ)')),
                ('valid_from', models.DateField(verbose_name='Geçerlilik Başlangıcı')),
                ('valid_to', models.DateField(blank=True, null=True, verbose_name='Geçerlilik Bitişi')),
                ('source', models.CharField(blank=True, max_length=200, verbose_name='Kaynak')),
                ('notes', models.TextField(blank=True, verbose_name='Notlar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Yakıt Türü',
                'verbose_name_plural': 'Yakıt Türleri',
                'ordering': ['name'],
            },
        ),
        
        # Scope1Data modeli
        migrations.CreateModel(
            name='Scope1Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustion_type', models.CharField(choices=[('stationary', 'Sabit Yanma'), ('mobile', 'Mobil Yanma')], max_length=20, verbose_name='Yanma Türü')),
                ('location', models.CharField(max_length=100, verbose_name='Lokasyon/Tesis')),
                ('consumption_value', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Tüketim Değeri')),
                ('consumption_unit', models.CharField(default='m³', max_length=20, verbose_name='Birim')),
                ('period_year', models.IntegerField(verbose_name='Yıl')),
                ('period_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Ay')),
                ('co2_emission', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='CO2 Emisyonu (ton)')),
                ('ch4_emission', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='CH4 Emisyonu (ton)')),
                ('n2o_emission', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='N2O Emisyonu (ton)')),
                ('total_co2e', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='Toplam CO2e (ton)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user', verbose_name='Oluşturan')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.firm', verbose_name='Firma')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carbon.fueltype', verbose_name='Yakıt Türü')),
            ],
            options={
                'verbose_name': 'Kapsam 1 Verisi',
                'verbose_name_plural': 'Kapsam 1 Verileri',
                'ordering': ['-period_year', '-period_month', 'location'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='scope1data',
            unique_together={('firm', 'location', 'fuel_type', 'period_year', 'period_month')},
        ),
        
        # Scope2Data modeli
        migrations.CreateModel(
            name='Scope2Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, verbose_name='Lokasyon/Tesis')),
                ('electricity_kwh', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Elektrik Tüketimi (kWh)')),
                ('grid_emission_factor', models.DecimalField(decimal_places=6, default=0.442, max_digits=10, verbose_name='Grid Emisyon Faktörü (tCO2/MWh)')),
                ('period_year', models.IntegerField(verbose_name='Yıl')),
                ('period_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Ay')),
                ('total_co2e', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='Toplam CO2e (ton)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user', verbose_name='Oluşturan')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.firm', verbose_name='Firma')),
            ],
            options={
                'verbose_name': 'Kapsam 2 Verisi',
                'verbose_name_plural': 'Kapsam 2 Verileri',
                'ordering': ['-period_year', '-period_month', 'location'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='scope2data',
            unique_together={('firm', 'location', 'period_year', 'period_month')},
        ),
        
        # Scope3Data modeli
        migrations.CreateModel(
            name='Scope3Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.CharField(choices=[('upstream', 'Tedarik Zinciri Nakliyesi'), ('downstream', 'Dağıtım Nakliyesi'), ('employee', 'Çalışan Ulaşımı'), ('business', 'İş Seyahatleri')], max_length=20, verbose_name='Nakliye Türü')),
                ('transport_mode', models.CharField(choices=[('road', 'Karayolu'), ('rail', 'Demiryolu'), ('air', 'Havayolu'), ('sea', 'Denizyolu')], max_length=20, verbose_name='Ulaşım Şekli')),
                ('vehicle_type', models.CharField(blank=True, max_length=100, verbose_name='Araç Tipi')),
                ('distance_km', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Mesafe (km)')),
                ('fuel_consumption_lt', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Yakıt Tüketimi (lt)')),
                ('cargo_weight_ton', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Yük Ağırlığı (ton)')),
                ('period_year', models.IntegerField(verbose_name='Yıl')),
                ('period_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Ay')),
                ('total_co2e', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='Toplam CO2e (ton)')),
                ('notes', models.TextField(blank=True, verbose_name='Notlar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user', verbose_name='Oluşturan')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.firm', verbose_name='Firma')),
                ('fuel_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='carbon.fueltype', verbose_name='Yakıt Türü')),
            ],
            options={
                'verbose_name': 'Kapsam 3 Verisi',
                'verbose_name_plural': 'Kapsam 3 Verileri',
                'ordering': ['-period_year', '-period_month', 'transport_type'],
            },
        ),
        
        # Scope4Data modeli
        migrations.CreateModel(
            name='Scope4Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('raw_material', 'Hammadde'), ('semi_finished', 'Yarı Mamul'), ('service', 'Hizmet'), ('capital_good', 'Sermaye Malı'), ('consumable', 'Sarf Malzemesi'), ('waste', 'Atık Yönetimi')], max_length=20, verbose_name='Ürün Kategorisi')),
                ('product_name', models.CharField(max_length=200, verbose_name='Ürün/Hizmet Adı')),
                ('supplier', models.CharField(blank=True, max_length=200, verbose_name='Tedarikçi')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=15, verbose_name='Miktar')),
                ('unit', models.CharField(max_length=20, verbose_name='Birim')),
                ('emission_factor', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Emisyon Faktörü (kgCO2e/birim)')),
                ('emission_factor_source', models.CharField(blank=True, max_length=200, verbose_name='EF Kaynağı')),
                ('period_year', models.IntegerField(verbose_name='Yıl')),
                ('period_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Ay')),
                ('total_co2e', models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True, verbose_name='Toplam CO2e (ton)')),
                ('notes', models.TextField(blank=True, verbose_name='Notlar')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.user', verbose_name='Oluşturan')),
                ('firm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.firm', verbose_name='Firma')),
            ],
            options={
                'verbose_name': 'Kapsam 4 Verisi',
                'verbose_name_plural': 'Kapsam 4 Verileri',
                'ordering': ['-period_year', '-period_month', 'product_category', 'product_name'],
            },
        ),
        
        # EmissionFactor modelini güncelle
        migrations.AddField(
            model_name='emissionfactor',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('1.1', 'Sabit Yanma'), ('1.2', 'Mobil Yanma'), ('1.3', 'Proses Emisyonları'), ('1.4', 'Kaçak Emisyonlar'), ('1.5', 'LULUCF'), ('2.1', 'Elektrik'), ('2.2', 'Isıtma/Soğutma'), ('2.3', 'Buhar'), ('3.1', 'Upstream Nakliye'), ('3.2', 'Downstream Nakliye'), ('3.3', 'Çalışan Ulaşımı'), ('3.4', 'İş Seyahatleri'), ('4.1', 'Satın Alınan Ürünler'), ('4.2', 'Sermaye Malları'), ('4.3', 'Atık Yönetimi'), ('4.4', 'Kiralık Varlıklar')], max_length=10, verbose_name='Alt Kategori'),
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='unit',
            field=models.CharField(default='kgCO2e', max_length=50, verbose_name='Birim'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notlar'),
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        
        # Report modelini güncelle
        migrations.AddField(
            model_name='report',
            name='scope1_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 1 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='scope2_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 2 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='scope3_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 3 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='scope4_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 4 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='scope5_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 5 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='scope6_total',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=15, verbose_name='Kapsam 6 Toplam (tCO2e)'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_period_start',
            field=models.DateField(null=True, verbose_name='Rapor Dönemi Başlangıç'),
        ),
        migrations.AddField(
            model_name='report',
            name='report_period_end',
            field=models.DateField(null=True, verbose_name='Rapor Dönemi Bitiş'),
        ),
    ]