# create a simple Calculations

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference between two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the qoutient of two numbers. Raises Zerodivision if the divisor is zero"""
    if y == 0:
        raise ValueError
    return x / y
