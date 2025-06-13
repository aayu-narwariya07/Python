# creating a list
fruits = ["apple", "banana", "cherry","mango", "orange"]
print("original list:", fruits)
# accessing element in a list
first_fruit = fruits [0]
last_fruit = fruits[-1]
print("frist fruit:", first_fruit)
print("last fruit:", last_fruit)

# slicing a list
sublist_fruits = fruits[:4]
print("sublist of first three fruits:", sublist_fruits)

# adding element of a list
fruits.append("grape")
print("list after adding 'grape':", fruits)
# remove element
fruits.remove("banana")
print(fruits)
# pop element
fruits.pop()
print(fruits)

# finding the length of list
length=len(fruits)
print("number of fruits in the list:",length )

# checking membership in a list 
is_in_list = "banana" in fruits
print("Is 'banana' in the list?", is_in_list)

# inserting element 
fruits.insert(1,"pineapple")
print("list after inserting 'pineapple' at position 1:", fruits)

# iterating over a list
print("iterating over the list: ")
for fruit in fruits:
    print(fruit)

# sorting a list
fruits.sort()
print("list after a sorting rearge:", fruits)

# reversing a list
fruits.reverse()
print("list after reversing the order:", fruits)
# list comprehension
long_fruits = [fruit for fruit in fruits if len(fruit) >5]
print("fruits with more than 5 letter", long_fruits)
# copying a list
fruits_copy = fruits.copy()
print("copied list:",fruits_copy)
# clearing a list
fruits.clear()
print("list after clearing all element:", fruits)
# extending a list with another list
vegetables =["carrot", "broccoli", "spinach"]
fruits_copy.extend(vegetables)
print("list after extending with vegetables:", fruits_copy)
# counting occurrence of an elementin a list
num_apple = fruits_copy.count("apple")
print("number of 'apple' in the list:", num_apple)
# finding the index element
if "carrot" in fruits_copy:
    carrot_index = fruits_copy.index("carrot")
    print("Index of 'carrot':",carrot_index)
# removing element
if len(fruits_copy)> 2:
    del fruits_copy[2]
print("list after removing element at index 2:", fruits_copy)
# nested lists
nested_list = [fruits_copy, vegetables]
print("nested list:", nested_list)
