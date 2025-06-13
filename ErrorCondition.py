#  Implement the ZeroDivisionError, ValuError, IndexError, and KeyError.
import os
def divide_numbers(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allpwed."
def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index is out of range. "
def get_dict_value(dct, key):
    try:
        return dct[key]
    except KeyError:
        return "Error: key not found in dictionary. "
def convert_to_integer(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Cannot convert value to integer."
    except TypeError:
        return "Error: Invalid type for conversion. "
    
# Demontration of different exceptions

print("Division Example: ")
print(divide_numbers(10, 0))

print("\nList Access Example: ")
my_list = [1, 2, 3]
print(access_list_element(my_list, 5))

print("\nDictionary Access Example: ")
my_dict = {"a": 1, "b": 2}
print(get_dict_value(my_dict, 'c'))

print("\nInteger Conversion Example: ")
print(convert_to_integer('123abc'))
print(convert_to_integer(123.45))
