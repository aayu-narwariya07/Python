#  Function to add two numbers
num1 = 10
num2 = 5
def add (a, b):
    result = a + b
    return result
print(add(num1, num2))
# Function to subtract two numbers
def subtraction(a,  b):
    result = a - b
    return result
print("subtraction:",num1- num2 )
# Function to multipiy two numbers
def multiply(a, b):
    result = a * b
    return  result
print("multipiy:", num1 * num2)
# Function to divide two numbers
def divide(a, b):
    if b != 0:
      result = a / b
    else:
      result = "cannot divide by zero"
    return result
print("Division :",divide(num1, num2)  )
