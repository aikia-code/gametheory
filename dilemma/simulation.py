r"""Main Simulation module containing all relevant actions for the
    program
"""

from .models import Session, Simulation
from .strategies import get_strategy_name


def simulate_strategies(slot1=None, slot2=None, rounds=1) -> Simulation:
    """run simulation by strategies

    Return:
        - (simulation): object containing all simulation information
    """
    if slot1 is None or slot2 is None:
        raise ValueError("Provide two-set of strategies")

    simulation = Simulation()

    for _ in range(rounds):
        session = Session(
            names=(get_strategy_name(slot1), get_strategy_name(slot2))
        )

        session.players[0].respond(strategy=slot1)

        session.players[1].respond(strategy=slot2)

        session.compute_payoffs()

        simulation.history.append(session)

    return simulation
