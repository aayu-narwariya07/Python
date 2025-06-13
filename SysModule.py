# sys modules
import sys

# print python version
print("python version:", sys.version)

# print system platform
print("platfrom:", sys.platform)

# print command line argument
print("Commend line argument:", sys.argv)

# random module
import random

print("Random integer between 1 and 10:", random.randint(1, 10))
# random floating point number between 0 and 1
print("Random float between 0 and 1:", random.random())
# random choice from a list
items = ['apple', 'banana', 'cherry']
print("Random choice from list:", random.choice(items))

