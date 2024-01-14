from random import choice

# Program library
from pdprogram.pdplayer import Player
from pdprogram.pdsession import Session
from pdprogram.pdtypes import Choice, Score

"""
GameLoop:
    - sessions
    - rounds
    - get final scores -> dict [player name, player total score]
    - show scores
    - run loop
"""


class GameLoop:
    def __init__(self) -> None:
        self.sessions = []

    def run(self, rounds: int) -> None:
        player_a, player_b = Player("Tit for tat"), Player("Random")

        session = Session(player_a, player_b)

        for i in range(rounds):
            # player A strategy is tit for tat
            try:
                if self.sessions[-1].get_player_choice(player_b) == Choice.DEFECT:
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

            # record session data
            self.sessions.append(session)

    def get_final_scores(self) -> dict:
        pass

    def show_final_scores(self) -> str:
        pass
