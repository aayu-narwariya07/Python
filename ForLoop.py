 A string
word = "Edunet Foundation"
for letter in word:
    print(letter)
# using range () in for loop
for i in range (5):
    print(i)
# number of rows for the triangle
rows = 5
# Outer loop for the number of rows
for i in range(1, rows + 1):
    for j in range (i):
        print("*", end = " ")
    print()
# for loop with break
for i in range (10):
    if i == 5:
        break
    print(i)
# for loop with continue
# even number
for i in range(10):
    if i  % 2 == 0:
        continue
    print(i) 
# for loop with else
# else
for i in range(5):
    print(i)
else:
    print("loop completed successfully")
