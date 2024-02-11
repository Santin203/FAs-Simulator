import pytest
from src.classes import *

@pytest.mark.parametrize("states", [
    [],
    ["q0"],
    ["q0", "q1", "q2"],
    ["state1", "state2", "state3"],
    ["q0", "q1", "q0"],
    ["q" + "a" * 1000],
    [123],
])

# Add states to the DFA
def test_add_states(states):
    fa = FA()
    fa.add_states(states)
    assert fa.states == states