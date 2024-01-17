from random import choice

# Program library
from dilemma.player import Player
from dilemma.session import Session
from dilemma.symbols import Choice, Score


class Simulation:
    def main(rounds: int = 200) -> None:
        # TODO: Simulation info object to store Simulation data like this: sessions list
        sessions = []

        p1 = "Tit for tat"
        p2 = "Random"

        for _ in range(rounds):
            player_a, player_b = Player(p1), Player(p2)

            session = Session(player_a, player_b)

            # TODO: Strategies module with functions to handle execution, creation and storage of strategies
            # BEGIN STRATEGY

            # player A strategy is tit for tat
            try:
                if sessions[-1].get_choice(p2) == Choice.DEFECT:
                    player_a.choose(Choice.DEFECT)
                else:
                    player_a.choose(Choice.COOPERATE)
            except IndexError:
                player_a.choose(Choice.COOPERATE)

            # player B strategy is to randomly choose responses
            player_choices = [Choice.COOPERATE, Choice.DEFECT]

            player_b.choose(choice(player_choices))

            # END STRATEGY

            # session score computation
            session.compute_score()

            # record session data
            sessions.append(session)

        # print out results for visual
        # TODO: Utility functions to handle pretty printing to console
        # TODO: Utility functions to handle writing results to file
        # TODO: Simulation info Object designed to only display simulation outcomes
        print(p1)

        for session in sessions:
            print(session.get_choice(p1)[2], end=" ")

        print("")

        for session in sessions:
            print(session.get_choice(p2)[2], end=" ")

        print("")
        # TODO: display scores
        print(p2, end=" ")
