# Input two numbers to perform the operation
import main_function as mf
def main():
    print("simple Calulator")
    print("Select operation: ")
    print("1. Add ")
    print("2. subtract ")
    print("3. MUltiply")
    print("4. Divide")

    # Get user choice
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter frist number: "))
    num2 = float(input("Enter second number: "))

    # perform the chosen operation
    if choice =='1':
        print(f"{num1} + {num2} = {mf.add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {mf.subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {mf.multiply(num1, num2 )}")
    elif choice == '4':
        print(f"{num1} / {num2} = {mf.divide(num1, num2)}")
    else:
        print("Invalid input ! Please select a valid opration. ")

if __name__ == "__main__":
    main()


