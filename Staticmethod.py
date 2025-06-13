# Task1:
# Define the Shopping Cart class and add items
class ShoppingCart:
    tax_rate = 0.08
    def __init__(self):
        self.items = []
    def add_item(self, name, price):
        """
        Add an item to the shopping cart.
        """
        self.items.append({'name': name, 'price': price})

# Task2:
# Calculate Total price including Tax
    def calculate_total(self):
        total = sum(item['price'] for item in self.items)
        total_with_tax = total + (total* self.tax_rate)
        return total_with_tax
    
# Task3:
# Apply discount to the total price
    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        discount = total *(discount_percentage/ 100)
        return total - discount

# Task3:
# Apply discount to the total price
    def apply_discount(self, discount_percentage):
        """
        Apply a discount to the total price.
        """
        total = self.calculate_total()
        discount = total * (discount_percentage/100) 
        return total- discount

    # Task4:
    # calculate Tax 
    @staticmethod
    def format_price(amount):
        return f"${amount:.2f}"

    @staticmethod

    def calculate_tax(amount):
        return amount * ShoppingCart.tax_rate

# Example
cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Headphone", 150)
cart.add_item("Mouse", 50)
# calculate the total price
total_price = cart.calculate_total()
print(f"total price (including tax): {ShoppingCart.format_price(total_price)}")

# apply a discount
discount_price = cart.apply_discount(10)
print(f"price after discount: {ShoppingCart.format_price(discount_price)}")

tax_on_laptop = ShoppingCart.calculate_tax(1000)
print(f"Tax on laptop:{ShoppingCart.format_price(tax_on_laptop)}")
