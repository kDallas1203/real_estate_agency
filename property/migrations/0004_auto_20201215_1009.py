# Generated by Django 2.2.4 on 2020-12-15 07:09
from django.db import migrations


def fill_new_building(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        flat.new_building = flat.construction_year >= 2015
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building)
    ]
