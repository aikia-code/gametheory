from .models import Session, Player, SimulationInfo
from .symbols import Action, Payoff
from .strategy import random_action, always_cooperate


class Simulation:
    def main(rounds: int = 50) -> None:
        sim_info = SimulationInfo()

        for _ in range(rounds):
            session = Session(names=("tit4tat", "rand"))

            session.players[0].respond(strategy=always_cooperate)

            session.players[1].respond(strategy=random_action)

            session.compute_score()

            sim_info.history.append(session)

        print(sim_info)
