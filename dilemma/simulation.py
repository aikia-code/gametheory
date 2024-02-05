r"""Simulation module for main subprocesses"""

from .models import Strategy

from .utils import (
    simulate,
    summarize_statistics,
    tabulate_summary,
)
from .strategies import (
    AlwaysCooperate,
    AlwaysDefect,
    Historian,
    RandomDefect,
    TitFor2Tat,
    TitForTat,
)

# strategies list
strategies: dict[int, type[Strategy]] = {
    1: AlwaysCooperate,
    2: AlwaysDefect,
    3: RandomDefect,
    4: TitForTat,
    5: TitFor2Tat,
    6: Historian,
}


def process_run_simulation() -> None:
    """sub process for full simulation"""

    print("simulating... ")

    # always cooperate | always cooperate
    print(simulate(slot1=strategies[1], slot2=strategies[1]))

    # always cooperate | always defect
    print(simulate(slot1=strategies[1], slot2=strategies[2]))

    # always cooperate | random defect
    print(simulate(slot1=strategies[1], slot2=strategies[3]))

    # always defect | always defect
    print(simulate(slot1=strategies[2], slot2=strategies[2]))

    # always defect | random defect
    print(simulate(slot1=strategies[2], slot2=strategies[3]))

    # random defect | random defect | TODO: fix: random defect probability to 50%

    # tit for tat | tit for tat
    print(simulate(slot1=strategies[4], slot2=strategies[4]))

    # tit for tat | always cooperate
    print(simulate(slot1=strategies[4], slot2=strategies[1]))

    # tit for tat | alway defect
    print(simulate(slot1=strategies[4], slot2=strategies[2]))

    # tit for tat | random defect
    print(simulate(slot1=strategies[4], slot2=strategies[3]))

    # tit for two tat | tit for two tat
    print(simulate(slot1=strategies[5], slot2=strategies[5]))

    # tit for two tat | tit for tat
    print(simulate(slot1=strategies[5], slot2=strategies[4]))

    # tit for two tat | always cooperate
    print(simulate(slot1=strategies[5], slot2=strategies[1]))

    # tit for two tat | always defect
    print(simulate(slot1=strategies[5], slot2=strategies[2]))

    # tit for two tat | random defect
    print(simulate(slot1=strategies[5], slot2=strategies[3]))

    # historian | historian
    print(simulate(slot1=strategies[6], slot2=strategies[6]))

    # historian | tit for 2 tat
    print(simulate(slot1=strategies[6], slot2=strategies[5]))

    # historian | tit for tat
    print(simulate(slot1=strategies[6], slot2=strategies[4]))

    # historian | always cooperate
    print(simulate(slot1=strategies[6], slot2=strategies[1]))

    # historian | always defect
    print(simulate(slot1=strategies[6], slot2=strategies[2]))

    # historian | random defect
    print(simulate(slot1=strategies[6], slot2=strategies[3]))


def summarize_simulation_table():
    """summarize and tabulate statistics"""
    print("summarizing... ")

    for strategy in strategies.values():
        summarize_statistics(strategy)

    tabulate_summary()

    for strategy in strategies.values():
        tabulate_summary(strategy)

    print("population")

    for strategy in strategies.values():
        print(f"   {strategy.name}   ---p{strategy.population}")


def process_setup_simulation() -> None:
    """sub process for user to setup simulation"""

    slot1 = user_input_select_strategy("slot-1")

    slot2 = user_input_select_strategy("slot-2")

    print("specify number of rounds")
    number_of_rounds = int(input("   > "))

    print("simulating... ")

    simulation = simulate(slot1, slot2, number_of_rounds)

    summarize_statistics(slot1)
    summarize_statistics(slot2)

    tabulate_summary()
    tabulate_summary(slot1)
    tabulate_summary(slot2)

    print(
        "Show action pattern?   ",
        "   [1]---   Yes   ---[Y]",
        "   [2]---   No    ---[N]",
        sep="\n",
    )
    show_pattern = input("   > ")
    if show_pattern in ["1", "y", "Y"]:
        print(simulation.get_action_pattern())


def user_input_select_strategy(slot_label: str) -> type[Strategy]:
    """select strategy sequence

    Args:
        slot_label (str): Slot label for messaging

    Returns:
        strategy: selected strategy
    """
    print(f"select strategy for {slot_label}")

    for index, strategy in strategies.items():
        print(f"  [{index}]---   ", strategy.name, "   ---")

    slot = strategies[int(input("   > "))]

    return slot
