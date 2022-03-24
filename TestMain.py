from main import *
import random
import pytest

@pytest.fixture
def input_values():
    #input = 39
    random.seed(9999)
    # Return 10 integers between 1-100
    random_ints = random.sample(range(1, random.randint(2, 100)), 10)
    return [(x, 2, x + 2) for x in random_ints]

def test_add_two(input_values):
    for x in input_values:
        assert(x[0] + x[1] == x[2])