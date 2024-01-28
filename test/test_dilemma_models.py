"""Test module > models.py"""

from dilemma.models import Player, Session
from dilemma.strategies import always_cooperate, always_defect
from dilemma.symbols import COOPERATE, DEFECT
from dilemma.symbols import TEMPT, SUCKER
from dilemma.simulation import simulate_strategies
from dilemma.utils import get_strategy_name


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

    def test_session_computation(self):
        """test to assert score computation"""

        assert self.session_inst.players[0].name == "sand"

        assert self.session_inst.players[1].name == "bite"

        self.session_inst.players[0].respond(strategy=always_cooperate)

        self.session_inst.players[1].respond(strategy=always_defect)

        self.session_inst.compute_payoffs()

        assert self.session_inst.players[0].score == SUCKER[0]

        assert self.session_inst.players[1].score == TEMPT[0]

    def test_strategy_simulation(self):
        """test strategy simulation functions"""

        simulation = simulate_strategies(
            slot1=always_cooperate, slot2=always_defect, rounds=100
        )

        assert simulation.get_total_score(1) == 0

        assert simulation.get_total_score(2) == 500

        assert simulation.get_average_score(2) == 5

        assert simulation.get_mode_score(2) == 5

        assert get_strategy_name(always_defect) == "Always Defect strategy"
