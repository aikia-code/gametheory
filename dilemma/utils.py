r"""utility functions for simulation """
from statistics import mean, mode


from .models import Session, Simulation


def get_strategy_name(strategy=None):
    """return the name of the strategy

    Args:
        strategy (strategy): strategy object

    Returns:
        str: name of strategy
    """
    if strategy is None:
        raise ValueError("A strategy needs to be specified")

    return strategy.strategy_name


def simulate_strategies(slot1=None, slot2=None, rounds=1) -> Simulation:
    """run simulation by strategies

    Return:
        - (simulation): object containing all simulation information
    """
    if slot1 is None or slot2 is None:
        raise ValueError("Provide two-set of strategies")

    simulation = Simulation()

    for _ in range(rounds):
        session = Session(names=(get_strategy_name(slot1), get_strategy_name(slot2)))

        session.players[0].respond(strategy=slot1)

        session.players[1].respond(strategy=slot2)

        session.compute_payoffs()

        simulation.history.append(session)

    return simulation


def update_statistics(strategy, simulation_instance, slot_num) -> dict:
    """Update current statistics

    Args:
        initial_statistics (dict): statistics object to update
        simulation_instance (simulation): simulation to pull data from

    Returns:
        dict: updated statistics
    """
    strategy.statistics["total"].append(simulation_instance.get_total_score(slot_num))

    strategy.statistics["average"].append(
        simulation_instance.get_average_score(slot_num)
    )

    strategy.statistics["mode"].append(simulation_instance.get_mode_score(slot_num))

    return strategy.statistics


def summarize_statistics(strategy) -> dict:
    """summarize all statistics

    Args:
        initial_statistics (dict): initial statistics as a dictionary of lists

    Returns:
        dict: final statistics as a dictionary of values
    """

    strategy.statistics["total"] = sum(strategy.statistics["total"])

    strategy.statistics["average"] = mean(strategy.statistics["average"])

    strategy.statistics["mode"] = mode(strategy.statistics["mode"])

    return strategy.statistics


def tabulate_summary(strategy=None):
    """print summary table lines

    Args:
        strategy (strategy, optional): strategy object. Defaults to None.
        statistics (dict, optional): dictionary of simulation strategy statistics. Defaults to None.
    """
    if strategy is None:
        print(
            "strategy".ljust(30),
            "total".center(10),
            "average".center(10),
            "mode".center(10),
            sep="",
        )
        return
    name_string = str(get_strategy_name(strategy))
    total_string = str(strategy.statistics["total"])
    average_string = str(round(strategy.statistics["average"], 3))
    mode_string = str(strategy.statistics["mode"])

    print(
        name_string.ljust(30),
        total_string.center(10),
        average_string.center(10),
        mode_string.center(10),
        sep="",
    )
