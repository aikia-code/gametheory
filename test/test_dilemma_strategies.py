"""Test all strategies"""

from dilemma.utils import (
    simulate,
)
from dilemma.strategies import (
    AlwaysCooperate,
    AlwaysDefect,
    Historian,
    TitForTat,
    TitFor2Tat,
    Unforgiving,
)


class TestDilemmaStrategies:
    """Test all available strategies in simulation"""

    def test_defect_and_cooperate_strategies(self):
        """test always defect and always cooperate strategies"""

        simulation = simulate(AlwaysCooperate([]), AlwaysCooperate([]), 50)
        assert simulation.get_total_score(1) == simulation.get_total_score(2) == 150

        simulation = simulate(AlwaysDefect([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == simulation.get_total_score(2) == 50

        simulation = simulate(AlwaysCooperate([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == 0
        assert simulation.get_total_score(2) == 250

    def test_tits_for_x_tats_strategies(self):
        """Test the tit for tats strategies with match ups"""

        simulation = simulate(TitFor2Tat([]), TitForTat([]), 50)
        assert simulation.get_total_score(2) == simulation.get_total_score(1) == 150
        assert simulation.get_mode_score(2) == simulation.get_mode_score(1) == 3

        simulation = simulate(TitFor2Tat([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == 48
        assert simulation.get_total_score(2) == 58
        assert simulation.get_mode_score(2) == simulation.get_mode_score(1) == 1

        simulation = simulate(TitForTat([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == 49
        assert simulation.get_total_score(2) == 54
        assert simulation.get_mode_score(2) == simulation.get_mode_score(1) == 1

    def test_historian_unforgiving_strategy(self):
        """Test the strategy with match ups"""

        simulation = simulate(Historian([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == 49
        assert simulation.get_total_score(2) == 54

        simulation = simulate(Unforgiving([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == 49
        assert simulation.get_total_score(2) == 54

        simulation = simulate(Unforgiving([]), Historian([]), 50)
        assert simulation.get_total_score(1) == simulation.get_total_score(2) == 150
