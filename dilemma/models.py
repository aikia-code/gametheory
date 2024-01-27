r"""collection of models for the dilemma simulation
"""

# Actions
from .symbols import COOPERATE, DEFECT

# Payoffs
from .symbols import PUNISH, REWARD, TEMPT, SUCKER


class Player:
    """describes a player and provides a state for player object"""

    def __init__(self, name):
        """Create a player by name"""

        self.action = DEFECT

        self.score = SUCKER[0]

        self.name = name

    def respond(self, strategy=None):
        """player response with strategy implemented

        Args:
            strategy (strategy): strategy
        """
        self.action = strategy.run()

    def __str__(self):
        return f"{self.name} | {self.action[1]} | {self.score}"


class Session:
    """A game session that computes player scores based on their choices"""

    def __init__(self, names):
        """initialise players by name and processes the choices and scores"""
        self.players = (Player(names[0]), Player(names[1]))

    def compute_payoffs(self):
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

    def __str__(self):
        return f"1 | {self.players[0]}\n2 | {self.players[1]}\n"


class Simulation:
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

    def __str__(self):
        total_scores = self.compute_score()
        sim_string = f"{self.history[0].players[0].name}\n"
        sim_string += "".join(session.players[0].action[2] for session in self.history)
        sim_string += f" {total_scores[0]}\n"
        sim_string += "".join(session.players[1].action[2] for session in self.history)
        sim_string += f" {total_scores[1]}\n"
        sim_string += f"{self.history[0].players[1].name}\n"
        return sim_string


class Strategy:
    """Supper class for strategies"""

    def __init__(self):
        self.player_index = None
        self.session_history = None

    def run(self):
        """returns action type"""
        raise NotImplementedError("(method)run: -> [Action.*] must be implemented")

    def create(self, player_index, session_history):
        """accepts and initializes player_index and history attribute"""
        self.player_index = player_index
        self.session_history = session_history
        return self
