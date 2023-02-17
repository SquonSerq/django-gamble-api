from django.db import models


class Player(models.Model):
    bot_id = models.CharField(verbose_name="ID в боте", max_length=150, default="")
    gold = models.IntegerField(verbose_name="Золото", default=1000)

    def __str__(self):
        return self.bot_id
