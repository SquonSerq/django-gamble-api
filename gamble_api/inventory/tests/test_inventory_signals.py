import pytest
from mixer.backend.django import mixer
from inventory.models import Inventory

pytestmark = pytest.mark.django_db


class TestInventorySignals:
    def test_inventory_create_signal_from_player(self):
        mixer.blend('players.Player')
        inventory_obj = Inventory.objects.get(pk=1)
        assert inventory_obj.pk == 1, "Should create inventory object\
              when player model created."
