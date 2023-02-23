import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestPlayersModel:
    def test_players_model(self):
        players_model = mixer.blend('players.Player')
        assert players_model.pk == 1, "Should create Player model"
