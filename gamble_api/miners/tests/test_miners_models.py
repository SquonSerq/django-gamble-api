import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


class TestMinersModel:
    def test_miner_model(self):
        miner_model = mixer.blend('miners.Miner')
        assert miner_model.pk == 1, "Should create Miner model"

    def test_miner_link_model(self):
        player_model = mixer.blend('players.Player')
        miner_model = mixer.blend('miners.Miner')
        miner_link_model = mixer.blend('miners.MinerLink',
                                       owner=player_model,
                                       miner=miner_model)

        assert miner_link_model.pk == 1, "Should create \
            miner link model with owner and miner as foreign keys."
