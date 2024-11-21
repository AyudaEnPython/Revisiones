"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

def roll_dice():
    random_roll = random.randint(1,6)
    random_roll2 = random.randint(1,6)
    print(random_roll,end="" + " ")
    print( random_roll2)

dice_roll = input("Roll the dice? y/n ").upper()
while dice_roll != "n":
    roll_dice()

    dice_roll = input("Roll the dice? y/n ").upper()
    if dice_roll == "n":
        print("thanks for playing")
        break