from random import choice

# Program library
from pdprogram.pdplayer import Player
from pdprogram.pdsession import Session
from pdprogram.pdsymbols import Choice, Score

"""
GameLoop:
    - sessions
    - rounds
    - get final scores -> dict [player name, player total score]
    - show scores
    - run loop
"""


class GameLoop:
    def run(self, rounds: int) -> None:
        sessions = []

        p1 = "Tit for tat"
        p2 = "Random"

        for i in range(rounds):
            player_a, player_b = Player(p1), Player(p2)

            session = Session(player_a, player_b)

            # player A strategy is tit for tat
            try:
                if sessions[-1].get_player_choice(p2) == Choice.DEFECT:
                    player_a.choose(Choice.DEFECT)
                else:
                    player_a.choose(Choice.COOPORATE)
            except IndexError:
                player_a.choose(Choice.COOPORATE)

            # player B strategy is to randomly choose responses
            gamechoices = [Choice.COOPORATE, Choice.DEFECT]

            player_b.choose(choice(gamechoices))

            # session computation
            session.compute_score()

            # print(session.get_choices())

            # record session data
            sessions.append(session)

        print(p1)

        for sess in sessions:
            print(sess.get_player_choice(p1)[2], end=" ")

        print("")

        for sess in sessions:
            print(sess.get_player_choice(p2)[2], end=" ")

        print("")

        print(p2, end=" ")

    def get_final_scores(self) -> dict:
        pass

    def show_final_scores(self) -> str:
        pass
