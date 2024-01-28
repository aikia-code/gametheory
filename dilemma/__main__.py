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

from .simulation import process_run_simulation

print("Prisoner's dilemma")

while True:
    print("1. run simulation          ---[A]")
    print("2. setup simulation        ---[B]")

    user_choice = input("> ")

    if user_choice in ["a", "A", "1"]:
        process_run_simulation()
        break

    if user_choice in ["b", "B", "2"]:
        print("Try again!")
        break
