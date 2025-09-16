# carbon/management/commands/update_subscope_names.py

from django.core.management.base import BaseCommand
from carbon.models import SubScope

class Command(BaseCommand):
    help = 'SubScope isimlerini günceller'

    def handle(self, *args, **kwargs):
        subscope_names = {
            '1.1': 'Sabit Yanma',
            '1.2': 'Mobil Yanma',
            '1.3': 'Proses Emisyonları',
            '1.4': 'Kaçak Emisyonlar',
            '1.5': 'AFOLU',
            '2.1': 'Elektrik Tüketimi',
            '3.1': 'Satın Alınan Mal ve Hizmet Taşımacılığı',
            '3.2': 'Satılan Mal ve Hizmet Taşımacılığı',
            '3.3': 'Kiralanan Varlıklar',
            '3.4': 'İşe Gidiş Geliş',
            '3.5': 'İş Seyahatleri',
            '4.1': 'Satın Alınan Mal ve Hizmetler',
            '4.2': 'Sermaye Malları',
            '4.3': 'Atık'
        }

        updated_count = 0
        for code, name in subscope_names.items():
            updated = SubScope.objects.filter(code=code).update(name=name)
            if updated:
                updated_count += updated
                self.stdout.write(f'✓ {code} - {name} güncellendi')

        self.stdout.write(
            self.style.SUCCESS(f'\nToplam {updated_count} kayıt güncellendi!')
        )