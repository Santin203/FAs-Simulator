import pytest
from src.classes import *

def test_valid_start_state():
    fa = FA()
    fa.set_start_state("q1")
    assert fa.start_state == "q1"

def test_update_start_state():
    fa = FA()
    fa.set_start_state("q0")
    fa.set_start_state("q2")
    assert fa.start_state == "q2"

def test_first_state_start_state():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.set_start_state(fa.states[0])
    assert fa.start_state == "q0"

def test_none_start_state():
    fa = FA()
    fa.set_start_state(None)
    assert fa.start_state is None

def test_empty_string_start_state():
    fa = FA()
    fa.set_start_state("")
    assert fa.start_state == ""