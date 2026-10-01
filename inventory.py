class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (
            f"country: {self.country}, "
            f"code: {self.code}, "
            f"product: {self.product}, "
            f"cost: {self.cost}, "
            f"quantity: {self.quantity}"
        )


# This list stores all the shoe objects.
shoe_list = []


def read_shoes_data():
    """Read shoe information from inventory.txt and create Shoe objects."""
    try:
        with open("inventory.txt", "r") as file:
            next(file)

            for line in file:
                line = line.strip()

                if not line:
                    continue

                country, code, product, cost, quantity = line.split(",")

                shoe = Shoe(
                    country,
                    code,
                    product,
                    float(cost),
                    int(quantity)
                )

                shoe_list.append(shoe)

        print("Inventory data loaded successfully.")

    except FileNotFoundError:
        print("Error: inventory.txt could not be found.")

    except ValueError:
        print("Error: There is invalid data in inventory.txt.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")


def capture_shoe():
    """Allow the user to enter a new shoe and add it to the list."""
    try:
        country = input("Enter country: ")
        code = input("Enter the shoe code: ")
        product = input("Enter the shoe product: ")
        cost = float(input("Enter the shoe cost: "))
        quantity = int(input("Enter the shoe quantity: "))

        new_shoe = Shoe(
            country,
            code,
            product,
            cost,
            quantity
        )

        shoe_list.append(new_shoe)

        print("Shoe added successfully.")

    except ValueError:
        print("Please enter a valid number for cost and quantity.")


def view_all():
    """Display all shoes in the inventory."""
    if not shoe_list:
        print("There are no shoes in the inventory.")
        return

    print("\n======== Shoe Inventory ========")

    for shoe in shoe_list:
        print(shoe)

    print("==============================")


def re_stock():
    """Find the shoe with the lowest quantity and offer to restock it."""

    if not shoe_list:
        print("There are no shoes in the inventory.")
        return

    lowest_shoe = min(
        shoe_list,
        key=lambda shoe: shoe.get_quantity()
    )

    print("\n========== Restock ==========")
    print("Shoe with the lowest quantity:")
    print(lowest_shoe)

    choice = input(
        "Would you like to restock this shoe? (yes/no): "
    ).lower()

    if choice == "yes":
        try:
            amount = int(
                input("How many shoes would you like to add? ")
            )

            if amount <= 0:
                print("Please enter a number greater than 0.")
                return

            lowest_shoe.quantity += amount

            # Read the current inventory file.
            with open("inventory.txt", "r") as file:
                lines = file.readlines()

            # Rewrite the file with the updated quantity.
            with open("inventory.txt", "w") as file:
                file.write(lines[0])

                for line in lines[1:]:
                    parts = line.strip().split(",")

                    if len(parts) == 5 and parts[1] == lowest_shoe.code:
                        parts[4] = str(lowest_shoe.quantity)
                        file.write(",".join(parts) + "\n")
                    else:
                        file.write(line)

            print("Shoe quantity updated successfully.")

        except ValueError:
            print("Please enter a whole number.")

        except FileNotFoundError:
            print("Error: inventory.txt could not be found.")

    elif choice == "no":
        print("No changes were made.")

    else:
        print("Please enter yes or no.")


def search_shoe():
    """Search for a shoe using its code."""
    code = input(
        "Enter the shoe code you want to search for: "
    ).strip()

    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print("\nShoe found:")
            print(shoe)
            return shoe

    print("Shoe not found.")
    return None


def value_per_item():
    """Calculate and display the total value of every shoe."""
    if not shoe_list:
        print("There are no shoes in the inventory.")
        return

    print("\n======== Value per Item ========")

    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"{shoe.product} ({shoe.code}) - "
            f"cost: {shoe.get_cost():.2f}, "
            f"Quantity: {shoe.get_quantity()}, "
            f"Total value: {value:.2f}"
        )

    print("==============================")


def highest_qty():
    """Find and display the shoe with the highest quantity."""
    if not shoe_list:
        print("There are no shoes in the inventory.")
        return

    highest_shoe = max(
        shoe_list,
        key=lambda shoe: shoe.get_quantity()
    )

    print("\n======== Highest Quantity ========")
    print("Shoe with the highest quantity:")
    print(highest_shoe)
    print("This shoe is currently for sale.")
    print("=========================================")


# Load the inventory when the program starts.
read_shoes_data()


while True:
    print("\n======== Nike Shoe Inventory =======")
    print("1. View all shoes")
    print("2. Capture a new shoe")
    print("3. Restock the shoe with the lowest quantity")
    print("4. Search for a shoe")
    print("5. Calculate the value per item")
    print("6. Find the shoe with the highest quantity")
    print("7. Exit")
    print("=============================================")

    choice = input("Please select an option (1-7): ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoe()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")