r"""Simulation module for main subprocesses"""

from .utils import (
    simulate,
    summarize_statistics,
    tabulate_summary,
)
from .strategies import always_cooperate, always_defect, random_defect

DEFAULT_ROUNDS = 200


strategies = {
    1: always_cooperate,
    2: always_defect,
    3: random_defect,
}


def process_run_simulation():
    """sub process for full simulation"""

    # always cooperate | always cooperate
    simulate(slot1=always_cooperate, slot2=always_cooperate, rounds=DEFAULT_ROUNDS)

    # always cooperate | always defect
    simulate(slot1=always_cooperate, slot2=always_defect, rounds=DEFAULT_ROUNDS)

    # always cooperate | random defect
    simulate(slot1=always_cooperate, slot2=random_defect, rounds=DEFAULT_ROUNDS)

    # always defect | always defect
    simulate(slot1=always_defect, slot2=always_defect, rounds=DEFAULT_ROUNDS)

    # always defect | random defect
    simulate(slot1=always_defect, slot2=random_defect, rounds=DEFAULT_ROUNDS)

    # random defect | random defect | TODO: fix: random defect probability to 50%

    # tit for tat | tit for tat

    # tit for tat | random defect

    # tit for tat | alway defect

    # tit for tat | always cooperate

    # summarize
    # -------------------------------
    summarize_statistics(always_defect)
    summarize_statistics(always_cooperate)
    summarize_statistics(random_defect)

    tabulate_summary()
    tabulate_summary(always_cooperate)
    tabulate_summary(always_defect)
    tabulate_summary(random_defect)


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
