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
    {
        "states":["q0","q1","q2","q3"],
        "alphabet":["0","1"],
        "delta":[
            {"state":"q0","input":"1","next_state":"q1"},
            {"state":"q1","input":"0","next_state":"q3"},
            {"state":"q3","input":"1","next_state":"q2"},
            {"state":"q2","input":"0","next_state":"q0"},
            {"state":"q1","input":"1","next_state":"q0"},
            {"state":"q3","input":"0","next_state":"q1"},
            {"state":"q2","input":"1","next_state":"q3"},
            {"state":"q0","input":"0","next_state":"q2"}
        ],
        "start_state":"q0",
        "accept_states":["q3"]
    },
    {
        "states": ["q0", "q1", "q2"],
        "alphabet": ["0", "1", "<EPSILON>"],
        "delta": [
        { "state": "q0", "input": "0", "next_state": "q1" },
        { "state": "q0", "input": "1", "next_state": "q0" },
        { "state": "q0", "input": "<EPSILON>", "next_state": "q2" },
        { "state": "q1", "input": "0", "next_state": "q2" },
        { "state": "q1", "input": "1", "next_state": "q0" },
        { "state": "q2", "input": "0", "next_state": "q2" },
        { "state": "q2", "input": "1", "next_state": "q2" }
        ],
        "start_state": "q0",
        "accept_states": ["q2"]
    },
    {
        "states": [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5"
        ],
        "alphabet": [
        "1",
        "0"
        ],
        "delta": [
        {
            "state": "2",
            "input": "0",
            "next_state": "2"
        },
        {
            "state": "3",
            "input": "0",
            "next_state": "3"
        },
        {
            "state": "2",
            "input": "1",
            "next_state": "2"
        },
        {
            "state": "5",
            "input": "1",
            "next_state": "5"
        },
        {
            "state": "4",
            "input": "0",
            "next_state": "5"
        },
        {
            "state": "5",
            "input": "0",
            "next_state": "4"
        },
        {
            "state": "0",
            "input": "1",
            "next_state": "4"
        },
        {
            "state": "0",
            "input": "0",
            "next_state": "1"
        },
        {
            "state": "1",
            "input": "0",
            "next_state": "2"
        },
        {
            "state": "1",
            "input": "1",
            "next_state": "2"
        },
        {
            "state": "3",
            "input": "1",
            "next_state": "4"
        },
        {
            "state": "4",
            "input": "1",
            "next_state": "3"
        }
        ],
        "start_state": "0",
        "accept_states": [
        "1",
        "3"
        ]
    }
    
])

def test_create_fa_json(data, fa):

    result = create_fa_json(data, fa)

    assert result.states == data["states"]
    assert result.alphabet == data["alphabet"]
    assert result.transitions == data["delta"]
    assert result.start_state == data["start_state"]
    assert result.accept_states == data["accept_states"]