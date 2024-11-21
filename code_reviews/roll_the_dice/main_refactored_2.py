"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint


def roll(n=2):
    return " ".join(str(randint(1, 6)) for _ in range(n))


def main():
    while True:
        user_input = input("Roll the dice? (y/n): ").lower()
        if user_input == "n":
            break
        print(roll())
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
