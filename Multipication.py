 multiplication table 
number = int(input("Enter a number to create its multiplication table : "))
print(F"multiplication table for {number} : ")
for i in range (1 , 11):
    result = number * i
    print(f"{number} * {i} = {result}")
