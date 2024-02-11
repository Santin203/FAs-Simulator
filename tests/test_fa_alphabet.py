import pytest
from src.classes import *
#from classes import FA

@pytest.mark.parametrize("symbols", [
    [],
    ['a'],
    ['a', 'b', 'c'],
    ['a', 'b'],
    ['!', '@', '#'],
    [' ', '\t', '\n'],
    ['\n'],
])
    
def test_add_alphabet(symbols):
    fa = FA()
    fa.add_alphabet(symbols)
    assert fa.alphabet == symbols

