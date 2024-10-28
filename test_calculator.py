# test_calculator.py

import calculator

def test_add():
    assert calculator.add(1, 2) == 3

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(2, 3) == 6

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    try:
        calculator.divide(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
