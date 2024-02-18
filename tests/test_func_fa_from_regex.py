import pytest
from src.functions import *
from src.classes import *

@pytest.fixture
def fa():
    return FA()

@pytest.mark.parametrize("regex, data", [
    ("a", {
        "states": ["q0", "q1"],
        "alphabet": ["a"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"}
        ],
        "start_state": "q0",
        "accept_states": ["q1"]
    }),
    ("b", {
        "states": ["q0", "q1"],
        "alphabet": ["b"],
        "delta": [
            {"state": "q0", "input": "b", "next_state": "q1"}
        ],
        "start_state": "q0",
        "accept_states": ["q1"]
    }),
    ("ab", {
        "states": ["q0", "q1", "q2"],
        "alphabet": ["a", "b"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "b", "next_state": "q2"}
        ],
        "start_state": "q0",
        "accept_states": ["q2"]
    }),
    ("a*", {
        "states": ["q0"],
        "alphabet": ["a"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q0"}
        ],
        "start_state": "q0",
        "accept_states": ["q0"]
    }),
    ("a+", {
        "states": ["q0", "q1"],
        "alphabet": ["a"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "a", "next_state": "q1"}
        ],
        "start_state": "q0",
        "accept_states": ["q1"]
    }),
    ("a?", {
        "states": ["q0", "q1"],
        "alphabet": ["a"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"}
        ],
        "start_state": "q0",
        "accept_states": ["q0", "q1"]
    }),
    ("ab*", {
        "states": ["q0", "q1", "a0"],
        "alphabet": ["a", "<EPSILON>", "b"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "<EPSILON>", "next_state": "a0"},
            {"state": "a0", "input": "b", "next_state": "a0"}
        ],
        "start_state": "q0",
        "accept_states": ["q1", "a0"]
    }),
    ("^ABC(01001)*09$", {
        "states": ["q0", "q1", "q2", "q3", "a0", "a1", "a2", "a3", "a4", "b0", "b1", "b2"],
        "alphabet": ["A", "<EPSILON>", "B", "C", "0", "1", "9"],
        "delta": [
            {"state": "q0", "input": "A", "next_state": "q1"},
            {"state": "q1", "input": "B", "next_state": "q2"},
            {"state": "q2", "input": "C", "next_state": "q3"},
            {"state": "q3", "input": "<EPSILON>", "next_state": "a0"},
            {"state": "a0", "input": "0", "next_state": "a1"},
            {"state": "a1", "input": "1", "next_state": "a2"},
            {"state": "a2", "input": "0", "next_state": "a3"},
            {"state": "a3", "input": "0", "next_state": "a4"},
            {"state": "a4", "input": "1", "next_state": "a0"},
            {"state": "q3", "input": "<EPSILON>", "next_state": "b0"},
            {"state": "a0", "input": "<EPSILON>", "next_state": "b0"},
            {"state": "b0", "input": "0", "next_state": "b1"},
            {"state": "b1", "input": "9", "next_state": "b2"}
        ],
        "start_state": "q0",
        "accept_states": ["q3", "a0", "b2"]
    }),
    ("0?1+", {
        "states": ["q0", "q1", "a0", "a1"],
        "alphabet": ["0","<EPSILON>", "1"],
        "delta": [
            {"state": "q0", "input": "0", "next_state": "q1"},
            {"state": "q0", "input": "<EPSILON>", "next_state": "a0"},
            {"state": "q1", "input": "<EPSILON>", "next_state": "a0"},
            {"state": "a0", "input": "1", "next_state": "a1"},
            {"state": "a1", "input": "1", "next_state": "a1"}
        ],
        "start_state": "q0",
        "accept_states": ["q0", "q1", "a1"]
    }),
    ("01*", {
        "states": ["q0", "q1", "a0"],
        "alphabet": ["0", "<EPSILON>", "1"],
        "delta": [
            {"state": "q0", "input": "0", "next_state": "q1"},
            {"state": "q1", "input": "<EPSILON>", "next_state": "a0"},
            {"state": "a0", "input": "1", "next_state": "a0"}
        ],
        "start_state": "q0",
        "accept_states": ["q1", "a0"]
    }),
    ("(ab)*", {
        "states": ["q0", "q1"],
        "alphabet": ["a", "b"],
        "delta": [
            {"state": "q0", "input": "a", "next_state": "q1"},
            {"state": "q1", "input": "b", "next_state": "q0"}
        ],
        "start_state": "q0",
        "accept_states": ["q0"]
    }),
])

def test_single_symbol_regex_fixed(regex, data):
    fa = FA()
    fa = fa_from_regex(regex)
    assert fa.alphabet == data["alphabet"]
    assert fa.states == data["states"]
    assert fa.start_state == data["start_state"]
    assert fa.accept_states == data["accept_states"]
    assert fa.transitions == data["delta"]