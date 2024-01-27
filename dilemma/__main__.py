r"""module entry point
"""

from .simulation import simulate_strategies
from .strategies import always_cooperate, always_defect

simulation = simulate_strategies(
    slot1=always_cooperate, slot2=always_defect, rounds=100
)

print(simulation)
