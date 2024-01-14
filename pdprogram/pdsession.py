from pdprogram.pdplayer import Player
from pdprogram.pdtypes import Choice, Score


class Session:
    """A game session that computes player scores based on thier choices"""

    def __init__(self, playerA: Player, playerB: Player):
        """Process the choices made and compute scores"""
        self.playerA = playerA
        self.playerB = playerB

    def compute_score(self):
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

    def get_players(self):
        return {"A": self.playerA.name, "B": self.playerB.name}

    def get_player_choice(self, player: Player) -> tuple:
        """Returns the exact response of a player

        Args:
            player (Player): Player object to check response of

        Returns:
            tuple: Choice tuple of player
        """
        if player == self.playerA:
            return self.playerA.choice
        if player == self.playerB:
            return self.playerB.choice

    def get_choices(self) -> dict:
        """Returns responses of all players in the session

        Returns:
            dict: Dictionary object of Player A and Player B response
        """
        return {
            self.playerA.name: self.playerA.choice,
            self.playerB.name: self.playerB.choice,
        }

    def get_player_score(self, player: Player) -> tuple:
        """Returns the exact score of a Player

        Args:
            player (Player): Player object to get score of

        Returns:
            tuple: Score tuple of player
        """
        if player == self.playerA:
            return self.playerA.score
        if player == self.playerB:
            return self.playerB.score

    def get_scores(self):
        """Returns scores of all players in the session

        Returns:
            dict: Dictionary object of Player A and Player B score
        """
        return {
            self.playerA.name: self.playerA.score,
            self.playerB.name: self.playerB.score,
        }

    def __str__(self):
        return f"A: {self.playerA}\nB: {self.playerB}"
