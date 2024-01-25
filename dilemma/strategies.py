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

    def run(self):
        return COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    def run(self):
        return DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    def run(self):
        player_choices = [COOPERATE, DEFECT]

        return choice(player_choices)


# -----------------------------------------------------
# exports

always_cooperate = AlwaysCooperate()
always_defect = AlwaysDefect()
random_defect = RandomDefect()
