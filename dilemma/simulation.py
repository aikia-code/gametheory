r"""Simulation module for main subprocesses"""

from .models import Strategy

from .utils import (
    simulate,
    tabulate_summary,
)
from .strategies import (
    AlwaysCooperate,
    AlwaysDefect,
    Historian,
    RandomDefect,
    TitFor2Tat,
    TitForTat,
    Unforgiving,
)

# strategies list
strategies: dict[int, Strategy] = {
    1: AlwaysCooperate([]),
    2: AlwaysDefect([]),
    3: RandomDefect([]),
    4: TitForTat([]),
    5: TitFor2Tat([]),
    6: Historian([]),
    7: Unforgiving([]),
}


def reset_strategies():
    """Reset strategies list"""
    strategies[1] = AlwaysCooperate([])
    strategies[2] = AlwaysDefect([])
    strategies[3] = RandomDefect([])
    strategies[4] = TitForTat([])
    strategies[5] = TitFor2Tat([])
    strategies[6] = Historian([])
    strategies[7] = Unforgiving([])


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

    # unforgiving | unforgiving
    print(simulate(slot1=strategies[7], slot2=strategies[7]))

    # unforgiving | always cooperate
    print(simulate(slot1=strategies[7], slot2=strategies[1]))

    # unforgiving | always defect
    print(simulate(slot1=strategies[7], slot2=strategies[2]))

    # unforgiving | random defect
    print(simulate(slot1=strategies[7], slot2=strategies[3]))

    # unforgiving | tit 4 tat
    print(simulate(slot1=strategies[7], slot2=strategies[4]))

    # unforgiving | tit 4 2 tat
    print(simulate(slot1=strategies[7], slot2=strategies[5]))

    # unforgiving | historian
    print(simulate(slot1=strategies[7], slot2=strategies[6]))


def summarize_simulation_table():
    """summarize and tabulate statistics"""
    print(
        "summary ",
        "================================================================ ",
        sep="\n",
    )

    tabulate_summary()

    for strategy in strategies.values():
        tabulate_summary(strategy)

    print(
        "population",
        "================================================================ ",
        sep="\n",
    )

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

    tabulate_summary()
    tabulate_summary(slot1)
    tabulate_summary(slot2)

    print(
        "  ",
        "   [1]---   Show action pattern?   ---[-]",
        "   [2]---   New Simulation         ---[-]",
        "   [3]---   close (X)              ---[-]",
        sep="\n",
    )
    show_pattern = input("> ")
    if show_pattern in ["1"]:
        print(simulation.get_action_pattern())

    if show_pattern in ["3", "x", "X"]:
        return


def user_input_select_strategy(slot_label: str) -> Strategy:
    """select strategy sequence

    Args:
        slot_label (str): Slot label for messaging

    Returns:
        strategy: selected strategy
    """
    print(f"select strategy for {slot_label}")

    for index, strategy in strategies.items():
        print(f"  [{index}]---   ", strategy.name)

    slot = strategies[int(input("> "))]

    return slot
