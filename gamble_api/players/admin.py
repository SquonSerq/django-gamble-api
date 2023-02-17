from django.contrib import admin
from .models import Player
from inventory.models import Inventory
from miners.models import MinerLink
from bank.models import Bank


class InventoryInline(admin.TabularInline):
    model = Inventory


class BankInline(admin.TabularInline):
    model = Bank


class MinersInline(admin.TabularInline):
    model = MinerLink
    fields = ('miner', 'mined_amount')


class PlayerAdmin(admin.ModelAdmin):
    inlines = [
        InventoryInline,
        BankInline,
        MinersInline
    ]
    fields = (
        'bot_id',
        'gold',
    )


admin.site.register(Player, PlayerAdmin)
