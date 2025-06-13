#  Positional Arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years  old.")
greet ("Aarti", 19)
# Keyword Argument
def greet(name, age):
    print(f"hello {name}, you are {age} years old")
greet( age = 30, name = "Aarti")
#  default arguments
def greet (name, age= 25):
    print(f"Hello {name}, you are {age} years old")
greet("Ramar")
greet("Aarti", 23)
# variable-lenth arguments
def print_number(*args):
    for number in args:
        print(number)
print_number(1, 2, 3, 4, 5)
# keyword variable-length argument
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Aarti", profession = "Engineer")
print_info(country= "Indai", population = 1.4e9, capita1 = "New Delhi")
# mixing different argument types
def mixed_argument(a, b=2, *args, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print("args:", args)
    print("kwargs:", kwargs)

mixed_argument(1, 2, 3, 4, 5, x =10, y=20)
