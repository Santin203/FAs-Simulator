import pytest
from src.classes import *

def test_copy_all_attributes():
    fa1 = FA()
    fa1.add_states(["q0", "q1", "q2"])
    fa1.add_alphabet(["a", "b"])
    fa1.add_transition([{"state": "q0", "input": "a", "next_state": "q1"},
                        {"state": "q1", "input": "b", "next_state": "q2"}])
    fa1.set_start_state("q0")
    fa1.set_accept_states(["q2"])

    fa2 = FA()
    fa2.copy_fa(fa1)

    assert fa2.states == fa1.states
    assert fa2.alphabet == fa1.alphabet
    assert fa2.transitions == fa1.transitions
    assert fa2.start_state == fa1.start_state
    assert fa2.accept_states == fa1.accept_states

def test_return_value():
    fa1 = FA()
    fa1.add_states(["q0", "q1", "q2"])
    fa1.add_alphabet(["a", "b"])
    fa1.add_transition([{"state": "q0", "input": "a", "next_state": "q1"},
                        {"state": "q1", "input": "b", "next_state": "q2"}])
    fa1.set_start_state("q0")
    fa1.set_accept_states(["q2"])

    fa2 = FA()
    return_value = fa2.copy_fa(fa1)

    assert return_value is None

def test_copy_empty_fa():
    fa1 = FA()

    fa2 = FA()
    fa2.copy_fa(fa1)

    assert fa2.states == []
    assert fa2.alphabet == []
    assert fa2.transitions == []
    assert fa2.start_state == ""
    assert fa2.accept_states == []

def test_copy_fa_no_states():
    fa1 = FA()
    fa1.add_alphabet(["a", "b"])
    fa1.add_transition([{"state": "", "input": "a", "next_state": ""}])
    fa1.set_start_state("")
    fa1.set_accept_states("")

    fa2 = FA()
    fa2.copy_fa(fa1)

    assert fa2.states == []
    assert fa2.alphabet == ["a", "b"]
    assert fa2.transitions == [{"state": "", "input": "a", "next_state": ""}]
    assert fa2.start_state == ""
    assert fa2.accept_states == []

def test_copy_fa_no_alphabet():
    fa1 = FA()
    fa1.add_states(["q0", "q1", "q2"])
    fa1.add_transition([{"state": "q0", "input": "", "next_state": "q1"}])
    fa1.set_start_state("q0")
    fa1.set_accept_states(["q2"])

    fa2 = FA()
    fa2.copy_fa(fa1)

    assert fa2.states == ["q0", "q1", "q2"]
    assert fa2.alphabet == []
    assert fa2.transitions == [{"state": "q0", "input": "", "next_state": "q1"}]
    assert fa2.start_state == "q0"
    assert fa2.accept_states == ["q2"]