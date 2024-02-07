r"""utility functions for simulation """

from statistics import mean, mode


from .models import Session, Simulation, Strategy


def simulate(
    slot1: Strategy,
    slot2: Strategy,
    rounds=200,
) -> Simulation:
    """run simulation by strategies

    Return:
        - (simulation): object containing all simulation information
    """
    if slot1 is None or slot2 is None:
        raise ValueError("Provide two-set of strategies. [slot1] and [slot2]")

    simulation = Simulation()

    slot1 = slot1.create(1, simulation.history)
    slot2 = slot2.create(0, simulation.history)

    for _ in range(rounds):
        session = Session(names=[slot1.name, slot2.name])

        session.players[0].respond(strategy=slot1)

        session.players[1].respond(strategy=slot2)

        session.compute_payoffs()

        # the sucker loses and dies
        if session.players[0].score > session.players[1].score:
            slot1.population += 1
            slot2.population -= 1

        if session.players[1].score > session.players[0].score:
            slot2.population += 1
            slot1.population -= 1

        # both players benefit and survive when they cooperate
        if session.players[1].score == session.players[0].score == 3:
            slot2.population += 1
            slot1.population += 1

        # both players lose and die out when they defect
        if session.players[1].score == session.players[0].score == 1:
            slot2.population -= 1
            slot1.population -= 1

        simulation.history.append(session)

    update_statistics(slot1, simulation, 1)
    update_statistics(slot2, simulation, 2)

    return simulation


def update_statistics(
    strategy: Strategy,
    simulation_instance: Simulation,
    slot_num: int,
) -> dict[str, int]:
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


def summarize_statistics(strategy: Strategy) -> dict:
    """summarize all statistics

    Args:
        initial_statistics (dict): initial statistics as a dictionary of lists

    Returns:
        dict: final statistics as a dictionary of values
    """

    final_statistics: dict = {"total": [], "average": [], "mode": []}

    final_statistics["total"] = sum(strategy.statistics["total"])

    final_statistics["average"] = mean(strategy.statistics["average"])

    final_statistics["mode"] = mode(strategy.statistics["mode"])

    return final_statistics


def tabulate_summary(strategy: Strategy | None = None) -> None:
    """print summary table lines

    Args:
        strategy (strategy, optional): strategy object. Defaults to None.
        statistics (dict, optional): dictionary of simulation strategy statistics. Defaults to None.
    """
    if strategy is None:
        print(
            "   ",
            "strategy".ljust(30),
            "total".center(10),
            "average".center(10),
            "mode".center(10),
            sep="",
        )

        return

    summary = summarize_statistics(strategy)

    name_string = str(strategy.name)

    total_string = str(summary["total"])
    average_string = str(round(summary["average"], 3))
    mode_string = str(summary["mode"])

    print(
        "   ",
        name_string.ljust(30),
        total_string.center(10),
        average_string.center(10),
        mode_string.center(10),
        sep="",
    )
