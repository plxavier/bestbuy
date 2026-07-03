from products import Product

class Store:
    """
    Represents a store that holds and manages multiple products.

    Methods:
        add_product(product: Product): Adds a product to the store.
        remove_product(product: Product): Removes a product from the store.
        get_total_quantity() -> int: Returns the total stock of all products.
        get_all_products() -> list[Product]: Returns all active products.
        order(shopping_list: list[tuple[Product, int]]) -> float:
            Processes an order of multiple products and returns the total cost.
    """
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        try:
            if not isinstance(product, Product):
                raise TypeError("Only Product objects can be added to the store")
            self.products.append(product)
        except TypeError as e:
            print(f"Error adding product: {e}")

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        try:
            if product in self.products:
                self.products.remove(product)
            else:
                print(f"Product '{product.name}' not found in store")
        except AttributeError as e:
            print(f"Error removing product: Invalid product object - {e}")

    def get_total_quantity(self) -> int:
        """Return the total stock of all products."""
        try:
            return sum(p.get_quantity() for p in self.products)
        except AttributeError as e:
            print(f"Error calculating total quantity: {e}")
            return 0

    def get_all_products(self) -> list[Product]:
        """Return all active products."""
        try:
            return [p for p in self.products if p.is_active()]
        except AttributeError as e:
            print(f"Error getting active products: {e}")
            return []

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Process an order of multiple products and return the total cost.

        Args:
            shopping_list: List of tuples (Product, quantity)

        Returns:
            float: Total price of the order

        Raises:
            ValueError: If shopping_list is empty or invalid
            TypeError: If shopping_list contains invalid items
        """
        try:
            if not shopping_list:
                raise ValueError("Shopping list cannot be empty")

            total_price = 0.0

            for item in shopping_list:
                # Validate item format
                if not isinstance(item, tuple) or len(item) != 2:
                    raise TypeError("Each item must be a tuple (Product, quantity)")

                product, quantity = item

                if not isinstance(product, Product):
                    raise TypeError(f"Invalid product object: {product}")

                if not isinstance(quantity, int) or quantity <= 0:
                    raise ValueError(f"Quantity must be a positive integer for product '{product.name}'")

                try:
                    total_price += product.buy(quantity)
                except ValueError as e:
                    print(f"Error purchasing {product.name}: {e}")
                    raise
                except Exception as e:
                    print(f"Error purchasing {product.name}: {e}")
                    raise

            return total_price

        except ValueError as e:
            print(f"Order error: {e}")
            raise
        except TypeError as e:
            print(f"Order error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected order error: {e}")
            raise


def main():
    try:
        print("=== Initializing Store ===")
        # Create product list
        product_list = [
            Product("MacBook Air M2", price=1450, quantity=100),
            Product("Bose QuietComfort Earbuds", price=250, quantity=500),
            Product("Google Pixel 7", price=500, quantity=250),
        ]

        print("Products created successfully!")
        print()

        # Initialize store
        best_buy = Store(product_list)

        # Test get_all_products
        print("=== Active Products ===")
        active_products = best_buy.get_all_products()
        for product in active_products:
            print(product.show())
        print()

        # Test get_total_quantity
        print(f"=== Total Store Stock ===")
        total_stock = best_buy.get_total_quantity()
        print(f"Total quantity: {total_stock}")
        print()

        # Test order
        print("=== Processing Order ===")
        try:
            shopping_list = [
                (product_list[0], 2),  # MacBook Air M2 x 2
                (product_list[1], 10),  # Bose Earbuds x 10
                (product_list[2], 5),   # Google Pixel 7 x 5
            ]

            total = best_buy.order(shopping_list)
            print(f"Order total: ${total:.2f}")

            # Show updated products
            print("\n=== Updated Products ===")
            for product in product_list:
                print(product.show())

        except ValueError as e:
            print(f"Order failed: {e}")
        except Exception as e:
            print(f"Order failed: {e}")

        print()

        # Test adding a product
        print("=== Adding New Product ===")
        try:
            new_product = Product("Samsung Galaxy S23", price=800, quantity=150)
            best_buy.add_product(new_product)
            print(f"Added: {new_product.show()}")
            print(f"New total stock: {best_buy.get_total_quantity()}")
        except ValueError as e:
            print(f"Error adding product: {e}")

        print()

        # Test removing a product
        print("=== Removing a Product ===")
        try:
            product_to_remove = product_list[2]  # Google Pixel 7
            best_buy.remove_product(product_to_remove)
            print(f"Removed product: {product_to_remove.name}")

            # Show remaining products
            print("\n=== Remaining Products ===")
            for product in best_buy.get_all_products():
                print(product.show())

        except Exception as e:
            print(f"Error removing product: {e}")

        print()

        # Test edge cases
        print("=== Testing Edge Cases ===")

        # Test empty shopping list
        print("Testing empty shopping list:")
        try:
            best_buy.order([])
        except ValueError as e:
            print(f"  Caught: {e}")

        # Test invalid shopping list item
        print("Testing invalid shopping list item:")
        try:
            invalid_list = [("not a product", 5)]
            best_buy.order(invalid_list)
        except TypeError as e:
            print(f"  Caught: {e}")

        # Test buying with insufficient stock
        print("Testing insufficient stock:")
        try:
            shopping_list = [(product_list[0], 9999)]  # MacBook Air M2
            best_buy.order(shopping_list)
        except ValueError as e:
            print(f"  Caught: {e}")

        # Test buying inactive product
        print("Testing inactive product:")
        try:
            # Force deactivate a product by buying all stock
            mac = product_list[0]
            mac.buy(mac.get_quantity())  # Buy all MacBooks
            shopping_list = [(mac, 1)]  # Try to buy more
            best_buy.order(shopping_list)
        except Exception as e:
            print(f"  Caught: {e}")

        # Test adding invalid product
        print("Testing adding invalid product:")
        try:
            best_buy.add_product("not a product")
        except TypeError as e:
            print(f"  Caught: {e}")

    except Exception as e:
        print(f"Unexpected error in main: {e}")


if __name__ == '__main__':
    main()