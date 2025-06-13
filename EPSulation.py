class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance = 0):
        """
        Initializes a new bank account with an account number, holder's name,and intial balance.
        """
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = initial_balance

    # Implement methods to perform deposits and withdraws
    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        """
        if amount >0:
            self.__balance += amount
            print(f"Deposoits ₹{amount:.2f}. New blance is ₹{self.__balance:.2f}")
        else:
            print("Deposit amount must be positive ")
    def withdraw(self, amount):
        """
        Withdraw the specified amount from account.
        """
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount:.2f}. New balance is ₹{self.__balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
#  Task:
    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.__balance
    def __str__(self):
        """
        Return a string representation of the account details.
        """
        return (f"Account Number: {self.__account_number}\n"
                f"Holder Name: {self.__holder_name}\n"
                f"balance: ₹{self.__balance:.2f}")
        
# Task4:
# String representation of the bank account
if __name__ =="__main__":
    account = BankAccount("12345678", "ramar Bose", 1700)
    # print(account)
    account.deposit(500)
    account.withdraw(200)
    print(f"Final balance: ₹{account.get_balance():.2f}")

    
