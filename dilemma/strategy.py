from .symbols import Action


def random_action(history, opponent):
    from random import choice

    player_choices = [Action.COOPERATE, Action.DEFECT]

    return choice(player_choices)


def always_cooperate(history, opponent):
    return Action.COOPERATE
