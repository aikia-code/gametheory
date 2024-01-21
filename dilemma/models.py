r"""models collection module
"""

from .symbols import Action, Payoff


class Player:
    """describes a player and provides a state for player object"""

    def __init__(self, name):
        """Create a player by name"""

        self.action = Action.COOPERATE

        self.score = Payoff.SUCKER[0]

        self.name = name

    def respond(self, strategy, opponent=None, history=None):
        """player response with strategy implemented

        Args:
            strategy (function): strategy callback
            opponent (player, optional): opponent to face off with strategy. Defaults to None.
            history (list[session], optional): history data to incorporate into strategy.
            Defaults to None.
        """
        self.action = strategy(history=history, opponent=opponent)

    def __str__(self):
        return f"{self.name} | {self.action[1]} | {self.score}"


class Session:
    """A game session that computes player scores based on their choices"""

    def __init__(self, names):
        """initialise players by name and processes the choices and scores"""
        self.players = (Player(names[0]), Player(names[1]))

    def compute_score(self):
        """Computes scores of players"""
        if (
            self.players[0].action == Action.COOPERATE
            and self.players[1].action == Action.COOPERATE
        ):
            self.players[0].score = self.players[1].score = Payoff.REWARD[0]
        elif (
            self.players[0].action == Action.COOPERATE
            and self.players[1].action == Action.DEFECT
        ):
            self.players[0].score = Payoff.SUCKER[0]
            self.players[1].score = Payoff.TEMPT[0]
        elif (
            self.players[1].action == Action.COOPERATE
            and self.players[0].action == Action.DEFECT
        ):
            self.players[1].score = Payoff.SUCKER[0]
            self.players[0].score = Payoff.TEMPT[0]
        elif (
            self.players[0].action == Action.DEFECT
            and self.players[1].action == Action.DEFECT
        ):
            self.players[0].score = self.players[1].score = Payoff.PUNISH[0]

    def __str__(self):
        return f"A > {self.players[0]}\nB > {self.players[1]}\n"


class SimulationInfo:
    """represent information from a simulation"""

    def __init__(self):
        self.history = []

    def compute_score(self):
        """computes simulation scores

        Returns:
            tuple[int, int]: scores of each player
        """
        score_0 = sum(session.players[0].score for session in self.history)
        score_1 = sum(session.players[1].score for session in self.history)
        return (score_0, score_1)

    def to_table_format(self):
        """formats simulation info as table. can be displayed on cui"""
        pass

    def to_csv_format(self):
        """formats simulation info as a table with comma separated values. can be written to file"""
        pass

    def __str__(self):
        total_scores = self.compute_score()
        sim_string = f"{self.history[0].players[0].name}\n"
        sim_string += "".join(session.players[0].action[2] for session in self.history)
        sim_string += f" {total_scores[0]}\n"
        sim_string += "".join(session.players[1].action[2] for session in self.history)
        sim_string += f" {total_scores[1]}\n"
        sim_string += f"{self.history[0].players[1].name}\n"
        return sim_string
