from django.core.management.base import BaseCommand
from decimal import Decimal
from carbon.models import FuelType, GWPValues, Scope1Excel, Scope2Excel, Scope4Excel, ExcelReport
from core.models import Firm

class Command(BaseCommand):
    help = 'Excel verilerini sisteme yükle'
    
    def handle(self, *args, **options):
        # 1. GWP değerlerini yükle
        self.stdout.write("GWP değerleri yükleniyor...")
        gwp, created = GWPValues.objects.get_or_create(
            id=1,
            defaults={
                'ch4_gwp': Decimal('27.9'),
                'n2o_gwp': Decimal('273'),
                'valid_from': '2024-01-01',
                'source': 'IPCC AR5'
            }
        )
        
        # 2. Yakıt türlerini yükle (Excel'deki değerlerle)
        self.stdout.write("Yakıt türleri yükleniyor...")
        
        # DOĞALGAZ
        FuelType.objects.get_or_create(
            name='Doğalgaz',
            defaults={
                'ef_co2': Decimal('56100'),
                'ef_ch4': Decimal('1'),
                'ef_n2o': Decimal('0.1'),
                'nkd': Decimal('48'),
                'density': Decimal('0.72'),
                'unit': 'm³'
            }
        )
        
        # MOTORİN
        FuelType.objects.get_or_create(
            name='Motorin',
            defaults={
                'ef_co2': Decimal('74100'),
                'ef_ch4': Decimal('3'),
                'ef_n2o': Decimal('0.6'),
                'nkd': Decimal('43'),
                'density': Decimal('0.835'),
                'unit': 'litre'
            }
        )
        
        # BENZİN
        FuelType.objects.get_or_create(
            name='Benzin',
            defaults={
                'ef_co2': Decimal('69300'),
                'ef_ch4': Decimal('3'),
                'ef_n2o': Decimal('0.6'),
                'nkd': Decimal('44.3'),
                'density': Decimal('0.745'),
                'unit': 'litre'
            }
        )
        
        # 3. Örnek verileri yükle (Excel'deki gibi)
        firm = Firm.objects.first()
        if not firm:
            self.stdout.write(self.style.ERROR("Firma bulunamadı! Önce firma oluşturun."))
            return
        
        self.stdout.write(f"'{firm.name}' firması için örnek veriler yükleniyor...")
        
        # KAPSAM 1 - Doğalgaz tüketimleri
        dogalgaz = FuelType.objects.get(name='Doğalgaz')
        
        # Excel'deki değerler
        kapsam1_veriler = [
            {'location': 'ASANSÖR D2', 'value': Decimal('1751988')},
            {'location': 'DÖKÜMHANE D3', 'value': Decimal('7118068')},
            {'location': 'FRENBU', 'value': Decimal('326622')},
        ]
        
        for veri in kapsam1_veriler:
            Scope1Excel.objects.update_or_create(
                firm=firm,
                location=veri['location'],
                year=2025,
                month=1,
                defaults={
                    'fuel_type': dogalgaz,
                    'consumption_value': veri['value'],
                }
            )
        
        # KAPSAM 2 - Elektrik tüketimleri
        kapsam2_veriler = [
            {'facility': 'ASANSÖR D2', 'kwh': Decimal('7955030')},
            {'facility': 'DÖKÜMHANE D3', 'kwh': Decimal('7118068')},
            {'facility': 'FRENBU', 'kwh': Decimal('753468')},
        ]
        
        for veri in kapsam2_veriler:
            Scope2Excel.objects.update_or_create(
                firm=firm,
                facility=veri['facility'],
                year=2025,
                month=1,
                defaults={
                    'electricity_kwh': veri['kwh'],
                    'emission_factor': Decimal('0.442'),
                }
            )
        
        # KAPSAM 4 - Satın alınan malzemeler
        kapsam4_veriler = [
            {'material': 'SİLİSLİ SAC', 'kg': Decimal('810000'), 'ef': Decimal('1.85')},
            {'material': 'PİK DÖKÜM', 'kg': Decimal('439000'), 'ef': Decimal('2.00')},
            {'material': 'Sfero Karbon Verici', 'kg': Decimal('138000'), 'ef': Decimal('1.90')},
            {'material': 'Magnezyum', 'kg': Decimal('2000'), 'ef': Decimal('8.50')},
            {'material': 'Ferro Fosfor', 'kg': Decimal('19000'), 'ef': Decimal('1.75')},
        ]
        
        for veri in kapsam4_veriler:
            Scope4Excel.objects.update_or_create(
                firm=firm,
                material_name=veri['material'],
                year=2025,
                month=1,
                defaults={
                    'quantity_kg': veri['kg'],
                    'emission_factor': veri['ef'],
                }
            )
        
        # 4. Rapor oluştur
        self.stdout.write("Rapor hesaplanıyor...")
        
        report, created = ExcelReport.objects.get_or_create(
            firm=firm,
            year=2025,
            month=1
        )
        
        # Toplamları hesapla
        report.calculate_totals()
        report.save()
        
        self.stdout.write(self.style.SUCCESS("\n✅ EXCEL VERİLERİ BAŞARIYLA YÜKLENDİ!"))
        self.stdout.write(f"\n📊 HESAPLAMA SONUÇLARI:")
        self.stdout.write(f"Kapsam 1: {report.scope1_total:.2f} tCO2e")
        self.stdout.write(f"Kapsam 2: {report.scope2_total:.2f} tCO2e")
        self.stdout.write(f"Kapsam 4: {report.scope4_total:.2f} tCO2e")
        self.stdout.write(f"{'='*40}")
        self.stdout.write(f"TOPLAM: {report.total_co2e:.2f} tCO2e")
        
        # Excel ile karşılaştırma
        self.stdout.write(f"\n📋 EXCEL İLE KARŞILAŞTIRMA:")
        self.stdout.write(f"Excel Kapsam 1: 18,049.12 tCO2e")
        self.stdout.write(f"Excel Kapsam 2: 6,995.34 tCO2e")
        self.stdout.write(f"Excel Kapsam 4: 15,354.70 tCO2e")
        self.stdout.write(f"Excel TOPLAM: 40,605.64 tCO2e")