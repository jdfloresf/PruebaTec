# 69. Write a Python class to represent a shopping cart with methods 
# to add, remove, and view items.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price):
        """Add an item to the shopping cart."""
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
            self.items[item_name]['price'] = price
        else:
            self.items[item_name] = {'quantity': quantity, 'price': price}

    def remove_item(self, item_name, quantity=None):
        """Remove an item or decrease its quantity from the shopping cart."""
        if item_name in self.items:
            if quantity is None or self.items[item_name]['quantity'] <= quantity:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity
        else:
            raise KeyError(f"Item '{item_name}' not found in the cart")

    def view_cart(self):
        """Return a list of items in the cart with their quantities and prices."""
        return [(item, info['quantity'], info['price']) for item, info in self.items.items()]

    def __str__(self):
        """Return a string representation of the shopping cart."""
        if not self.items:
            return "Shopping cart is empty"
        cart_contents = "\n".join([f"{item}: {info['quantity']} @ ${info['price']:.2f} each"
                                   for item, info in self.items.items()])
        return f"Shopping Cart:\n{cart_contents}"


cart = ShoppingCart()
cart.add_item("Apple", 3, 0.5)
cart.add_item("Banana", 2, 0.3)
cart.add_item("Orange", 5, 0.7)
print(cart)
print("\nViewing cart contents:")
print(cart.view_cart())
print("\nRemoving 2 Oranges...")
cart.remove_item("Orange", 2)
print(cart)
print("\nRemoving all Bananas...")
cart.remove_item("Banana")
print(cart)
