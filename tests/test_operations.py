"""Module for testing the Operations Itself

This module tests the basic operations provided by the calculator.operations module,
ensuring that addition, subtraction, multiplication, and division work correctly.
"""

from decimal import Decimal

import pytest
from calculator.calculation import Calculation
from calculator.operations import add, multiply, subtract, divide

def test_operation_addition():
    '''Test 'addition' operation itself '''
    myCalc = Calculation(Decimal('20'), Decimal('5'), add )
    assert myCalc.perform() == Decimal('25')

def test_operation_subtraction():
    '''Test 'subtraction' operation itself '''
    myCalc = Calculation(Decimal('20'), Decimal('5'), subtract )
    assert myCalc.perform() == Decimal('15')

def test_operation_multiplication():
    '''Test 'multiplication' operation itself '''
    myCalc = Calculation(Decimal('20'), Decimal('5'), multiply )
    assert myCalc.perform() == Decimal('100')

def test_operation_division():
    '''Test 'division' operation itself '''
    myCalc = Calculation(Decimal('20'), Decimal('5'), divide )
    assert myCalc.perform() == Decimal('4')

def test_div_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        myCalc = Calculation(Decimal('10'), Decimal('0'), divide)
        myCalc.perform()
    