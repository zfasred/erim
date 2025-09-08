# carbon/management/commands/load_emission_factors.py

from django.core.management.base import BaseCommand
from carbon.models import EmissionFactor
from datetime import date
from decimal import Decimal

class Command(BaseCommand):
    help = 'Örnek emisyon faktörlerini yükle'
    
    def handle(self, *args, **options):
        # KAPSAM 1 - Sabit Yanma
        factors_kapsam1_sabit = [
            {'name': 'Doğalgaz', 'value': 56100, 'unit': 'kgCO2/TJ'},
            {'name': 'LPG', 'value': 63100, 'unit': 'kgCO2/TJ'},
            {'name': 'Fuel Oil', 'value': 77400, 'unit': 'kgCO2/TJ'},
            {'name': 'Kömür', 'value': 94600, 'unit': 'kgCO2/TJ'},
        ]
        
        for factor in factors_kapsam1_sabit:
            EmissionFactor.objects.get_or_create(
                name=factor['name'],
                category='KAPSAM_1',
                subcategory='sabit_yanma',
                defaults={
                    'value': factor['value'],
                    'unit': factor['unit'],
                    'valid_from': date(2024, 1, 1),
                    'source': 'IPCC 2006',
                    'is_active': True
                }
            )
        
        # KAPSAM 1 - Mobil Yanma
        factors_kapsam1_mobil = [
            {'name': 'Benzin', 'value': 69300, 'unit': 'kgCO2/TJ'},
            {'name': 'Motorin', 'value': 74100, 'unit': 'kgCO2/TJ'},
            {'name': 'Jet Yakıtı', 'value': 71500, 'unit': 'kgCO2/TJ'},
        ]
        
        for factor in factors_kapsam1_mobil:
            EmissionFactor.objects.get_or_create(
                name=factor['name'],
                category='KAPSAM_1',
                subcategory='mobil_yanma',
                defaults={
                    'value': factor['value'],
                    'unit': factor['unit'],
                    'valid_from': date(2024, 1, 1),
                    'source': 'IPCC 2006',
                    'is_active': True
                }
            )
        
        # KAPSAM 2 - Elektrik
        EmissionFactor.objects.get_or_create(
            name='Türkiye Elektrik Şebekesi',
            category='KAPSAM_2',
            subcategory='elektrik',
            defaults={
                'value': 0.442,
                'unit': 'tCO2/MWh',
                'valid_from': date(2024, 1, 1),
                'source': 'TEİAŞ 2024',
                'is_active': True
            }
        )
        
        # KAPSAM 4 - Hammaddeler
        factors_kapsam4 = [
            {'name': 'Çelik', 'value': 1.85, 'unit': 'kgCO2e/kg'},
            {'name': 'Alüminyum', 'value': 8.24, 'unit': 'kgCO2e/kg'},
            {'name': 'Bakır', 'value': 3.83, 'unit': 'kgCO2e/kg'},
            {'name': 'Plastik (PP)', 'value': 1.90, 'unit': 'kgCO2e/kg'},
            {'name': 'Kağıt', 'value': 0.95, 'unit': 'kgCO2e/kg'},
            {'name': 'Cam', 'value': 0.86, 'unit': 'kgCO2e/kg'},
        ]
        
        for factor in factors_kapsam4:
            EmissionFactor.objects.get_or_create(
                name=factor['name'],
                category='KAPSAM_4',
                subcategory='hammadde',
                defaults={
                    'value': factor['value'],
                    'unit': factor['unit'],
                    'valid_from': date(2024, 1, 1),
                    'source': 'Ecoinvent 3.8',
                    'is_active': True
                }
            )
        
        self.stdout.write(self.style.SUCCESS('✅ Emisyon faktörleri başarıyla yüklendi!'))