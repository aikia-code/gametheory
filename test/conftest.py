"""Pytest fixtures    """

import pytest
from dilemma.models import Player, Session, Simulation

from dilemma.strategies import AlwaysCooperate, AlwaysDefect


@pytest.fixture
def strategy1():
    """Strategy 1"""
    return AlwaysCooperate([])


@pytest.fixture
def strategy2():
    """Strategy 2"""
    return AlwaysDefect([])


@pytest.fixture
def simulation():
    """New simulation"""
    return Simulation()


@pytest.fixture
def player_inst():
    """Player instance"""
    return Player("test_player")


@pytest.fixture
def session_inst():
    """Session instance"""
    return Session(names=["sand", "bite"])
