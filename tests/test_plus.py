import pytest
from src.classes import *

def test_plus_single_symbol():
    regex = "b+"
    fa = FA()
    plus_fa(regex, fa)
    assert fa.alphabet == ['b']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q1']
    assert fa.transitions == [
        {"state": "q0", "input": "b", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q1"}
    ]
def test_plus_fa_empty_regex():
    regex = ""
    fa = FA()
    plus_fa(regex, fa)
    assert fa.alphabet == []
    assert fa.start_state == ''
    assert fa.accept_states == []
    assert fa.transitions == []

def test_plus_fa_multiple_characters():
    regex = "abc"
    fa = FA()
    plus_fa(regex, fa)
    assert fa.alphabet == ['a', 'b', 'c']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q3']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "c", "next_state": "q3"},
        {"state": "q3", "input": "a", "next_state": "q1"}
    ]
