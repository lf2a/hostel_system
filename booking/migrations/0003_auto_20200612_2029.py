# Generated by Django 2.2.6 on 2020-06-12 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20200111_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bedroom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bedroom', to='bedroom.Bedroom', verbose_name='Bedroom'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Client'),
        ),
    ]
