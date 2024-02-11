"""Calculator Testing
This file tests if calculator.__init__.py works properly, one layer above operations
Tests if my Calculator item is calling and operating the correct functions when called"""
from calculator import Calculator

def test_addition():
    '''Test 'addition' func result '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test 'subtraction' func result '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test 'multiply' func result '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test 'divide' func result '''    
    assert Calculator.divide(2,2) == 1
