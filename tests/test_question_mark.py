import pytest
from src.classes import *

def test_question_mark_fa_empty_regex():
    regex = ""
    fa = FA()
    question_mark_fa(regex, fa)
    assert fa.alphabet == []
    assert fa.start_state == ''
    assert fa.accept_states == []
    assert fa.transitions == []

def test_question_mark_fa_single_symbol():
    regex = "a"
    fa = FA()
    question_mark_fa(regex, fa)
    assert fa.alphabet == ['a']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q0','q1']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"}
    ]

def test_question_mark_fa_multiple_symbols():
    regex = "abc"
    fa = FA()
    question_mark_fa(regex, fa)
    assert fa.alphabet == ['a', 'b', 'c']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q0', 'q3']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "c", "next_state": "q3"}
    ]

def test_question_mark_fa_regex_with_symbols():
    regex = "a?b?c?"
    fa = FA()
    question_mark_fa(regex, fa)
    assert fa.alphabet == ['a', 'b', 'c']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q0', 'q3']
    assert fa.transitions == [
        {"state": "q0", "input": "a", "next_state": "q1"},
        {"state": "q1", "input": "b", "next_state": "q2"},
        {"state": "q2", "input": "c", "next_state": "q3"}
    ]
