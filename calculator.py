# calculator.py

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers. Raises a ZeroDivisionError if y is zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def square(x):
    """Square a number."""
    return x * x
