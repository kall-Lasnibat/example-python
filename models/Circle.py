class CashRegister:

    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.purchase = []
     
    # Add a product to the purchase
    def add_product(self, product, quantity=1):
        for _ in range(quantity):
            self.purchase.append(product)

     # Show the list of products in the current purchase
    def show_products(self):
        print("Current purchase:")
        for product in self.purchase:
            print(product)

    # Remove a product from the purchase
    def remove_product(self, product_name):
        for product in self.purchase:
            if product["name"] == product_name:
                self.purchase.remove(product)
                print(product_name, "removed.")
                return
        print(product_name, "not found.")

    # Update the price of a product after it has been added
    def update_price(self, product_name, new_price):
        updated = False
        for product in self.purchase:
            if product["name"] == product_name:
                product["price"] = new_price
                updated = True
        if updated:
            print("Price updated for", product_name)
        else:
            print(product_name, "not found.")

    # Find subtotal
    def get_subtotal(self):
        subtotal = 0
        for product in self.purchase:
            subtotal += product["price"]
        return round(subtotal, 2)

    # Find total taxes (5%)
    def get_taxes(self):
        return round(self.get_subtotal() * 0.05, 2)

    # Find total amount
    def get_total(self):
        return round(self.get_subtotal() + self.get_taxes(), 2)

    # Clear purchase
    def clear_purchase(self):
        self.purchase.clear()
        print("Purchase cleared.")


# Products
apple = {"name": "Apple", "price": 1.50}
bread = {"name": "Bread", "price": 2.30}
milk = {"name": "Milk", "price": 3.25}

# Cash register
register = CashRegister("Kall")

print("Cashier:", register.cashier_name)
print()

# Add products
register.add_product(apple)
register.add_product(bread, 2)
register.add_product(milk, 1)

# Show products
register.show_products()
print()

# Update price
register.update_price("Bread", 2.50)
print()

# Show products again
register.show_products()
print()

# Remove a product
register.remove_product("Apple")
print()

# Show products again
register.show_products()
print()

# Subtotal, taxes, and total
print("Subtotal:", register.get_subtotal())
print("Taxes:", register.get_taxes())
print("Total:", register.get_total())
print()

# Clear purchase
register.clear_purchase()
register.show_products()
