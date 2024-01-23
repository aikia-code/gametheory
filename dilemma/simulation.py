r"""Simulation module
"""

from .models import Session, SimulationInfo
from .strategies import always_cooperate, random_defect


def main(rounds=100):
    """Simulation entry point

    Args:
        rounds (int, optional): number iterations to run the simulation. Defaults to 50.
    """
    info = SimulationInfo()

    for _ in range(rounds):
        session = Session(names=("tit4tat", "rand"))

        session.players[0].respond(strategy=always_cooperate)

        session.players[1].respond(strategy=random_defect)

        session.compute_payoffs()

        info.history.append(session)

    print(info)
