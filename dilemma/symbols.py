r"""
Static types and constants for Choices, Scores
"""


class Choice:
    """
    Static choice to COOPERATE or DEFECT

    Usage:
        Choice.COOPERATE: Choose to Cooperate in a given session
    """

    COOPERATE = (0, "COOPERATE", "+")
    DEFECT = (1, "DEFECT", "-")


class Score:
    """
    Static scores for PUNISH, REWARD, TEMPT, or SUCKER

    Usage:
        Score.PUNISH: Award a score of PUNISH
    """

    PUNISH = (1, "PUNISH", "P")
    REWARD = (3, "REWARD", "R")
    TEMPT = (6, "TEMPT", "T")
    SUCKER = (0, "SUCKER", "S")
