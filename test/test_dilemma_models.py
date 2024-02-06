"""Test module > models.py"""

from dilemma.symbols import COOPERATE, DEFECT
from dilemma.symbols import TEMPT, SUCKER
from dilemma.utils import (
    simulate,
)
from dilemma.strategies import (
    AlwaysCooperate,
    AlwaysDefect,
)


class TestDilemmaModels:
    """Test model scenarios"""

    simulation = simulate(slot1=AlwaysDefect([]), slot2=AlwaysCooperate([]), rounds=100)

    def test_player_response(self, player_inst):
        """test player instance and its response on a strategy"""

        assert player_inst.name == "test_player"

        assert player_inst.action == DEFECT

        player_inst.respond(strategy=AlwaysCooperate(self.simulation.history, 1))

        assert player_inst.action == COOPERATE

    def test_session_computation(self, session_inst):
        """test to assert score computation"""

        assert session_inst.players[0].name == "sand"
        assert session_inst.players[1].name == "bite"

        session_inst.players[0].respond(
            strategy=AlwaysCooperate(self.simulation.history, 1)
        )
        session_inst.players[1].respond(
            strategy=AlwaysDefect(self.simulation.history, 0)
        )

        session_inst.compute_payoffs()

        assert session_inst.players[0].score == SUCKER[0]
        assert session_inst.players[1].score == TEMPT[0]

    def test_strategy_simulation(self):
        """test strategy simulation functions"""

        assert self.simulation.get_total_score(1) == 500
        assert self.simulation.get_total_score(2) == 0

        assert self.simulation.get_average_score(1) == 5
        assert self.simulation.get_average_score(2) == 0

        assert self.simulation.get_mode_score(1) == 5
        assert self.simulation.get_mode_score(2) == 0
