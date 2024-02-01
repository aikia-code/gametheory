r"""symbols collection module
"""

Payoff = tuple[int, str, str]
PlayerAction = tuple[int, str, str]

# ------------------------------------------
# Actions

COOPERATE: PlayerAction = (0, "COOPERATE", "+")
DEFECT: PlayerAction = (1, "DEFECT", "-")


# ------------------------------------------
# Payoffs
PUNISH: Payoff = (1, "PUNISH", "P")
REWARD: Payoff = (3, "REWARD", "R")
TEMPT: Payoff = (5, "TEMPT", "T")
SUCKER: Payoff = (0, "SUCKER", "S")
