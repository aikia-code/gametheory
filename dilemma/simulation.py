r"""Simulation module for main subprocesses"""

from .utils import (
    simulate,
    summarize_statistics,
    tabulate_summary,
)
from .strategies import AlwaysCooperate, AlwaysDefect, RandomDefect, TitForTat

DEFAULT_ROUNDS = 400


strategies = {
    1: AlwaysCooperate,
    2: AlwaysDefect,
    3: RandomDefect,
    4: TitForTat,
}


def process_run_simulation():
    """sub process for full simulation"""

    # always cooperate | always cooperate
    simulate(slot1=strategies[1], slot2=strategies[1], rounds=DEFAULT_ROUNDS)

    # always cooperate | always defect
    simulate(slot1=strategies[1], slot2=strategies[2], rounds=DEFAULT_ROUNDS)

    # always cooperate | random defect
    simulate(slot1=strategies[1], slot2=strategies[3], rounds=DEFAULT_ROUNDS)

    # always defect | always defect
    simulate(slot1=strategies[2], slot2=strategies[2], rounds=DEFAULT_ROUNDS)

    # always defect | random defect
    simulate(slot1=strategies[2], slot2=strategies[3], rounds=DEFAULT_ROUNDS)

    # random defect | random defect | TODO: fix: random defect probability to 50%

    # tit for tat | tit for tat
    simulate(slot1=strategies[4], slot2=strategies[4], rounds=DEFAULT_ROUNDS)

    # tit for tat | always cooperate
    simulate(slot1=strategies[4], slot2=strategies[1], rounds=DEFAULT_ROUNDS)

    # tit for tat | alway defect
    simulate(slot1=strategies[4], slot2=strategies[2], rounds=DEFAULT_ROUNDS)

    # tit for tat | random defect
    simulate(slot1=strategies[4], slot2=strategies[3], rounds=DEFAULT_ROUNDS)

    # summarize
    # -------------------------------
    for strategy in strategies.values():
        summarize_statistics(strategy)

    tabulate_summary()

    for strategy in strategies.values():
        tabulate_summary(strategy)


def process_setup_simulation():
    """sub process for user to setup simulation"""

    slot1 = user_input_select_strategy("slot-1")

    slot2 = user_input_select_strategy("slot-2")

    print("specify number of rounds")
    number_of_rounds = int(input("   > "))

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


def user_input_select_strategy(slot_label):
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
