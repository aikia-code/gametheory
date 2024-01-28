r"""Simulation module for main subprocesses"""

from .utils import (
    simulate_strategies,
    update_statistics,
    summarize_statistics,
    tabulate_summary,
)
from .strategies import always_cooperate, always_defect, random_defect

DEFAULT_ROUNDS = 200


def process_run_simulation():
    """sub process for full simulation"""

    always_cooperate_statistics = {"total": [], "average": [], "mode": []}
    always_defect_statistics = {"total": [], "average": [], "mode": []}
    random_defect_statistics = {"total": [], "average": [], "mode": []}

    # always cooperate | always cooperate
    simulation = simulate_strategies(
        slot1=always_cooperate, slot2=always_cooperate, rounds=DEFAULT_ROUNDS
    )

    always_cooperate_statistics = update_statistics(
        always_cooperate_statistics, simulation, 1
    )
    always_cooperate_statistics = update_statistics(
        always_cooperate_statistics, simulation, 2
    )

    # always cooperate | always defect
    simulation = simulate_strategies(
        slot1=always_cooperate, slot2=always_defect, rounds=DEFAULT_ROUNDS
    )

    always_cooperate_statistics = update_statistics(
        always_cooperate_statistics, simulation, 1
    )
    always_defect_statistics = update_statistics(
        always_defect_statistics, simulation, 2
    )

    # always cooperate | random defect
    simulation = simulate_strategies(
        slot1=always_cooperate, slot2=random_defect, rounds=DEFAULT_ROUNDS
    )

    always_cooperate_statistics = update_statistics(
        always_cooperate_statistics, simulation, 1
    )
    random_defect_statistics = update_statistics(
        random_defect_statistics, simulation, 2
    )

    # always defect | always defect
    simulation = simulate_strategies(
        slot1=always_defect, slot2=always_defect, rounds=DEFAULT_ROUNDS
    )

    always_defect_statistics = update_statistics(
        always_defect_statistics, simulation, 1
    )
    always_defect_statistics = update_statistics(
        always_defect_statistics, simulation, 2
    )

    # always defect | random defect
    simulation = simulate_strategies(
        slot1=always_defect, slot2=random_defect, rounds=DEFAULT_ROUNDS
    )

    always_defect_statistics = update_statistics(
        always_defect_statistics, simulation, 1
    )
    random_defect_statistics = update_statistics(
        random_defect_statistics, simulation, 2
    )

    # random defect | random defect
    simulation = simulate_strategies(
        slot1=random_defect, slot2=random_defect, rounds=DEFAULT_ROUNDS
    )

    random_defect_statistics = update_statistics(
        random_defect_statistics, simulation, 1
    )
    random_defect_statistics = update_statistics(
        random_defect_statistics, simulation, 2
    )

    # summarize
    # -------------------------------

    always_cooperate_statistics = summarize_statistics(always_cooperate_statistics)
    always_defect_statistics = summarize_statistics(always_defect_statistics)
    random_defect_statistics = summarize_statistics(random_defect_statistics)

    tabulate_summary()
    tabulate_summary(always_cooperate, always_cooperate_statistics)
    tabulate_summary(always_defect, always_defect_statistics)
    tabulate_summary(random_defect, random_defect_statistics)
