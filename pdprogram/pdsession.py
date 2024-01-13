from pdplayer import Player

from pdtypes import Choice, Score


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

    def get_choices(self, player=None):
        if player is not None:
            if player == self.playerA:
                return self.playerA.choice
            if player == self.playerB:
                return self.playerB.choice
        return {
            self.playerA.name: self.playerA.choice[1],
            self.playerB.name: self.playerB.choice[1],
        }

    def get_scores(self, player=None):
        if player is not None:
            if player == self.playerA:
                return self.playerA.score
            if player == self.playerB:
                return self.playerB.score
        return {
            self.playerA.name: self.playerA.score[1],
            self.playerB.name: self.playerB.score[1],
        }

    def show_results(self):
        print(
            self.playerA.name,
            "->",
            self.playerA.choice[1],
            "|",
            self.playerA.score[1],
            "=",
            self.playerA.score[0],
            sep="  ",
        )

        print(
            self.playerB.name,
            "->",
            self.playerB.choice[1],
            "|",
            self.playerB.score[1],
            "=",
            self.playerB.score[0],
            sep="  ",
        )

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def __str__(self):
        return f"A: {self.playerA}\nB: {self.playerB}"


# ==================================
