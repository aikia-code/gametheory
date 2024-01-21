r"""
Symbols for Choices, Payoffs
"""


class Action:
    """
    Static choice to COOPERATE or DEFECT

    Usage:
        Choice.COOPERATE: Choose to Cooperate in a given session
    """

    COOPERATE = (0, "COOPERATE", "+")
    DEFECT = (1, "DEFECT", "-")


class Payoff:
    """
    Payoff symbols for PUNISH, REWARD, TEMPT, or SUCKER

    Usage:
        Payoff.PUNISH: Awards a payoff of PUNISH
    """

    PUNISH = (1, "PUNISH", "P")
    REWARD = (3, "REWARD", "R")
    TEMPT = (5, "TEMPT", "T")
    SUCKER = (0, "SUCKER", "S")
