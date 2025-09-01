# carbon/management/commands/load_initial_carbon_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from carbon.models import CoefficientType, FuelType, EmissionFactor

class Command(BaseCommand):
    help = 'Karbon modülü için başlangıç verilerini yükler'

    def handle(self, *args, **kwargs):
        self.stdout.write('Başlangıç verileri yükleniyor...')
        
        # Katsayı Türleri
        coefficient_types = [
            {'name': 'EF_CO2', 'unit': 'kgCO2/TJ', 'description': 'CO2 Emisyon Faktörü'},
            {'name': 'EF_CH4', 'unit': 'kgCH4/TJ', 'description': 'CH4 Emisyon Faktörü'},
            {'name': 'EF_N2O', 'unit': 'kgN2O/TJ', 'description': 'N2O Emisyon Faktörü'},
            {'name': 'NCV', 'unit': 'TJ/Gg', 'description': 'Net Kalorifik Değer'},
            {'name': 'Grid_EF', 'unit': 'tCO2/MWh', 'description': 'Elektrik Grid Emisyon Faktörü'},
        ]
        
        for ct_data in coefficient_types:
            ct, created = CoefficientType.objects.get_or_create(
                name=ct_data['name'],
                defaults=ct_data
            )
            if created:
                self.stdout.write(f"Katsayı türü oluşturuldu: {ct.name}")
        
        # Yakıt Türleri (Excel'deki verilerden)
        fuel_types = [
            {
                'code': 'NG',
                'name': 'Doğalgaz',
                'category': 'gas',
                'ncv': 48.0,  # TJ/Gg
                'ef_co2': 56100,  # kgCO2/TJ
                'ef_ch4': 1,  # kgCH4/TJ
                'ef_n2o': 0.1,  # kgN2O/TJ
                'valid_from': date(2024, 1, 1),
                'source': 'IPCC 2006 Guidelines',
            },
            {
                'code': 'DIESEL',
                'name': 'Motorin',
                'category': 'liquid',
                'ncv': 43.0,  # TJ/Gg
                'ef_co2': 74100,  # kgCO2/TJ
                'ef_ch4': 3,  # kgCH4/TJ
                'ef_n2o': 0.6,  # kgN2O/TJ
                'valid_from': date(2024, 1, 1),
                'source': 'IPCC 2006 Guidelines',
            },
            {
                'code': 'GASOLINE',
                'name': 'Benzin',
                'category': 'liquid',
                'ncv': 44.3,  # TJ/Gg
                'ef_co2': 69300,  # kgCO2/TJ
                'ef_ch4': 3,  # kgCH4/TJ
                'ef_n2o': 0.6,  # kgN2O/TJ
                'valid_from': date(2024, 1, 1),
                'source': 'IPCC 2006 Guidelines',
            },
            {
                'code': 'COAL',
                'name': 'Kömür',
                'category': 'solid',
                'ncv': 25.8,  # TJ/Gg
                'ef_co2': 94600,  # kgCO2/TJ
                'ef_ch4': 1,  # kgCH4/TJ
                'ef_n2o': 1.5,  # kgN2O/TJ
                'valid_from': date(2024, 1, 1),
                'source': 'IPCC 2006 Guidelines',
            },
            {
                'code': 'LPG',
                'name': 'LPG',
                'category': 'liquid',
                'ncv': 47.3,  # TJ/Gg
                'ef_co2': 63100,  # kgCO2/TJ
                'ef_ch4': 1,  # kgCH4/TJ
                'ef_n2o': 0.1,  # kgN2O/TJ
                'valid_from': date(2024, 1, 1),
                'source': 'IPCC 2006 Guidelines',
            },
        ]
        
        for fuel_data in fuel_types:
            fuel, created = FuelType.objects.get_or_create(
                code=fuel_data['code'],
                defaults=fuel_data
            )
            if created:
                self.stdout.write(f"Yakıt türü oluşturuldu: {fuel.name}")
        
        # Kapsam 4 için Emisyon Faktörleri (Excel'deki ürünler)
        scope4_factors = [
            {'name': 'Silisli Sac', 'value': 1.85, 'unit': 'kgCO2e/kg'},
            {'name': 'Pik Döküm', 'value': 2.0, 'unit': 'kgCO2e/kg'},
            {'name': 'Sfero Karbon Verici', 'value': 1.9, 'unit': 'kgCO2e/kg'},
            {'name': 'Magnezyum', 'value': 8.5, 'unit': 'kgCO2e/kg'},
            {'name': 'Ferro Fosfor', 'value': 1.75, 'unit': 'kgCO2e/kg'},
            {'name': 'Ferro Krom', 'value': 2.1, 'unit': 'kgCO2e/kg'},
            {'name': 'Ferro Silisyum 75', 'value': 1.95, 'unit': 'kgCO2e/kg'},
            {'name': 'Rulman', 'value': 2.0, 'unit': 'kgCO2e/kg'},
            {'name': 'Takoz-Palet', 'value': 1.8, 'unit': 'kgCO2e/kg'},
            {'name': 'Klemens', 'value': 1.85, 'unit': 'kgCO2e/kg'},
            {'name': 'Çelik', 'value': 1.85, 'unit': 'kgCO2e/kg'},
            {'name': 'Alüminyum Külçe', 'value': 10.5, 'unit': 'kgCO2e/kg'},
            {'name': 'Hurda Metal', 'value': 0.2, 'unit': 'kgCO2e/kg'},
            {'name': 'Silisyum Karbür', 'value': 0.35, 'unit': 'kgCO2e/kg'},
            {'name': 'Maça Boyası', 'value': 2.5, 'unit': 'kgCO2e/kg'},
        ]
        
        # EF tipi al
        ef_type = CoefficientType.objects.filter(name='EF_CO2').first()
        
        for factor_data in scope4_factors:
            ef, created = EmissionFactor.objects.get_or_create(
                name=factor_data['name'],
                category='KAPSAM_4',
                defaults={
                    'type': ef_type,
                    'subcategory': '4.1',
                    'value': factor_data['value'],
                    'unit': factor_data['unit'],
                    'source': 'DEFRA/EPA',
                    'valid_from': date(2024, 1, 1),
                }
            )
            if created:
                self.stdout.write(f"Emisyon faktörü oluşturuldu: {ef.name}")
        
        # Elektrik Grid Emisyon Faktörü (Türkiye)
        grid_ef_type = CoefficientType.objects.filter(name='Grid_EF').first()
        grid_ef, created = EmissionFactor.objects.get_or_create(
            name='Türkiye Ulusal Grid',
            category='KAPSAM_2',
            defaults={
                'type': grid_ef_type or ef_type,
                'subcategory': '2.1',
                'value': 0.442,
                'unit': 'tCO2/MWh',
                'source': 'TEİAŞ 2024',
                'valid_from': date(2024, 1, 1),
            }
        )
        if created:
            self.stdout.write("Grid emisyon faktörü oluşturuldu")
        
        self.stdout.write(self.style.SUCCESS('Başlangıç verileri başarıyla yüklendi!'))