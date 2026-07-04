from products import Product
from store import Store


def list_products(store: Store):
    """Show all active products."""
    try:
        products = store.get_all_products()
        if not products:
            print('No products available')
            return
        print("\n=== Available Products ===")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.show()}")
    except Exception as error:
        print(f"Error listing products: {error}")


def show_total_quantity(store: Store):
    """Show total quantity of items in store."""
    try:
        total = store.get_total_quantity()
        print(f"\nTotal of {total} items in store")
    except Exception as error:
        print(f"Error getting total quantity: {error}")


def make_order(store: Store):
    """Handle user orders interactively."""
    orders = []

    try:
        while True:
            try:
                products = store.get_all_products()
                if not products:
                    print('No products available for ordering!')
                    break

                print('\n=== Available Products ===')
                for i, p in enumerate(products, start=1):
                    print(f"{i}. {p.show()}")

                print('\nEnter 0 to finish your order')

                try:
                    choice = int(input("Which product # do you want? "))
                except ValueError:
                    print('Please enter a valid number.')
                    continue

                if choice == 0:
                    break
                if choice < 0 or choice > len(products):
                    print("Invalid product number.")
                    continue

                try:
                    quantity = int(input("What amount do you want? "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if quantity < 0:
                    print("Quantity must be positive.")
                    continue

                if quantity == 0:
                    print("Quantity cannot be zero.")
                    continue

                # Check if product is active before adding to order
                try:
                    selected_product = products[choice - 1]
                    if not selected_product.is_active():
                        print(f"Product '{selected_product.name}' is inactive\n"
                              f" and cannot be ordered.")
                        continue
                except Exception as error:
                    print(f"Error checking product status: {error}")
                    continue

                orders.append((products[choice - 1], quantity))
                print(f"✅ Added {quantity} x {products[choice - 1].name} to your order")

            except KeyboardInterrupt:
                print("\nOrder cancelled by user.")
                return
            except Exception as error:
                print(f"Unexpected error in order process: {error}")
                continue

        if orders:
            try:
                total_price = store.order(orders)
                print(f"\n✅ Order placed! Total payment: ${total_price:.2f}")
            except ValueError as error:
                print(f"Error processing order: {error}")
            except Exception as error:
                print(f"Error processing order: {error}")
        else:
            print('No items were ordered.')

    except Exception as error:
        print(f"Unexpected error in make_order: {error}")


def start(store: Store):
    """Main menu loop."""
    menu_options = {
        1: list_products,
        2: show_total_quantity,
        3: make_order
    }

    while True:
        try:
            print("\n    Store Menu    ")
            print("    ----------     ")
            print("1. List all products in store")
            print("2. Show total amount in store")
            print("3. Make an order")
            print("4. Quit")

            try:
                user_choice = int(input("Please choose a number: "))
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 4.')
                continue

            if user_choice == 4:
                print('Good Bye!')
                break

            action = menu_options.get(user_choice)
            if action:
                try:
                    action(store)
                except Exception as error:
                    print(f"Error performing action: {error}")
            else:
                print('Please enter a valid option (1-4)')

        except KeyboardInterrupt:
            print("\n\nGood Bye!")
            break
        except Exception as error:
            print(f"Unexpected error in menu: {error}")
            continue


def main():
    """Main function to initialize and run the store."""
    try:
        print("=== Initializing Store ===")

        # Setup initial stock of inventory
        try:
            product_list = [
                Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
                Product("Samsung Galaxy S23", price=800, quantity=150),
            ]
            print("Products created successfully!")
        except ValueError as error:
            print(f"Error creating products: {error}")
            return
        except Exception as error:
            print(f"Unexpected error creating products: {error}")
            return

        try:
            best_buy = Store(product_list)
            print("Store initialized successfully!")
            print(f"Total products in store: {len(best_buy.products)}")
            print(f"Total stock: {best_buy.get_total_quantity()}")
        except Exception as error:
            print(f"Error initializing store: {error}")
            return

        # Start the main menu
        try:
            start(best_buy)
        except Exception as error:
            print(f"Error in store menu: {error}")

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Good Bye!")
    except Exception as error:
        print(f"Fatal error in main: {error}")


if __name__ == "__main__":
    main()
