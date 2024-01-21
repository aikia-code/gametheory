r"""Simulation module
"""

from .models import Session, SimulationInfo
from .strategy import random_action, always_cooperate


class Simulation:
    """class to setup and run simulation"""

    def __init__(self) -> None:
        self.info = SimulationInfo()

    def main(self, rounds=50):
        """Simulation entry point

        Args:
            rounds (int, optional): number iterations to run the simulation. Defaults to 50.
        """

        for _ in range(rounds):
            session = Session(names=("tit4tat", "rand"))

            session.players[0].respond(strategy=always_cooperate)

            session.players[1].respond(strategy=random_action)

            session.compute_score()

            self.info.history.append(session)

        print(self.info)
