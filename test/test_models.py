"""Test module > models.py"""

from dilemma.models import Player
from dilemma.strategies import always_cooperate
from dilemma.symbols import COOPERATE, DEFECT


class TestPlayerModel:
    """Test Player Model"""

    player_inst = Player("test_player")

    def test_player_instance_response(self):
        """test player instance and its response"""
        assert self.player_inst.name == "test_player"

        assert self.player_inst.action == DEFECT

        self.player_inst.respond(strategy=always_cooperate)

        assert self.player_inst.action == COOPERATE

    def test_player_pass(self):
        """test player instance and its response"""

        assert 1 + 1 == 2
