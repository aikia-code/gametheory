r"""collection of models for the dilemma simulation
"""

# python statistics module
from statistics import mean, mode
from typing import Self


# Actions
from .symbols import COOPERATE, DEFECT

# Payoffs
from .symbols import PUNISH, REWARD, TEMPT, SUCKER


class Strategy:
    """Supper class for strategies"""

    name = "***"
    statistics: dict = {"total": [], "average": [], "mode": []}

    def __init__(self, opponent_index: int, session_history: list) -> None:
        self.opponent_index = opponent_index
        self.session_history = session_history

    def run(self) -> tuple[int, str, str]:
        """returns action type"""
        raise NotImplementedError("(method)run: -> [Action.*] must be implemented")

    def create(self, opponent_index: int, session_history: list) -> Self:
        """return self with opponent data and session history data

        Args:
            opponent_index (int, optional): opponent reference. Defaults to 0 | 1.
            session_history (list, optional): history list. Defaults to None.

        Returns:
            Strategy: Self
        """
        self.opponent_index = opponent_index
        self.session_history = session_history

        return self


class Player:
    """describes a player and provides a state for player object"""

    def __init__(self, name: str) -> None:
        """Create a player by name"""

        self.action = DEFECT

        self.score = SUCKER[0]

        self.name = name

    def respond(self, strategy: Strategy) -> None:
        """player response with strategy implemented

        Args:
            strategy (strategy): strategy
        """
        self.action = strategy.run()

    def __str__(self) -> str:
        return f"{self.name} | {self.action[1]} | {self.score}"


class Session:
    """A game session that computes player scores based on their choices"""

    def __init__(self, names: list[str]) -> None:
        """initialise players by name and processes the choices and scores"""
        self.players = (Player(names[0]), Player(names[1]))

    def compute_payoffs(self) -> None:
        """Computes scores of players"""
        if self.players[0].action == COOPERATE and self.players[1].action == COOPERATE:
            self.players[0].score = self.players[1].score = REWARD[0]
        elif self.players[0].action == COOPERATE and self.players[1].action == DEFECT:
            self.players[0].score = SUCKER[0]
            self.players[1].score = TEMPT[0]
        elif self.players[1].action == COOPERATE and self.players[0].action == DEFECT:
            self.players[1].score = SUCKER[0]
            self.players[0].score = TEMPT[0]
        elif self.players[0].action == DEFECT and self.players[1].action == DEFECT:
            self.players[0].score = self.players[1].score = PUNISH[0]

    def __str__(self) -> str:
        return f"1 | {self.players[0]}\n2 | {self.players[1]}\n"


class Simulation:
    """represent information from a simulation"""

    def __init__(self) -> None:
        self.history: list[Session] = []

    def get_total_score(self, slot_num: int = 1 | 2) -> int:
        """compute total scores of either player

        Returns:
            int: total score of player
        """
        if slot_num < 1 or slot_num > 2:
            raise ValueError
        slot1 = sum(session.players[0].score for session in self.history)
        slot2 = sum(session.players[1].score for session in self.history)
        return slot1 if slot_num == 1 else slot2

    def get_average_score(self, slot_num: int = 1 | 2) -> float:
        """compute average score of either player

        Returns:
            int: average score of player
        """
        if slot_num < 1 or slot_num > 2:
            raise ValueError
        slot1 = mean([session.players[0].score for session in self.history])
        slot2 = mean([session.players[1].score for session in self.history])
        return slot1 if slot_num == 1 else slot2

    def get_mode_score(self, slot_num: int = 1 | 2) -> int:
        """compute mode score of either player

        Returns:
            int: mode score of player
        """
        if slot_num < 1 or slot_num > 2:
            raise ValueError
        slot1 = mode([session.players[0].score for session in self.history])
        slot2 = mode([session.players[1].score for session in self.history])
        return int(slot1) if slot_num == 1 else int(slot2)

    def get_slot_name(self, slot_num: int = 1 | 2) -> str:
        """compute mode score of either player

        Returns:
            str: name of player
        """
        if slot_num < 1 or slot_num > 2:
            raise ValueError
        slot1 = self.history[0].players[0].name
        slot2 = self.history[0].players[1].name
        return slot1 if slot_num == 1 else slot2

    def get_action_pattern(self):
        """retrieve action patterns

        Returns:
            str:pattern
        """
        pattern = f"   {self.history[0].players[0].name}\n"
        pattern += "".join([session.players[0].action[2] for session in self.history])

        pattern += "\n"

        pattern += f"   {self.history[0].players[1].name}\n"
        pattern += "".join([session.players[1].action[2] for session in self.history])

        pattern += "\n"

        return pattern

    def __str__(self) -> str:
        sim_string = ""
        slot1 = self.get_slot_name(1)
        slot2 = self.get_slot_name(2)
        score1 = str(self.get_total_score(1))
        score2 = str(self.get_total_score(2))

        sim_string = f"{slot1.center(len(slot1)+2)}|{slot2.center(len(slot2)+2)}\n"
        sim_string += f"{score1.center(len(slot1)+2)}|{score2.center(len(slot2)+2)}"
        return sim_string
