"""Test module > models.py"""

from dilemma.models import Player, Session
from dilemma.strategies import AlwaysCooperate, AlwaysDefect
from dilemma.symbols import COOPERATE, DEFECT
from dilemma.symbols import TEMPT, SUCKER
from dilemma.utils import (
    simulate,
    summarize_statistics,
)


class TestDilemmaModels:
    """Test model scenarios"""

    player_inst = Player("test_player")

    session_inst = Session(names=["sand", "bite"])

    simulation = simulate(slot1=AlwaysDefect, slot2=AlwaysCooperate, rounds=10000)

    def test_player_response(self):
        """test player instance and its response on a strategy"""

        assert self.player_inst.name == "test_player"

        assert self.player_inst.action == DEFECT

        self.player_inst.respond(strategy=AlwaysCooperate(1, self.simulation.history))

        assert self.player_inst.action == COOPERATE

    def test_session_computation(self):
        """test to assert score computation"""

        assert self.session_inst.players[0].name == "sand"
        assert self.session_inst.players[1].name == "bite"

        self.session_inst.players[0].respond(
            strategy=AlwaysCooperate(1, self.simulation.history)
        )
        self.session_inst.players[1].respond(
            strategy=AlwaysDefect(0, self.simulation.history)
        )

        self.session_inst.compute_payoffs()

        assert self.session_inst.players[0].score == SUCKER[0]
        assert self.session_inst.players[1].score == TEMPT[0]

    def test_strategy_simulation(self):
        """test strategy simulation functions"""

        assert self.simulation.get_total_score(1) == 50000
        assert self.simulation.get_total_score(2) == 0

        assert self.simulation.get_average_score(1) == 5
        assert self.simulation.get_average_score(2) == 0

        assert self.simulation.get_mode_score(1) == 5
        assert self.simulation.get_mode_score(2) == 0

    def test_simulation_utility_functions(self):
        """test simulation utility functions"""

        summarize_statistics(AlwaysDefect)

        assert AlwaysDefect.statistics["total"] == 50000
        assert AlwaysDefect.statistics["average"] == 5
        assert AlwaysDefect.statistics["mode"] == 5

        summarize_statistics(AlwaysCooperate)

        assert AlwaysCooperate.statistics["total"] == 0
        assert AlwaysCooperate.statistics["average"] == 0
        assert AlwaysCooperate.statistics["mode"] == 0
