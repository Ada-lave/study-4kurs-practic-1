# Generated by Django 5.1.5 on 2025-01-14 16:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adoption',
            options={'verbose_name': 'Устройство', 'verbose_name_plural': 'Устройства'},
        ),
        migrations.AlterModelOptions(
            name='cat',
            options={'verbose_name': 'Кот', 'verbose_name_plural': 'Коты'},
        ),
        migrations.AlterModelOptions(
            name='shelter',
            options={'verbose_name': 'Приют', 'verbose_name_plural': 'Приюты'},
        ),
        migrations.AlterField(
            model_name='cat',
            name='shelter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.shelter', verbose_name='Приют'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='capacity',
            field=models.IntegerField(verbose_name='Вместимость'),
        ),
    ]
