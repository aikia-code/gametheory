"""Test Utilities"""

from dilemma.models import Session
from dilemma.utils import (
    simulate,
    summarize_statistics,
    update_statistics,
)


class TestDilemmaUtilities:
    """Test all available utility functions"""

    def test_simulation_summary_utility(self, strategy1, strategy2):
        """test simulation summary utility function"""

        new_simulation = simulate(slot1=strategy1, slot2=strategy2, rounds=100)

        cooperation_summary = summarize_statistics(strategy1)

        assert cooperation_summary["total"] == new_simulation.get_total_score(1) == 0
        assert (
            cooperation_summary["average"] == new_simulation.get_average_score(1) == 0
        )
        assert cooperation_summary["mode"] == new_simulation.get_mode_score(1) == 0

        defection_summary = summarize_statistics(strategy2)

        assert defection_summary["total"] == new_simulation.get_total_score(2) == 500
        assert defection_summary["average"] == new_simulation.get_average_score(2) == 5
        assert defection_summary["mode"] == new_simulation.get_mode_score(2) == 5

    def test_simulation_update_utility(self, strategy1, strategy2, simulation):
        """test the update utility"""

        for _ in range(10):
            session = Session(names=[strategy1.name, strategy2.name])

            strategy1 = strategy1.create(1, simulation.history)
            session.players[0].respond(strategy=strategy1)

            strategy2 = strategy2.create(0, simulation.history)
            session.players[1].respond(strategy=strategy2)

            session.compute_payoffs()

            simulation.history.append(session)

        statistics = update_statistics(strategy1, simulation, 1)
        assert statistics["total"] == [0]

        statistics = update_statistics(strategy2, simulation, 2)
        assert statistics["total"] == [50]
