from django.db import models
from players.models import Player


class Miner(models.Model):
    name = models.CharField(verbose_name="Шахтер",
                            max_length=255,
                            default="miner")
    income = models.IntegerField(verbose_name="Доход")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Шахтер"
        verbose_name_plural = "Шахтеры"


class MinerLink(models.Model):
    owner = models.ForeignKey(Player,
                              on_delete=models.CASCADE,
                              verbose_name="Игрок")
    miner = models.ForeignKey(Miner,
                              on_delete=models.CASCADE,
                              verbose_name="Шахтер")
    mined_amount = models.IntegerField(default=0,
                                       verbose_name="Добыто")
