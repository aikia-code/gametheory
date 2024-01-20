from random import choice

from .models import Session, Player, SimulationInfo
from .symbols import Choice, Score


class Simulation:
    def main(rounds: int = 50) -> None:
        sim_info = SimulationInfo(("tit4tat", "random"))

        for _ in range(rounds):
            session = Session(sim_info.names)

            # TODO: Strategies module with functions to handle execution, creation and storage of strategies
            # BEGIN STRATEGY

            # player A strategy is tit for tat
            try:
                if sim_info.sessions[-1].players[1].choice == Choice.DEFECT:
                    session.players[0].choose(Choice.DEFECT)
                else:
                    session.players[0].choose(Choice.COOPERATE)
            except IndexError:
                session.players[0].choose(Choice.COOPERATE)

            # player B strategy is to randomly choose responses
            player_choices = [Choice.COOPERATE, Choice.DEFECT]

            session.players[1].choose(choice(player_choices))

            # END STRATEGY

            session.compute_score()

            sim_info.sessions.append(session)

        # print out results for visual
        # TODO: Utility functions to handle pretty printing to console
        # TODO: Utility functions to handle writing results to file table[]
        # TODO: Simulation info Object designed to only display simulation outcomes

        print(sim_info)
