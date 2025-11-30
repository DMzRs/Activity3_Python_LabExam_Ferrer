#class for individual item details
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, amount):
        self.quantity = amount

    def __str__(self):
        return f"Items (Name={self.name}, Quantity={self.quantity}, Price={self.price}, Total Value={self.quantity * self.price})"

#class for inventory management and controls
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            raise ValueError("Item already exists in inventory.")
        self.items[item.name] = item

    def update_item_quantity(self, item_name, amount):
        if item_name not in self.items:
            raise ValueError("Item not found in inventory.")
        self.items[item_name].update_quantity(amount)

    def get_item(self, item_name):
        return self.items.get(item_name, None)

    def list_items(self):
        return list(self.items.values())


#MAIN

#call inventory management system method
inventory = Inventory()
running = True

#loop the program until user exits
while running:
    print("=====INVENTORY MANAGEMENT SYSTEM=====")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. View All Items")
    print("4. View Total Inventory Value")
    print("5. Exit")
    print("=====================================")
    print("Selected Option:")
    choice = input()

    #process user input depending on choice

    #add item to inventory
    if choice == '1':
        name = input("Enter item name: ").strip()
        if not name:
            print("Item name cannot be empty.")
            continue
        try:
            quantity = int(input("Enter item quantity: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        try:
            price = float(input("Enter item price: ").strip())
        except ValueError:
            print("Invalid price. Please enter a number.")
            continue
        item = Item(name, quantity, price)
        try:
            inventory.add_item(item)
            print("Item added successfully.")
        except ValueError as e:
            print(e)

    #update item quantity in inventory
    elif choice == '2':
        name = input("Enter item name to update quantity: ").strip()
        if not name:
            print("Item name cannot be empty.")
            continue
        try:
            amount = int(input("Enter quantity to add: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue
        try:
            inventory.update_item_quantity(name, amount)
            print("Item quantity updated successfully.")
        except ValueError as e:
            print(e)

    #view all items in inventory
    elif choice == '3':
        items = inventory.list_items()
        if not items:
            print("No items in inventory.")
        else:
            for item in items:
                print(item)

    #view total inventory value
    elif choice == '4':
        total_value = sum(item.quantity * item.price for item in inventory.list_items())
        print(f"Total Inventory Value: {total_value}")

    #exit the program
    elif choice == '5':
        running = False
        print("Exiting Inventory Management System....")

    #invalid option
    else:
        print("Invalid option selected.")