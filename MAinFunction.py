# Choose an arithmetic oprearation 
def add(x, y):
    """Returns the sum two numbers."""
    return x+y

def subtract(x, y):
    """Returns the diffrence between two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x* y

def divide(x, y):
    """Returns the quotient of two numbers. Raise zeroDivisionError if the division is zero. """
    if y == 0:
        raise ValueError ("Cannot divide by Zero. ")
    return x / y
