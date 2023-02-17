from django.db import models
from players.models import Player


class Inventory(models.Model):
    owner = models.OneToOneField(Player, models.CASCADE)
    slots_amount = models.IntegerField(verbose_name="Количество слотов", default=25)

    def __str__(self):
        return f'Инвентарь пользователя: {self.owner.bot_id}'

    class Meta:
        verbose_name = "Инвентарь"
        verbose_name_plural = "Инвентари"


def create_inventory(sender, instance, created, **kwargs):
    if created:
        Inventory.objects.create(owner=instance)


models.signals.post_save.connect(receiver=create_inventory, sender=Player, weak=False, dispatch_uid='models.create_inventory')
