from random import choice

# Program library
from pdprogram.player import Player
from pdprogram.session import Session
from pdprogram.symbols import Choice, Score


class Simulation:
    def main(self, rounds: int = 200) -> None:
        
        # TODO: Simulation info object to store Simulation data like this: sessions list
        sessions = []

        p1 = "Tit for tat"
        p2 = "Random"

        for i in range(rounds):
            player_a, player_b = Player(p1), Player(p2)

            session = Session(player_a, player_b)

            # TODO: Strategies module with functions to handle execution, creation and storage of strategies
            # BEGIN STRATEGY

            # player A strategy is tit for tat
            # =======================================>
            try:
                if sessions[-1].get_choice(p2) == Choice.DEFECT:
                    player_a.choose(Choice.DEFECT)
                else:
                    player_a.choose(Choice.COOPORATE)
            except IndexError:
                player_a.choose(Choice.COOPORATE)

            # player B strategy is to randomly choose responses
            # ========================================>
            gamechoices = [Choice.COOPORATE, Choice.DEFECT]

            player_b.choose(choice(gamechoices))

            # END STRATEGY

            # session score computation
            session.compute_score()

            # record session data
            sessions.append(session)

        # print out results for visual
        # TODO: Utility functions to handle pretty printing to console
        # TODO: Utility functions to handle writing results to file
        # TODO: Simulation info Object designed to only display simualtion outcomes
        print(p1)

        for sess in sessions:
            print(sess.get_choice(p1)[2], end=" ")

        print("")

        for sess in sessions:
            print(sess.get_choice(p2)[2], end=" ")

        print("")
        # TODO: display scores
        print(p2, end=" ")
