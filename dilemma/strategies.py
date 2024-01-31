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
    statistics = {"total": [], "average": [], "mode": []}

    def __init__(self, opponent_index: int = 0 | 1, session_history: list = None):
        super().__init__(opponent_index, session_history)

    def run(self):
        return COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    name = "Always Defect"
    statistics = {"total": [], "average": [], "mode": []}

    def __init__(
        self, opponent_index: int = 0 | 1, session_history: list = None
    ) -> None:
        super().__init__(opponent_index, session_history)

    def run(self):
        return DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    name = "Random"
    statistics = {"total": [], "average": [], "mode": []}

    def __init__(
        self, opponent_index: int = 0 | 1, session_history: list = None
    ) -> None:
        super().__init__(opponent_index, session_history)

    def run(self):
        player_choices = [COOPERATE, DEFECT]

        return choice(player_choices)


class TitForTat(Strategy):
    """Tit for tat strategy"""

    name = "Tit for Tat"
    statistics = {"total": [], "average": [], "mode": []}

    def __init__(
        self, opponent_index: int = 0 | 1, session_history: list = None
    ) -> None:
        super().__init__(opponent_index, session_history)

    def run(self):
        return (
            DEFECT
            if self.session_history[-1].players[self.opponent_index].action
            else COOPERATE
        )


# -----------------------------------------------------
# exports
