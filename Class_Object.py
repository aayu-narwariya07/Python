#  Task1:
# Define the bank account
class BankAccount:
    def  __init__(self, account_number, holder_name, intial_balance=0):
        """Initializes a new bank account with an account number, holder's name, and intial balance."""
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance=  intial_balance

# Deposit and withdraw methods
    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
          self.balance += amount
          print(f"Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraws the sepcified amount from the account.
        """
        if 0 < amount <=self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance is {self.balance:.2f}.")
        else:
            print("Insufficient funds or invalid amount.")

# Check the Account balance
    def get_balance(self):
        """
        Return the current balance of the account.
        """
        return self.balance
    
# String Representation of the Account
    def __str__(self):
        """
        Return a string representation of the account details
        """
        return(f"Account Number: {self.account_number}\n"
               f"Holder Name: {self.holder_name}\n"
               f"Balance: ₹{self.balance:.2f}")
    
# Example usage
if __name__ == "__main__":
    account = BankAccount("12345678", "Ramar", 1000)
    print (account)  
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500) 

# check balance
    print(f" Final balance: ₹{account.get_balance():.2f}")
