# How to write property testing
def add(a, b):
    return a + b

# Basic test
def test_add_basic():
    # Check as the same system add
    assert add(23, 3) == 23 + 3
    # Check that order doesn't matter
    assert add(23, 3) == add(3, 23)

# 