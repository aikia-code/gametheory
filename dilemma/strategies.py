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

    name = "Always Cooperate"
    statistics: dict = {"total": [], "average": [], "mode": []}

    def run(self):
        return COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    name = "Always Defect"
    statistics: dict = {"total": [], "average": [], "mode": []}

    def run(self):
        return DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    name = "Random"
    statistics: dict = {"total": [], "average": [], "mode": []}

    def run(self):
        player_choices = [COOPERATE, DEFECT]

        return choice(player_choices)


class TitForTat(Strategy):
    """Tit for tat strategy"""

    name = "Tit for Tat"
    statistics: dict = {"total": [], "average": [], "mode": []}

    def run(self):
        try:
            if self.session_history[-1].players[self.opponent_index].action == DEFECT:
                return DEFECT
            return COOPERATE
        except IndexError:
            return COOPERATE
