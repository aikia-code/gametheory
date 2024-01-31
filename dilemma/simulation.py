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
}


def process_run_simulation():
    """sub process for full simulation"""

    # always cooperate | always cooperate
    simulate(slot1=AlwaysCooperate, slot2=AlwaysCooperate, rounds=DEFAULT_ROUNDS)

    # always cooperate | always defect
    simulate(slot1=AlwaysCooperate, slot2=AlwaysDefect, rounds=DEFAULT_ROUNDS)

    # always cooperate | random defect
    simulate(slot1=AlwaysCooperate, slot2=RandomDefect, rounds=DEFAULT_ROUNDS)

    # always defect | always defect
    simulate(slot1=AlwaysDefect, slot2=AlwaysDefect, rounds=DEFAULT_ROUNDS)

    # always defect | random defect
    simulate(slot1=AlwaysDefect, slot2=RandomDefect, rounds=DEFAULT_ROUNDS)

    # random defect | random defect | TODO: fix: random defect probability to 50%

    # tit for tat | tit for tat

    # tit for tat | random defect

    # tit for tat | alway defect

    # tit for tat | always cooperate

    # summarize
    # -------------------------------
    summarize_statistics(AlwaysDefect)
    summarize_statistics(AlwaysCooperate)
    summarize_statistics(RandomDefect)

    tabulate_summary()
    tabulate_summary(AlwaysCooperate)
    tabulate_summary(AlwaysDefect)
    tabulate_summary(RandomDefect)


def process_setup_simulation():
    """sub process for user to setup simulation"""

    slot1 = user_input_select_strategy("slot-1")

    slot2 = user_input_select_strategy("slot-2")

    print("specify number of rounds")
    number_of_rounds = int(input("> "))

    simulate(slot1, slot2, number_of_rounds)

    summarize_statistics(slot1)
    summarize_statistics(slot2)

    tabulate_summary()
    tabulate_summary(slot1)
    tabulate_summary(slot2)


def user_input_select_strategy(slot_label):
    """select strategy sequence

    Args:
        slot_label (str): Slot label for messaging

    Returns:
        strategy: selected strategy
    """
    print(f"select strategy for {slot_label}")
    print(strategies[1].name, "  --[1]")
    print(strategies[2].name, "  --[2]")
    print(strategies[3].name, "  --[3]")
    slot = strategies[int(input("> "))]
    return slot
