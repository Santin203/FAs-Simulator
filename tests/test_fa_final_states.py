import pytest
from src.classes import *
import pytest
from src.classes import FA

@pytest.mark.parametrize("accept_states", [
    ["q2"],
    ["q1", "q2"],
])

def test_set_accept_states(accept_states):
    fa = FA()
    fa.set_accept_states(accept_states)
    assert fa.accept_states == accept_states
