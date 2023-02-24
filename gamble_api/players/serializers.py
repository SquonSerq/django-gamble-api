from bank.serializers import BankSerializer
from inventory.serializers import InventorySerializer
from rest_framework import serializers

from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    bank = BankSerializer(many=False, read_only=True)
    inventory = InventorySerializer(many=False, read_only=True)

    class Meta:
        model = Player
        fields = ["id", "bot_id", "gold", "bank", "inventory"]
