r"""module entry point

UI:
    - Prisoner's dilemma
    - run simulation          ---[A]
    - setup simulation        ---[B]
    
    [A] - auto run every possible simulation
        - each strategy face off against itself and all other strategies
        - display full strategy statistics ranked by total score
        
        strategy                  | score | average | mode |
        always cooperate strategy |  500  |    3    |   5  |
        -                         |   -   |    -    |   -  |
        
    [B] - select strategy for slot 1 [list of strategies]
        - select strategy for slot 2 [list of strategies]
        - specify number of rounds >> _
        
        - run simulate with strategy
        - display statistics ranked by total score
        
        strategy                  | score | average | mode |
        always cooperate strategy |  500  |    3    |   5  |
        -                         |   -   |    -    |   -  |

"""
from statistics import mean, mode


from .simulation import simulate_strategies
from .strategies import always_cooperate, always_defect, random_defect

# strategy list:
# -------------------------------
# always cooperate
# always defect
# random defect


# strategy statistics
# -------------------------------
# _                      [total, average, mode]
always_cooperate_statistics = {"total": [], "average": [], "mode": []}
always_defect_statistics = {"total": [], "average": [], "mode": []}
random_defect_statistics = {"total": [], "average": [], "mode": []}


DEFAULT_ROUNDS = 200


# helper functions
# -------------------------------


def update_statistics(initial_statistics, simulation_instance, slot_num) -> dict:
    """Update current statistics

    Args:
        initial_statistics (dict): statistics object to update
        simulation_instance (simulation): simulation to pull data from

    Returns:
        dict: updated statistics
    """
    initial_statistics["total"].append(simulation_instance.get_total_score(slot_num))

    initial_statistics["average"].append(
        simulation_instance.get_average_score(slot_num)
    )

    initial_statistics["mode"].append(simulation_instance.get_mode_score(slot_num))

    return initial_statistics


def summarize_statistics(initial_statistics) -> dict:
    """summarize all statistics

    Args:
        initial_statistics (dict): initial statistics as a dictionary of lists

    Returns:
        dict: final statistics as a dictionary of values
    """

    initial_statistics["total"] = sum(initial_statistics["total"])

    initial_statistics["average"] = mean(initial_statistics["average"])

    initial_statistics["mode"] = mode(initial_statistics["mode"])

    return initial_statistics


# strategy face off
# -------------------------------

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
always_defect_statistics = update_statistics(always_defect_statistics, simulation, 2)


# always cooperate | random defect
simulation = simulate_strategies(
    slot1=always_cooperate, slot2=random_defect, rounds=DEFAULT_ROUNDS
)

always_cooperate_statistics = update_statistics(
    always_cooperate_statistics, simulation, 1
)
random_defect_statistics = update_statistics(random_defect_statistics, simulation, 2)


# always defect | always defect
simulation = simulate_strategies(
    slot1=always_defect, slot2=always_defect, rounds=DEFAULT_ROUNDS
)

always_defect_statistics = update_statistics(always_defect_statistics, simulation, 1)
always_defect_statistics = update_statistics(always_defect_statistics, simulation, 2)


# always defect | random defect
simulation = simulate_strategies(
    slot1=always_defect, slot2=random_defect, rounds=DEFAULT_ROUNDS
)

always_defect_statistics = update_statistics(always_defect_statistics, simulation, 1)
random_defect_statistics = update_statistics(random_defect_statistics, simulation, 2)


# random defect | random defect
simulation = simulate_strategies(
    slot1=random_defect, slot2=random_defect, rounds=DEFAULT_ROUNDS
)

random_defect_statistics = update_statistics(random_defect_statistics, simulation, 1)
random_defect_statistics = update_statistics(random_defect_statistics, simulation, 2)


# summary
# -------------------------------

always_cooperate_statistics = summarize_statistics(always_cooperate_statistics)
always_defect_statistics = summarize_statistics(always_defect_statistics)
random_defect_statistics = summarize_statistics(random_defect_statistics)

print(always_cooperate_statistics)
print(always_defect_statistics)
print(random_defect_statistics)
