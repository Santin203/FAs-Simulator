import pytest
from src.classes import *

def test_start_state_in_states():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["a", "b"])
    fa.add_transition([
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "a", "next_state": "q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == True

def test_transitions_in_states_and_alphabet():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["a", "b"])
    fa.add_transition([
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "a", "next_state": "q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == True

def test_accept_states_in_states():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["a", "b"])
    fa.add_transition([
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "a", "next_state": "q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == True

def test_no_states():
    fa = FA()
    fa.add_alphabet(["a", "b"])
    fa.add_transition([
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "a", "next_state": "q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == False

def test_no_alphabet():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_transition([
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "a", "next_state": "q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == False

def test_no_transitions():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["a", "b"])
    fa.set_start_state("q0")
    fa.set_accept_states(["q2"])

    assert fa.check_fa_consistency() == True