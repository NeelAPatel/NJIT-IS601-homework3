"""Module for testing calculator operations.

This module tests the basic operations provided by the calculator.operations module,
ensuring that addition, subtraction, multiplication, and division work correctly.
"""

from calculator.operations import add, multiply, subtract, divide
def test_addition():
    '''Test 'addition' operation itself '''
    assert add(2,2) == 4

def test_subtraction():
    '''Test 'subtraction' operation itself '''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test 'multiplication' operation itself '''
    assert multiply(2,2) == 4

def test_division():
    '''Test 'division' operation itself '''
    assert divide(2,2) == 1
    