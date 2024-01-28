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

from .utils import (
    get_strategy_name,
    simulate_strategies,
    update_statistics,
    summarize_statistics,
    tabulate_summary,
)
from .strategies import always_cooperate, always_defect, random_defect
from .simulation import process_run_simulation


strategies = {
    1: always_cooperate,
    2: always_defect,
    3: random_defect,
}

print("Prisoner's dilemma")

while True:
    print("1. run simulation          ---[A]")
    print("2. setup simulation        ---[B]")

    user_choice = input("> ")

    if user_choice in ["a", "A", "1"]:
        process_run_simulation()
        break

    if user_choice in ["b", "B", "2"]:
        print("select strategy for slot1")
        print(get_strategy_name(strategies[1]), "  --[1]")
        print(get_strategy_name(strategies[2]), "  --[2]")
        print(get_strategy_name(strategies[3]), "  --[3]")
        slot1 = strategies[int(input("> "))]

        print("select strategy for slot2")
        print(get_strategy_name(strategies[1]), "  --[1]")
        print(get_strategy_name(strategies[2]), "  --[2]")
        print(get_strategy_name(strategies[3]), "  --[3]")
        slot2 = strategies[int(input("> "))]

        print("specify number of rounds")
        number_of_rounds = int(input("> "))

        simulation = simulate_strategies(slot1, slot2, number_of_rounds)

        slot1_statistics = {"total": [], "average": [], "mode": []}
        slot2_statistics = {"total": [], "average": [], "mode": []}

        slot1_statistics = update_statistics(slot1_statistics, simulation, 1)
        slot2_statistics = update_statistics(slot2_statistics, simulation, 2)

        slot1_statistics = summarize_statistics(slot1_statistics)
        slot2_statistics = summarize_statistics(slot2_statistics)

        tabulate_summary()
        tabulate_summary(slot1, slot1_statistics)
        tabulate_summary(slot2, slot2_statistics)

        break
