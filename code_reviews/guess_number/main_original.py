"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

# generate random number and store it in a variable
def rand_num():
    num = random.randint(1, 100)
    return num

number = rand_num()

# let user guess a number between 1 and 100
def user_guess():
    user = input("Guess a number between 1 and 100: ")
    return user

# check if input is a number
def str_2_int():
    user = user_guess()
    while not user.isdigit():
        user = user_guess()
    user = int(user)
    return user

# checks if input is between 1 and 100
def is_valid():
    user = str_2_int()
    while user < 1 or user > 100:
        user = str_2_int()
    return user

# check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answe. Track the number of turns remaining.
def is_correct(num, counter):
    user = is_valid()
    if user > num:
        print("Too high. Try again.")
        counter -= 1
        print(counter, "turns left")
        is_correct(num, counter)
    elif user < num:
        print("Too low. Try again.")
        counter -= 1
        print(counter, "turns left")
        is_correct(num, counter)
# if they got the answer correct, show the actual answer to the player.
    else:
        counter = 0
        print(f"Guess is correct! Computer selected number is {num}")

# Include different difficulty levels
def difficulty(dif_lvl):
    lvl = input("Select difficulty: Easy (1), Medium (2), Hard (3): ")
    while not lvl.isdigit():
        lvl = input("Select difficulty: Easy (1), Medium (2), Hard (3): ")
    lvl = int(lvl)
    while lvl < 1 or lvl > 3:
        lvl = input("Select difficulty: Easy (1), Medium (2), Hard (3): ")
    turns = dif_lvl[lvl - 1]
    return turns

lvl_list = [10, 7, 5]

# Include an ASCII art logo.
# from art import logo
# print(logo)

turns_left = difficulty(lvl_list)
print(number) # for testing only

while turns_left > 0:
    is_correct(number, turns_left)

# if they run out of turns, provide feedback to the player.
print(f"No turns left. Correct number was {number}")