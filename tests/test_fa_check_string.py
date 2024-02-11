import pytest
from src.classes import *

def test_check_string_empty():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1", "<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"1","next_state":"q1"},
        {"state":"q1","input":"0","next_state":"q2"},
        {"state":"q2","input":"<EPSILON>","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states(["q0"])
    assert fa.check_string(fa.start_state,"") == False

def test_check_string_accepted():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1", "<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"1","next_state":"q1"},
        {"state":"q1","input":"0","next_state":"q2"},
        {"state":"q2","input":"<EPSILON>","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q0")
    assert fa.check_string(fa.start_state,"10") == True

def test_check_string_not_accepted():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1", "<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"1","next_state":"q1"},
        {"state":"q1","input":"0","next_state":"q2"},
        {"state":"q2","input":"<EPSILON>","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q0")
    assert fa.check_string(fa.start_state,"01") == False

def test_check_string_invalid_symbol():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1", "<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"1","next_state":"q1"},
        {"state":"q1","input":"0","next_state":"q2"},
        {"state":"q2","input":"<EPSILON>","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q0")
    assert fa.check_string(fa.start_state,"11") == False

def test_check_string_epsilon_transition():
    fa = FA()
    fa.add_states(["q0", "q1"])
    fa.add_alphabet(["<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"<EPSILON>","next_state":"q1"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q1")
    assert fa.check_string(fa.start_state,"") == True

def test_check_string_multiple_epsilon_transitions():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1", "<EPSILON>"])
    fa.add_transition([
        {"state":"q0","input":"1","next_state":"q1"},
        {"state":"q1","input":"<EPSILON>","next_state":"q2"},
        {"state":"q2","input":"<EPSILON>","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q0")
    assert fa.check_string(fa.start_state,"1") == True
    
def test_no_transition():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1"])
    fa.add_transition([
        {"state":"q0","input":"0","next_state":"q1"},
        {"state":"q1","input":"1","next_state":"q2"},
        {"state":"q2","input":"0","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q2")
    assert fa.check_string(fa.start_state, "1") == False

def test_no_path_to_accept_state():
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1"])
    fa.add_transition([
        {"state":"q0","input":"0","next_state":"q1"},
        {"state":"q1","input":"1","next_state":"q0"},
        {"state":"q1","input":"0","next_state":"q1"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q2")
    assert fa.check_string(fa.start_state, "010") == False
    
def test_symbols_not_in_alphabet(capsys):
    fa = FA()
    fa.add_states(["q0", "q1", "q2"])
    fa.add_alphabet(["0", "1"])
    fa.add_transition([
        {"state":"q0","input":"0","next_state":"q1"},
        {"state":"q1","input":"1","next_state":"q2"},
        {"state":"q2","input":"0","next_state":"q0"}
    ])
    fa.set_start_state("q0")
    fa.set_accept_states("q2")
    assert fa.check_string(fa.start_state, "2") == False
    captured = capsys.readouterr()
    assert captured.out == "Symbol 2 is not in the alphabet\n"