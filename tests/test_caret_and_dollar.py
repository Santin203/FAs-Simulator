import pytest
from src.classes import *

def test_caret_and_dollar_fa_empty_regex():
    regex = ""
    fa = FA()
    caret_and_dollar_fa(regex, fa)
    assert fa.alphabet == []
    assert fa.start_state == ''
    assert fa.accept_states == []
    assert fa.transitions == []

def test_caret_and_dollar_fa_single_symbol():
    regex = "a"
    fa = FA()
    caret_and_dollar_fa(regex, fa)
    assert fa.alphabet == ['a']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q1']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"}
    ]

def test_caret_and_dollar_fa_multiple_symbols():
    regex = "abc"
    fa = FA()
    caret_and_dollar_fa(regex, fa)
    assert fa.alphabet == ['a', 'b', 'c']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q3']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "c", "next_state": "q3"}
    ]
    
def test_add_symbol_to_alphabet_not_in_regex_or_fa_alphabet():
    regex = "abc"
    fa = FA()
    caret_and_dollar_fa(regex, fa)
    assert fa.alphabet == ['a', 'b', 'c']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q3']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "c", "next_state": "q3"}
    ]
    fa.add_alphabet("d")
    assert fa.alphabet == ['a', 'b', 'c', 'd']