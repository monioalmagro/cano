# Generated by Django 3.0.4 on 2020-06-05 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_fiambre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiambre',
            old_name='fraccionado',
            new_name='cien_gramos',
        ),
        migrations.RenameField(
            model_name='fiambre',
            old_name='masdecuatrounidades',
            new_name='cuarto_kilo',
        ),
        migrations.RemoveField(
            model_name='fiambre',
            name='porHorma',
        ),
    ]
