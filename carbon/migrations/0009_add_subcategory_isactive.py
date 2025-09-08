from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('carbon', '0009_add_subcategory_isactive.py'),  # En son migration'ınızın adı
    ]

    operations = [
        migrations.AddField(
            model_name='emissionfactor',
            name='subcategory',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Alt Kategori'),
        ),
        migrations.AddField(
            model_name='emissionfactor',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Aktif'),
        ),
        migrations.AlterUniqueTogether(
            name='emissionfactor',
            unique_together={('name', 'category', 'subcategory', 'valid_from')},
        ),
    ]