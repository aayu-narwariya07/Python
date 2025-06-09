# Initialize a counter
count = 1
while count <= 5:
    print(count)
    count += 1
# Correct number to guess
correct_number = 7
guess = 0
while guess != correct_number:
    guess = int(input("Guess the number between 1 and 10: "))
print("congratulation! you guessed the correct number. ")
# break loop
number = 10
while number >0:
    print(number)
    number -= 1
    if number == 5:
        break
print(number)
# continue
number = 0
while number < 10:
    number += 1
    if number% 2 == 0:
        continue
    print(number)
# start an infinite loop
while True:
    name = input("Enter your name (type 'exit' to stop ): ")
    if name.lower() == 'exit':
        break
    print(f"hello, {name}!")
print("loop exited.")
