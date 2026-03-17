# Writing a programme using OOP to read an inventory list
# Prog then to return variables from the inventory list

# Define shoe class from inventory file
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # method definition get cost
    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost
    #method definition to get quantity
    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity
    # return string representation
    def __str__(self):
        """String representation of the Shoe object."""
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

# create empty shoes variable
shoes_list = []

# read data from the inventory file
def read_shoes_data():
    """Read data from inventory.txt and populate shoes_list."""
    try:
        with open("inventory.txt", "r") as file:
            # Skip the header line
            next(file)  
            for line in file:
                line = line.strip()
                if line:
                    country, code, product, cost, quantity = line.split(",")
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoes_list.append(shoe)
        print("Shoe data successfully loaded")
    except FileNotFoundError:
        print("Error: inventory.txt file not found")
    except Exception as e:
        print(f"An error occurred: {e}")

# capture data about the shoe to use and append data
def capture_shoes():
    """Allow user to capture shoe data."""
    print("\n--- Capture New Shoe ---")
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product name: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    # append data to a file
    with open("inventory.txt", "a") as file:
        file.write(f"\n{country},{code},{product},{cost},{quantity}")

    print("New shoe added successfully!")

#iterate over shoe list and print details
def view_all():
    """Display all shoes in inventory."""
    print("\n--- All Shoes in Inventory ---")
    for shoe in shoes_list:
        print(shoe)

# returns the lowest quantity
def re_stock():
    """Find the shoe with the lowest quantity and restock it."""
    if not shoes_list:
        print("Shoe list is empty")
        return

    min_shoe = min(shoes_list, key=lambda s: s.quantity)
    print(f"\nLowest stock shoe:\n{min_shoe}")

    choice = input("Do you want to restock shoe? (yes/no): ").lower()
    if choice == "yes":
        try:
            add_qty = int(input("Enter quantity to add: "))
            min_shoe.quantity += add_qty
            update_inventory_file()
            print("Stock updated successfully.")
        except ValueError:
            print("Invalid quantity entered.")

# search by code and print shoe
def search_shoe():
    """Search for a shoe by its code."""
    code = input("Enter shoe code to search: ").strip()
    for shoe in shoes_list:
        if shoe.code.lower() == code.lower():
            print(f"\nFound shoe:\n{shoe}")
            return
    print("Shoe not found.")

# finding the total cost of the shoes
def value_per_item():
    """Calculate total value for each shoe."""
    print("\n--- Value per Item ---")
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Total Value: R{value:.2f}")

# Find the largest quantity
def highest_qty():
    """Determine the product with the highest quantity."""
    if not shoes_list:
        print("Shoe list is empty. Load data first.")
        return

    max_shoe = max(shoes_list, key=lambda s: s.quantity)
    print(f"\n the shoe with the highest quantity (FOR SALE):\n{max_shoe}")

# Write to the inventory text file
def update_inventory_file():
    """Write the updated shoe list back to inventory.txt."""
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


# Inventory menu to define choices
def main():
    while True:
        print("""
======== SHOE INVENTORY MENU ========
1. Read shoes data
2. Capture new shoe
3. View all shoes
4. Restock shoes
5. Search shoe by code
6. Calculate value per item
7. Show highest quantity (For Sale)
8. Exit
""")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
