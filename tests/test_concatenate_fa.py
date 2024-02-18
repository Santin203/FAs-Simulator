from src.functions import *
from src.classes import *

def test_concatenate_fa():
    # Create the first FA
    fa1 = FA()
    fa1.add_alphabet(['a', 'b'])
    fa1.add_states(['q0', 'q1'])
    fa1.set_start_state('q0')
    fa1.set_accept_states(['q1'])
    fa1.add_transition([{"state": 'q0', "input": 'a', "next_state": 'q1'}])
    
    # Create the second FA
    fa2 = FA()
    fa2.add_alphabet(['b', 'c'])
    fa2.add_states(['q2', 'q3'])
    fa2.set_start_state('q2')
    fa2.set_accept_states(['q3'])
    fa2.add_transition([{"state": 'q2', "input": 'b', "next_state": 'q3'}])
    
    # Concatenate the FAs
    fa = concatenate_fa(fa1, fa2)
    
    # Check the concatenated FA properties
    assert fa.alphabet == ['a', "<EPSILON>", 'b', 'c']
    assert fa.states == ['q0', 'q1', 'q2', 'q3']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q1', 'q3']
    assert fa.transitions == [
        {"state": 'q0', "input": 'a', "next_state": 'q1'},
        {'state': 'q1', 'input': '<EPSILON>', 'next_state': 'q2'},
        {"state": 'q2', "input": 'b', "next_state": 'q3'}
    ]
    
    fa1 = FA()
    fa1.add_alphabet(['1'])
    fa1.add_states(['q0'])
    fa1.set_start_state('q0')
    fa1.set_accept_states(['q0'])
    fa1.add_transition([{"state": 'q0', "input": '1', "next_state": 'q0'}])
    
    fa2 = FA()
    fa2.add_alphabet(['0'])
    fa2.add_states(['q1', 'q2'])
    fa2.set_start_state('q1')
    fa2.set_accept_states(['q2'])
    fa2.add_transition([{"state": 'q1', "input": '0', "next_state": 'q2'},
                        {"state": 'q2', "input": '0', "next_state": 'q2'}
                        ])
    
    fa = concatenate_fa(fa1, fa2)
    
    assert fa.alphabet == ['1', "<EPSILON>", '0']
    assert fa.states == ['q0', 'q1', 'q2']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q0', 'q2']
    assert fa.transitions == [
        {"state": 'q0', "input": '1', "next_state": 'q0'},
        {'state': 'q0', 'input': '<EPSILON>', 'next_state': 'q1'},
        {"state": 'q1', "input": '0', "next_state": 'q2'},
        {"state": 'q2', "input": '0', "next_state": 'q2'}
    ]
    
def test_concatenate_fa_empty():
    # Create an empty FA
    fa1 = FA()
    
    # Create a non-empty FA
    fa2 = FA()
    fa2.add_alphabet(['a'])
    fa2.add_states(['q0'])
    fa2.set_start_state('q0')
    fa2.set_accept_states(['q0'])
    
    # Concatenate the FAs
    fa = concatenate_fa(fa1, fa2)
    
    # Check the concatenated FA properties
    assert fa.alphabet == ['a']
    assert fa.states == ['q0']
    assert fa.start_state == 'q0'
    assert fa.accept_states == ['q0']
    assert fa.transitions == []
