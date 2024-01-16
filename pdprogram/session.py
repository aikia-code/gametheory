from pdprogram.player import Player
from pdprogram.symbols import Choice, Score


class Session:
    """A game session that computes player scores based on thier choices"""

    def __init__(self, playerA: Player, playerB: Player):
        """Process the choices made and compute scores"""
        self.playerA = playerA
        self.playerB = playerB

    def compute_score(self):
        """Computes the results of a single session of the game"""
        if (
            self.playerA.choice == Choice.COOPORATE
            and self.playerB.choice == Choice.COOPORATE
        ):
            self.playerA.score = self.playerB.score = Score.REWARD
        elif (
            self.playerA.choice == Choice.COOPORATE
            and self.playerB.choice == Choice.DEFECT
        ):
            self.playerA.score = Score.SUCKER
            self.playerB.score = Score.TEMPT
        elif (
            self.playerB.choice == Choice.COOPORATE
            and self.playerA.choice == Choice.DEFECT
        ):
            self.playerB.score = Score.SUCKER
            self.playerA.score = Score.TEMPT
        elif (
            self.playerA.choice == Choice.DEFECT
            and self.playerB.choice == Choice.DEFECT
        ):
            self.playerA.score = self.playerB.score = Score.PUNISH

    def get_choice(self, name: str) -> tuple:
        """Returns the exact response of a player

        Args:
            player (Player): Player object to check response of

        Returns:
            tuple: Choice tuple of player
        """
        if name == self.playerA.name:
            return self.playerA.choice
        if name == self.playerB.name:
            return self.playerB.choice

    def get_score(self, name: str) -> tuple:
        """Returns the exact score of a Player

        Args:
            player (Player): Player object to get score of

        Returns:
            tuple: Score tuple of player
        """
        if name == self.playerA.name:
            return self.playerA.score
        if name == self.playerB.name:
            return self.playerB.score

    def __str__(self):
        return f"A > {self.playerA}\nB > {self.playerB}\n"
