"""Test module > models.py"""

from dilemma.models import Player, Session
from dilemma.strategies import always_cooperate, always_defect
from dilemma.symbols import COOPERATE, DEFECT
from dilemma.symbols import TEMPT, SUCKER
from dilemma.utils import (
    get_strategy_name,
    simulate_strategies,
    update_statistics,
    summarize_statistics,
)


class TestDilemmaModels:
    """Test model scenarios"""

    player_inst = Player("test_player")
    session_inst = Session(names=("sand", "bite"))

    simulation = simulate_strategies(
        slot1=always_defect, slot2=always_cooperate, rounds=100000
    )

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
            slot1=always_defect, slot2=always_defect, rounds=10000
        )

        assert simulation.get_total_score(1) == 10000
        assert simulation.get_total_score(2) == 10000

        assert simulation.get_average_score(1) == 1
        assert simulation.get_average_score(2) == 1

        assert simulation.get_mode_score(1) == 1
        assert simulation.get_mode_score(2) == 1

    def test_simulation_utility_functions(self):
        """test simulation utility functions"""

        assert get_strategy_name(always_defect) == "Always Defect strategy"
        assert get_strategy_name(always_cooperate) == "Always Cooperate strategy"

        statistics1 = {"total": [], "average": [], "mode": []}
        statistics1 = update_statistics(statistics1, self.simulation, 1)
        statistics1 = summarize_statistics(statistics1)

        assert statistics1["total"] == 500000
        assert statistics1["average"] == 5
        assert statistics1["mode"] == 5
