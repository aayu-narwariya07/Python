# Opening and closing a file
# opening a file in write mode ('w')
file = open('example.txt', 'w')
file.write("Thanks for the memories 2024.\nWelcome the new chepter 2025.Happy new year! ")
file.close()

# task 2:
# opening a file in read mode('r')
file = open('example.txt', 'r')
content = file.read()
print("Full content:")
print(content)
file.close()

# Task3:
# using read lines()
file = open('example.txt', 'r')
print("Reading all lines at once: ")
lines = file.readlines()
for line in lines:
    print(line, end= '')
file.close()

# task4:
# using readlines()
# opening the file again to read all lines at once
file = open('example.txt', 'r')
print("Reading all lines at once:")
lines = open('example.txt', 'r')
for line in lines:
    print(line, end='')
file.close()

# Task5:
# opening a file in append mode('a')
file = open('example.txt', 'a')
file.write("\nAppending a new line to the file. ")
file.close()

# task6
# Using with statement for file handling
#  Using with satement to automatically close the file

with open('example.txt', 'r') as file:
    content = file.read()
    print("Contant using 'with' statement: ")
    print(content)

# tesk7
# file pointer managment
# open file in read mode
with open('example.txt', 'r') as file:
    print("Initial pointer position:", file.tell())
    file.read(5)
    print("pointer position after reading 5 characters:", file.tell())

    file.seek(0)
    print("pointer position after seek(0):", file.tell())

    content = file.read()
    print("content after seek(0):")
    print(content)

# Tesk 8:
# checking file existence with csv file
import os
file_path = 'testcsvfile.csv'
if os.path.exists(file_path):
    print(f"'{file_path}' exists.")
else:
    print(f"'{file_path}' does not exist. ")

# Tesk 9:
# handing file Exceptions
try:
    with open('non_existent_file.txt','r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist. ")
