'''Testing Calculator'''
from calculator import add, subtract, multiply, divide, remainder

def test_addition():
    '''Test if add works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test if minus works '''    
    assert subtract(2,2) == 0

def test_multiply():
    '''Test if multiply works '''
    assert multiply(2,2) == 4

def test_divide():
    '''Test if divide works '''    
    assert divide(2,2) == 1

def test_remainder():
    '''Test if remainder works '''    
    assert remainder(2,2) == 0
    