# Task1:
# Define the base class item
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def display(self):
        print(f"Item: {self.name}, Quantity: {self.quantity}")

# Task2:
# Define the class perishableitem
class PerishableItem(Item):
    def __init__(self, name, quantity,expriration_date):
        super().__init__(name, quantity)
        self.expriration_date = expriration_date

    def display(self):
        super().display()
        print(f"Expiration Date: {self.expriration_date}")

# Task3 Define the class NonPerishableltem
class NonPerishableItem(Item):
    def display(self):
        super().display()
        print("This is a non-perishable item.")

# Task4: Object and disply item details
apple = PerishableItem("Apple", 10, "2024-10-15")
canned_beans = NonPerishableItem("Canned Beans", 20)

print("Perishable Item Details:")
apple.display()
print("\nNon-perishable Item Details: ")
canned_beans.display()
