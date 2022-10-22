import pytest

# place this files inside tests/ directory
# test files must start with test_ or end with _test (e.g. test_sample.py)

"""
assertEqual(a, b)       Verify that a == b
assertNotEqual(a, b)    Verify that a != b
assertTrue(x)           Verify that x is True
assertFalse(x)          Verify that x is False
assertIn(item, list)    Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
"""

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
