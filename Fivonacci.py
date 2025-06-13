#30 read the starting and ending numbers ffrom the user
start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number "))
# two fibonacci
a, b = 0, 1
fibonacci_series = []
while a <= end_num:
    if a >= start_num:
        fibonacci_series.append(a)
    a, b = b, a + b
if fibonacci_series:
    print(F"fibonacci series between {start_num} and {end_num} is ")
    print(fibonacci_series)
else:
    print(f"no fibonacci numbers found between {start_num} and {end_num} is") 
