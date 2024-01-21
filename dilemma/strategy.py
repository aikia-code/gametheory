r"""A collection of available strategies for simulation
"""

from random import choice

from .symbols import Action


def random_action(history, opponent):
    """Strategy that responds at random

    Args:
        history (list[Session]): history data from simulation
        opponent (Player): Opponent to face off with

    Returns:
        Action.symbol: Is response from implementing the strategy
    """

    player_choices = [Action.COOPERATE, Action.DEFECT]

    return choice(player_choices)


def always_cooperate(history, opponent):
    """Strategy that always cooperates

    Args:
        history (list[Session]): history data from simulation
        opponent (Player): Opponent to face off with

    Returns:
        Action.symbol: Is response from implementing the strategy
    """
    return Action.COOPERATE
