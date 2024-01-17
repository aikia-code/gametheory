from dilemma.symbols import Choice, Score


class Player:
    """describes a player and provides a state for player object"""

    def __init__(self, name: str):
        """Create a player by name"""

        """Choice"""
        self.choice = Choice.COOPERATE

        """Score"""
        self.score = Score.SUCKER

        """Name"""
        self.name = name

    def choose(self, choice=Choice.COOPERATE):
        """
        Make a choice to COOPERATE and DEFECT

        Args:
            tuple : Accepts Choice.COOPERATE or Choice.DEFECT. Defaults to Choice.COOPERATE.
        """
        self.choice = choice

    def __str__(self) -> str:
        return f"{self.name} | {self.choice[1]} | {self.score[1]}"
