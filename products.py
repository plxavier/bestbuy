class Product:
    """
    Represents a product available in the Best-Buy store.

    Methods:
        get_quantity() -> int: Returns the current stock quantity.
        set_quantity(quantity: int): Updates the stock quantity, stops if 0.
        is_active() -> bool: Checks if the product is active/available.
        deactivate(): Marks the product as inactive/unavailable.
        show() -> str: Returns a string representation of the product.
        buy(quantity: int) -> float: Purchases items, decreases stock, returns total price.
    """
    def __init__(self, name: str, price: float, quantity: int):
        if not name.strip():
            raise ValueError('Name cannot be an empty string')
        if price < 0:
            raise ValueError('Price cannot be negative')
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if not self.active:
            raise Exception('Product is unavailable(out of stock) and cannot be purchased')

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


def main():
    """Main function to initialize and run the store. For autotesting the script uncomment tests"""
    try:
        # Create products
        bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        # Show products
        print("=== Initial Products ===")
        print(bose.show())
        print(mac.show())
        print()

        # # Test purchases
        # print("=== Testing Purchases ===")
        # try:
        #     print(f"Buying 50 Bose: ${bose.buy(50):.2f}")
        #     print(f"Buying 100 MacBook: ${mac.buy(100):.2f}")
        # except ValueError as e:
        #     print(f"Purchase error: {e}")
        # except Exception as e:
        #     print(f"Purchase error: {e}")
        #
        # print()

        # Show products after purchases
        print("=== After Purchases ===")
        print(bose.show())
        print(mac.show())
        print(f"MacBook active: {mac.is_active()}")
        print()

        # # Test setting quantity
        # print("=== Setting Quantity ===")
        # try:
        #     bose.set_quantity(1000)
        #     print(f"Updated Bose quantity to {bose.get_quantity()}")
        #     print(bose.show())
        # except ValueError as e:
        #     print(f"Error setting quantity: {e}")
        #
        # print()

        # # Test edge cases
        # print("=== Testing Edge Cases ===")
        #
        # # Test invalid product creation
        # try:
        #     invalid = Product("", price=10, quantity=5)
        #     print(invalid.show())
        # except ValueError as e:
        #     print(f"Product creation error: {e}")
        #
        # # Test buying from inactive product
        # try:
        #     print("Trying to buy from inactive MacBook...")
        #     mac.buy(1)
        # except Exception as e:
        #     print(f"Error: {e}")

        # # Test buying with insufficient quantity
        # try:
        #     print("Trying to buy 2000 Bose...")
        #     bose.buy(2000)
        # except ValueError as e:
        #     print(f"Error: {e}")
        #
        # # Test setting negative quantity
        # try:
        #     print("Trying to set negative quantity...")
        #     bose.set_quantity(-5)
        # except ValueError as e:
        #     print(f"Error: {e}")
        #
        # print()
        # print("=== Final Product State ===")
        # print(bose.show())
        # print(mac.show())

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()