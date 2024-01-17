from dilemma.player import Player
from dilemma.symbols import Choice, Score


class Session:
    """A game session that computes player scores based on their choices"""

    def __init__(self, player_a: Player, player_b: Player):
        """Process the choices made and compute scores"""
        self.player_a = player_a
        self.player_b = player_b

    def compute_score(self):
        """Computes the results of a single session of the game"""
        if (
            self.player_a.choice == Choice.COOPERATE
            and self.player_b.choice == Choice.COOPERATE
        ):
            self.player_a.score = self.player_b.score = Score.REWARD
        elif (
            self.player_a.choice == Choice.COOPERATE
            and self.player_b.choice == Choice.DEFECT
        ):
            self.player_a.score = Score.SUCKER
            self.player_b.score = Score.TEMPT
        elif (
            self.player_b.choice == Choice.COOPERATE
            and self.player_a.choice == Choice.DEFECT
        ):
            self.player_b.score = Score.SUCKER
            self.player_a.score = Score.TEMPT
        elif (
            self.player_a.choice == Choice.DEFECT
            and self.player_b.choice == Choice.DEFECT
        ):
            self.player_a.score = self.player_b.score = Score.PUNISH

    def get_choice(self, name: str) -> tuple:
        """Returns the exact response of a player

        Args:
            player (Player): Player object to check response of

        Returns:
            tuple: Choice tuple of player
        """
        if name == self.player_a.name:
            return self.player_a.choice
        if name == self.player_b.name:
            return self.player_b.choice

    def get_score(self, name: str) -> tuple:
        """Returns the exact score of a Player

        Args:
            player (Player): Player object to get score of

        Returns:
            tuple: Score tuple of player
        """
        if name == self.player_a.name:
            return self.player_a.score
        if name == self.player_b.name:
            return self.player_b.score

    def __str__(self):
        return f"A > {self.player_a}\nB > {self.player_b}\n"
