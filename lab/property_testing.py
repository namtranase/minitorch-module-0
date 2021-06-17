# How to write property testing
def add(a, b):
    return a + b

# Basic test
def test_add_basic():
    # Check as the same system add
    assert add(23, 3) == 23 + 3
    # Check that order doesn't matter
    assert add(23, 3) == add(3, 23)

# Naive test
def test_add_naive():
    for a in range(-10000, 10000):
        for b in range(-10000, 10000):
            assert add(a, b) == a + b
            assert add(a, b) == add(b, a)

# Using hypothesis lib
from hypothesis.strategies import integers
from hypothesis import given
@given(integers(), integers())
def test_add(a, b):
    # Check same as slow system add
    assert add(a, b) == a + b
    assert add(b, b) == add(b, a)