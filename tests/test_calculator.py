'''test cases for calculator'''
from calculator import add, substract, multiply, divide
def test_add():
    '''test addition function'''
    assert add(2, 2) == 4

def test_substraction():
    '''test subsraction function'''
    assert substract(5, 2) == 3

def test_multiplication():
    '''test multiplication function'''
    assert multiply(2, 4) == 8

def test_division():
    '''test division function'''
    assert divide(10, 2) == 5
