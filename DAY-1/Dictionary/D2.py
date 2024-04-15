# a real-world Python program that uses dictionary data structures for problem-solving and logic building. Let's create a program that tracks the inventory of a store and allows users to perform various operations such as adding items, updating quantities, checking stock availability, and displaying the inventory.


inventory = {}

def add_item(item_name, quantity):
 if item_name in inventory:
  inventory[item_name] += quantity
 else:
  inventory[item_name] = quantity
 print(f"{quantity} {item_name} (s) added to inventroy. ")


def update_item(item_name, new_quantity):
 if item_name in inventory:
  inventory[item_name] = new_quantity
  print(f"{item_name} quantity updated to {new_quantity}.")
 else:
  print(f"{item_name} not found in inventrory. ")
 

def check_stock(item_name):
 if item_name in inventory:
  print(f"{item_name}: {inventory[item_name]} in stock.")
 else:
  print(f"{item_name} not found in inventory.")

def display_inventory():
 print("Current Inventory: ")
 for item, quantity in inventory.items():
  print(f"{item} : {quantity}")




while True:
 print("\n1. Add Item in inevntory:  ")
 print("2. update Item in Inventory: ")
 print("3.  Check Stock of an Item: ")
 print("4. Display the entire Inventory: ")
 print("5. Exit: ")

 choice = input("Enter your choice (1-5)")

 if choice == '1':
  item_name = input("Enter you Item Name : ")
  quantity = int(input("Enter Quantity: "))
  add_item(item_name, quantity)
 elif choice == '2':
  item_name = input("Enter Item name: ")
  new_qty = input("Enter the new Quantity:")
  update_item(item_name, new_qty)
 elif choice == '3':
  item_name = input("Enter the item Name for stock updates: ")
  check_stock(item_name)
 elif choice == '4':
  display_inventory()
 elif choice == '5':
  print("Exiting...")
  break
 else:
  print("Invaild input You Have Enter. Please Enter  Again!")
  
