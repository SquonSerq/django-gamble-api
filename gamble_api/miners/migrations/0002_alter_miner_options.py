# Generated by Django 4.1.7 on 2023-02-24 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miners', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miner',
            options={'verbose_name': 'Шахтер', 'verbose_name_plural': 'Шахтеры'},
        ),
    ]
