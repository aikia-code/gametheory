r"""Main Simulation module containing all relevant actions for the
    program
"""

from .models import Session, Simulation
from .strategies import get_strategy_name


def simulate_strategies(strategy1=None, strategy2=None, rounds=1):
    """run simulation by strategies

    Return:
        - (simulation): object containing all simulation information
    """
    simulation = Simulation()

    for _ in range(rounds):
        session = Session(
            names=(get_strategy_name(strategy1), get_strategy_name(strategy2))
        )

        session.players[0].respond(strategy=strategy1)

        session.players[1].respond(strategy=strategy2)

        session.compute_payoffs()

        simulation.history.append(session)

    return simulation
