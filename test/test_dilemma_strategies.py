from dilemma.utils import (
    simulate,
    summarize_statistics,
)
from dilemma.strategies import (
    AlwaysCooperate,
    AlwaysDefect,
    TitForTat,
    Historian,
    TitFor2Tat,
)


class TestDilemmaStrategies:
    """Test all available strategies in simulation"""

    def test_defect_and_cooperate_strategies(self):
        """test always defect and always cooperate strategies"""

        simulation = simulate(AlwaysCooperate([]), AlwaysCooperate([]), 50)
        assert simulation.get_total_score(1) == simulation.get_total_score(2) == 150

        simulation = simulate(AlwaysDefect([]), AlwaysDefect([]), 50)
        assert simulation.get_total_score(1) == simulation.get_total_score(2) == 50
