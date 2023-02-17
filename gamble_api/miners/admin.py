from django.contrib import admin
from .models import Miner, MinerLink


class MinerLinkInline(admin.TabularInline):
    model = MinerLink
    fields = ('owner', 'mined_amount')


class MinerAdmin(admin.ModelAdmin):
    inlines = [
        MinerLinkInline
    ]


admin.site.register(Miner, MinerAdmin)
