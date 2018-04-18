import pytest
import random
import math

@pytest.fixture
def Log(tester):
    return tester.contracts('Log').deploy()

def all_permutations(max_val):
    if max_val <= 2:
        return [(1, 2)]
    
    this_level = [(max_val, b) for b in range(2, max_val)]
    next_level = all_permutations(max_val-1)
    this_level.extend(next_level)
    return this_level

test_cases = all_permutations(3)#2**127-1)

@pytest.mark.parametrize("a,b", test_cases)
def test_log(Log, a, b):
    result = math.floor(math.log(a, b))
    assert Log.log(a, b) == result
