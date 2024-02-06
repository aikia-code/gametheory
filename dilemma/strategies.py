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

    def run(self):
        return COOPERATE


class AlwaysDefect(Strategy):
    """Always Defect strategy

    Defects at every encounter
    """

    name = "Always Defect"

    def run(self):
        return DEFECT


class RandomDefect(Strategy):
    """Random Defect strategy

    Defects randomly with every encounter
    """

    name = "Random"

    def run(self):
        player_choices = [COOPERATE, DEFECT]

        return choice(player_choices)


class TitForTat(Strategy):
    """Tit for tat strategy"""

    name = "Tit for Tat"

    def run(self):
        try:
            if self.session_history[-1].players[self.opponent_index].action == DEFECT:
                return DEFECT
            return COOPERATE
        except IndexError:
            return COOPERATE


class TitFor2Tat(Strategy):
    """Tit for 2 tat strategy

    Defects after opponent defects twice in a row
    """

    name = "Tit for 2 Tat"

    def run(self):
        try:
            if (
                self.session_history[-1].players[self.opponent_index].action == DEFECT
                and self.session_history[-2].players[self.opponent_index].action
                == DEFECT
            ):
                return DEFECT
            return COOPERATE
        except IndexError:
            return COOPERATE


class Unforgiving(Strategy):
    """None Forgiving strategy

    Defects forever if opponent defects even once
    """

    name = "Unforgiving"

    def run(self):
        try:
            if self.session_history[-1].players[self.opponent_index].action == DEFECT:
                self.no_mercy = True
        except IndexError:
            return COOPERATE
        return DEFECT if self.no_mercy else COOPERATE


class Historian(Strategy):
    """Historian strategy

    Defects when opponent has only defected or defected more historically
    """

    name = "Historian"

    def run(self):
        try:
            self.opponent_action_history.append(
                self.session_history[-1].players[self.opponent_index].action
            )
        except IndexError:
            return COOPERATE

        total_cooperate = self.opponent_action_history.count(COOPERATE)
        total_defect = self.opponent_action_history.count(DEFECT)

        if total_defect > total_cooperate or total_cooperate == 0:
            return DEFECT
        else:
            return COOPERATE
