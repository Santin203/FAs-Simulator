import pytest
from src.classes import *

@pytest.mark.parametrize("delta, expected_length", [
        ([{"state": "q0", "input": "a", "next_state": "q1"}], 1),
        ([{"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "b", "next_state": "q2"},
            {"state": "q2", "input": "c", "next_state": "q3"}], 3),
        ([{"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "a", "next_state": "q2"},
            {"state": "q2", "input": "a", "next_state": "q3"},
            {"state": "q3", "input": "a", "next_state": "q4"}], 4),
        ([{"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "b", "next_state": "q2"},
            {"state": "q2", "input": "c", "next_state": "q3"},
            {"state": "q3", "input": "d", "next_state": "q4"},
            {"state": "q4", "input": "e", "next_state": "q5"}], 5)
])
def test_add_transitions(delta, expected_length):
        # Initialize the FA
        fa = FA()

        # Add the transitions to the DFA
        fa.add_transition(delta)

        # Check if the transitions were added correctly
        assert len(fa.transitions) == expected_length
        assert fa.transitions == delta
