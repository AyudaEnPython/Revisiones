"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random


def roll_dice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    print(f"{x} {y}")


while True:
    user_input = input("Roll the dice? y/n ").lower()
    if user_input == "n":
        break
    roll_dice()

print("thanks for playing")