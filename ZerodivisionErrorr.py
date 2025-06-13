# Implement the zerodivisionerror and ValueError
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result of {num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot dividen by zero.")
    except ValueError:
        print("Error: Please enter valid numeric values.")
    finally:
        print("Division operation completed.")
