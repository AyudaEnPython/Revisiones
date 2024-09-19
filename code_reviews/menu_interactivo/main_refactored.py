"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import menu_input


def main():
    options = "frutilla", "manzana", "pera"
    user_input = menu_input(options, numbers=True)
    print(f"Su elección fue '{user_input}'")


if __name__ == "__main__":
    main()
