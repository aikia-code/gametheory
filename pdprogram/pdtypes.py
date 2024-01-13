r"""
Static types and constants for Choices, Scores
"""


class Choice:
    """
    Static choice to COOPORATE or DEFECT

    Usage:
        Choice.COOPORATE: Choose to Cooporate in a given session
    """

    COOPORATE = (0, "COOPORATE")
    DEFECT = (1, "DEFECT")


class Score:
    """
    Static scores for PUNISH, REWARD, TEMPT, or SUCKER

    Usage:
        Score.PUNISH: Award a score of PUNISH
    """

    PUNISH = (1, "PUNISH")
    REWARD = (3, "REWARD")
    TEMPT = (6, "TEMPT")
    SUCKER = (0, "SUCKER")


# ======================================================

# print(Choice.COOPORATE)
# print(Choice.DEFECT)
