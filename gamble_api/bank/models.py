from django.db import models
from players.models import Player


class Bank(models.Model):
    owner = models.OneToOneField('players.Player',
                                 models.CASCADE,
                                 verbose_name="Игрок")
    gold_stored = models.IntegerField(default=0, verbose_name="Депозит")

    def __str__(self):
        return f'Банк пользователя: {self.owner.bot_id}'

    class Meta:
        verbose_name = "Банк"
        verbose_name_plural = "Банки"


def create_bank(sender, instance, created, **kwargs):
    if created:
        Bank.objects.create(owner=instance)


models.signals.post_save.connect(receiver=create_bank,
                                 sender=Player,
                                 weak=False,
                                 dispatch_uid='models.create_bank')
