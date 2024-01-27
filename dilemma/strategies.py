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
# helper


def get_strategy_name(strategy=None):
    """return the name of the strategy

    Args:
        strategy (strategy): strategy object

    Returns:
        str: name of strategy
    """
    if strategy is None:
        raise ValueError("A strategy needs to be specified")

    return strategy.__doc__.split(sep="\n")[0]


# -----------------------------------------------------
# exports


always_cooperate = AlwaysCooperate()
always_defect = AlwaysDefect()
random_defect = RandomDefect()
