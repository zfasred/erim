# Management Command: python manage.py load_carbon_data
# carbon/management/commands/load_carbon_data.py
from django.core.management.base import BaseCommand
from carbon.services import ExcelDataLoader, CarbonCalculationService
from core.models import Firm


class Command(BaseCommand):
    help = 'Excel verilerini yükle ve karbon hesaplamalarını yap'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--firm_id',
            type=int,
            default=1,
            help='Firma ID'
        )
        parser.add_argument(
            '--year',
            type=int,
            default=2025,
            help='Hesaplama yılı'
        )
        parser.add_argument(
            '--month',
            type=int,
            default=1,
            help='Hesaplama ayı'
        )
    
    def handle(self, *args, **options):
        # Emisyon faktörlerini yükle
        self.stdout.write("📊 Emisyon faktörleri yükleniyor...")
        ExcelDataLoader.load_emission_factors()
        
        # Firma seç
        firm_id = options['firm_id']
        firm = Firm.objects.get(pk=firm_id)
        
        # Hesaplama servisi oluştur
        calculator = CarbonCalculationService(
            firm=firm,
            year=options['year'],
            month=options['month']
        )
        
        # Örnek verileri yükle
        self.stdout.write(f"📝 {firm.name} için örnek veriler yükleniyor...")
        calculator.load_example_data()
        
        # Rapor oluştur
        self.stdout.write("🔄 Karbon hesaplamaları yapılıyor...")
        report = calculator.create_report()
        
        # Sonuçları göster
        self.stdout.write(self.style.SUCCESS("\n✅ HESAPLAMA TAMAMLANDI!"))
        self.stdout.write(f"\n📊 ÖZET RAPOR - {firm.name}")
        self.stdout.write("=" * 50)
        self.stdout.write(f"Kapsam 1: {report.scope1_total:.2f} tCO2e")
        self.stdout.write(f"Kapsam 2: {report.scope2_total:.2f} tCO2e")
        self.stdout.write(f"Kapsam 3: {report.scope3_total:.2f} tCO2e")
        self.stdout.write(f"Kapsam 4: {report.scope4_total:.2f} tCO2e")
        self.stdout.write("=" * 50)
        self.stdout.write(f"TOPLAM: {report.total_co2e:.2f} tCO2e")
        
        # Ürün dağılımını göster
        self.stdout.write("\n📦 ÜRÜN BAZLI DAĞILIM")
        self.stdout.write("=" * 50)
        
        allocations = report.product_allocations.all()
        for allocation in allocations:
            self.stdout.write(
                f"{allocation.product_name}: "
                f"{allocation.co2e_per_unit:.6f} tCO2e/adet"
            )