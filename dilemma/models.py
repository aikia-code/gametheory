from .symbols import Choice, Score


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


class Session:
    """A game session that computes player scores based on their choices"""

    def __init__(self, names: tuple = (str, str)):
        """Accepts players by name and processes the choices and scores"""
        self.players = (Player(names[0]), Player(names[1]))

    def compute_score(self) -> None:
        """Computes scores of players"""
        if (
            self.players[0].choice == Choice.COOPERATE
            and self.players[1].choice == Choice.COOPERATE
        ):
            self.players[0].score = self.players[1].score = Score.REWARD
        elif (
            self.players[0].choice == Choice.COOPERATE
            and self.players[1].choice == Choice.DEFECT
        ):
            self.players[0].score = Score.SUCKER
            self.players[1].score = Score.TEMPT
        elif (
            self.players[1].choice == Choice.COOPERATE
            and self.players[0].choice == Choice.DEFECT
        ):
            self.players[1].score = Score.SUCKER
            self.players[0].score = Score.TEMPT
        elif (
            self.players[0].choice == Choice.DEFECT
            and self.players[1].choice == Choice.DEFECT
        ):
            self.players[0].score = self.players[1].score = Score.PUNISH

    def get_choice(self, player: Player) -> tuple:
        """Returns the exact response of a player

        Args:
            player (Player): Player object to check response of

        Returns:
            tuple: Choice tuple of player
        """
        if player == self.players[0]:
            return self.players[0].choice
        if player == self.players[1]:
            return self.players[1].choice

    def get_score(self, player: Player) -> tuple:
        """Returns the exact score of a Player

        Args:
            player (Player): Player object to get score of

        Returns:
            tuple: Score tuple of player
        """
        if player == self.players[0]:
            return self.players[0].score
        if player == self.players[1]:
            return self.players[1].score

    def __str__(self) -> str:
        return f"A > {self.players[0]}\nB > {self.players[1]}\n"


class SimulationInfo:
    def __init__(self, player_names: tuple = (str, str)) -> None:
        self.names = player_names
        self.sessions = []

    def __str__(self) -> str:
        sim_string = self.names[0] + "\n"

        for session in self.sessions:
            sim_string += session.players[0].choice[2]

        # TODO: display scores
        sim_string += "\n"

        for session in self.sessions:
            sim_string += session.players[1].choice[2]

        sim_string += "\n"
        sim_string += self.names[1] + "\n"

        return sim_string
