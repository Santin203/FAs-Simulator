import pytest
from src.functions import *
from src.classes import *

@pytest.fixture
def fa():
    return FA()

@pytest.mark.parametrize("data", [
    {
        "states":["q0","q1","q2"],
        "alphabet":["0","1","<EPSILON>"],
        "delta":[
            {"state":"q0","input":"1","next_state":"q1"},
            {"state":"q1","input":"0","next_state":"q2"},
            {"state":"q2","input":"<EPSILON>","next_state":"q0"}

        ],
        "start_state":"q0",
        "accept_states":["q0"]
    },
])

def test_create_fa_json(data, fa):

    result = create_fa_json(data, fa)

    assert result.states == data["states"]
    assert result.alphabet == data["alphabet"]
    assert result.transitions == data["delta"]
    assert result.start_state == data["start_state"]
    assert result.accept_states == data["accept_states"]