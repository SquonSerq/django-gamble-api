import pytest
from mixer.backend.django import mixer
from bank.models import Bank

pytestmark = pytest.mark.django_db


class TestBankSignals:
    def test_bank_create_signal_from_player(self):
        mixer.blend('players.Player')
        bank_obj = Bank.objects.get(pk=1)
        assert bank_obj.pk == 1, "Should create bank object\
              when player model created."
