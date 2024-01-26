"""Test module > models.py"""

from dilemma.models import Player, Session
from dilemma.strategies import always_cooperate, always_defect
from dilemma.symbols import COOPERATE, DEFECT
from dilemma.symbols import TEMPT, REWARD, SUCKER, PUNISH


class TestDilemmaModels:
    """Test model scenarios"""

    player_inst = Player("test_player")
    session_inst = Session(names=("sand", "bite"))

    def test_player_response(self):
        """test player instance and its response on a strategy"""
        assert self.player_inst.name == "test_player"

        assert self.player_inst.action == DEFECT

        self.player_inst.respond(strategy=always_cooperate)

        assert self.player_inst.action == COOPERATE

    def test_session_score_compute(self):
        """test to assert score computation"""

        assert self.session_inst.players[0].name == "sand"

        assert self.session_inst.players[1].name == "bite"

        self.session_inst.players[0].respond(strategy=always_cooperate)

        self.session_inst.players[1].respond(strategy=always_defect)

        self.session_inst.compute_payoffs()

        assert self.session_inst.players[0].score == SUCKER[0]

        assert self.session_inst.players[1].score == TEMPT[0]
