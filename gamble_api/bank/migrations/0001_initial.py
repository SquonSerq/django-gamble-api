# Generated by Django 4.1.7 on 2023-02-17 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0002_player_bot_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gold_stored', models.IntegerField(default=0, verbose_name='Депозит')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player', verbose_name='Игрок')),
            ],
        ),
    ]