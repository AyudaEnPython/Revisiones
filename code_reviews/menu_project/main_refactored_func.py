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
MESSAGES = {
    "input_add": "Enter item name to add to the shoppin list: ",
    "input_remove": "Insert item name to remove from shopping list: ",
    "show_true": "Here's the contents of your list:",
    "show_false": "Your list does not contain any elements.",
    "add": "The {} item has been successfully added to the list.",
    "remove": "The {} item has been successfully removed from the list.",
    "not_in_list": "The {} item is not in the list.",
    "cleared": "The list has been cleared of its contents.",
    "invalid_option": "Please choose a valid option..."
}
MENU_CHOICES = ("1", "2", "3", "4", "5")


def load_data():
    if os.path.exists(PATH):
        with open(PATH, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)


def add_item(data):
    item = input(MESSAGES["input_add"])
    data.append(item)
    print(MESSAGES["add"].format(item))


def remove_item(data):
    item = input(MESSAGES["input_remove"])
    if item in data:
        data.remove(item)
        print(MESSAGES["remove"].format(item))
    else:
        print(MESSAGES["not_in_list"].format(item))


def show_list(data):
    if data:
        print(MESSAGES["show_true"])
        for i, item in enumerate(data, 1):
            print(f"{i}. {item}")
    else:
        print(MESSAGES["show_false"])


def clear_list(data):
    data.clear()
    print(MESSAGES["cleared"])


def main():
    data = load_data()
    while True:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print(MESSAGES["invalid_option"])
            continue
        if user_choice == "1":
            add_item(data)
        elif user_choice == "2":
            remove_item(data)
        elif user_choice == "3":
            show_list(data)
        elif user_choice == "4":
            clear_list(data)
        elif user_choice == "5":
            save_data(data)
            break
    print("See you soon!")
    print("_" * 50)


if __name__ == "__main__":
    main()
