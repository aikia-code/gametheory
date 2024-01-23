r"""A collection of available strategies for simulation
"""
# utility imports
from random import choice

# standard simulation imports
from .symbols import Action
from .models import Strategy


# -----------------------------------------------------
# collection


class AlwaysCooperate(Strategy):
    """Always Cooperate strategy

    Cooperates at every encounter
    """

    def run(self):
        return Action.COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    def run(self):
        return Action.DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    def run(self):
        player_choices = [Action.COOPERATE, Action.DEFECT]

        return choice(player_choices)


# -----------------------------------------------------
# exports

always_cooperate = AlwaysCooperate()
always_defect = AlwaysDefect()
random_defect = RandomDefect()
