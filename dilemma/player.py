from dilemma.symbols import Choice, Score


class Player:
    """describes a player and provides a state for player object"""

    def __init__(self, name: str):
        """Create a player by name"""

        """Choice"""
        self.choice = Choice.COOPORATE

        """Score"""
        self.score = Score.SUCKER

        """Name"""
        self.name = name

    def choose(self, choice=Choice.COOPORATE):
        """
        Make a choice to COOPORATE and DEFECT

        Args:
            tuple : Accepts Choice.COOPORATE or Choice.DEFECT. Defaults to Choice.COOPORATE.
        """
        self.choice = choice

    def __str__(self) -> str:
        return f"{self.name} | {self.choice[1]} | {self.score[1]}"
