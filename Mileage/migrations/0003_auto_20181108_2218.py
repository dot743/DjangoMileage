# Generated by Django 2.1.3 on 2018-11-09 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mileage', '0002_auto_20181108_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mileage_entry',
            old_name='milesDriven',
            new_name='miles_driven',
        ),
    ]
