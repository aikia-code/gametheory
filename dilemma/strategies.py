r"""A collection of available strategies for simulation
"""
# utility imports
from random import choice

# standard simulation imports
from .symbols import COOPERATE, DEFECT
from .models import Strategy


# -----------------------------------------------------
# Strategy Collection


class AlwaysCooperate(Strategy):
    """Always Cooperate strategy

    Cooperates at every encounter
    """

    def __init__(self, opponent_index=0 | 1, session_history=None):
        super().__init__(opponent_index, session_history)
        self.strategy_name = "Always Cooperate"

    def run(self):
        return COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    def __init__(self, opponent_index=0 | 1, session_history=None):
        super().__init__(opponent_index, session_history)
        self.strategy_name = "Always Defect"

    def run(self):
        return DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    def __init__(self, opponent_index=0 | 1, session_history=None):
        super().__init__(opponent_index, session_history)
        self.strategy_name = "Random"

    def run(self):
        player_choices = [COOPERATE, DEFECT]

        return choice(player_choices)


class TitForTat(Strategy):
    """Tit for tat strategy"""

    def __init__(self, opponent_index=0 | 1, session_history=None):
        super().__init__(opponent_index, session_history)
        self.strategy_name = "Tit for Tat"

    def run(self):
        return (
            DEFECT
            if self.session_history[-1].players[self.opponent_index].action
            else COOPERATE
        )


# -----------------------------------------------------
# exports


always_cooperate = AlwaysCooperate()
always_defect = AlwaysDefect()
random_defect = RandomDefect()
