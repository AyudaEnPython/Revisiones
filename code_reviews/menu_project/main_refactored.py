"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import os
import json

CURR_DIR = os.path.dirname(__file__)
PATH = os.path.join(CURR_DIR, "list.json")
MENU = """Choose from the following 5 options:
1: Add an item to the list
2: Remove one item from the list
3: Show the list
4: Clear the list
5: Quit
Your choice: """
MENU_CHOICES = ("1", "2", "3", "4", "5")

if os.path.exists(PATH):
    with open(PATH, "r") as f:
        data = json.load(f)
else:
    data = []

while True:
    user_choice = input(MENU)
    if user_choice not in MENU_CHOICES:
        print("Please choose a valid option...")
        continue
    if user_choice == "1":
        item = input("Enter item name to add to shopping list: ")
        data.append(item)
        print(f"The {item} item has been successfully added to the list.")
    elif user_choice == "2":
        item = input("Insert item name to remove from shopping list: ")
        if item in data:
            data.remove(item)
            print(f"The {item} item has been successfully removed from the list.")
        else:
            print(f"The {item} item is not in the list.")
    elif user_choice == "3":
        if data:
            print("Here's the contents of your list:")
            for i, item in enumerate(data, 1):
                print(f"{i}. {item}")
        else:
            print("Your list does not contain any elements.")
    elif user_choice == "4":
        data.clear()
        print("The list has been cleared of its contents.")
    elif user_choice == "5":
        with open(PATH, "w") as f:
            json.dump(data, f, indent=4)
        break
print("See you soon!")
print("_" * 50)
