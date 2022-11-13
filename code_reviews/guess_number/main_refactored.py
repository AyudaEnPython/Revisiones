"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
# pip install prototools
from prototools import menu_input, int_input, write_letters, text_align

MIN, MAX = 1, 100
TITLE = "Guess the Number"
MODE = {"Difficult": 5, "Medium": 7, "Easy": 10}


def get_number(a=MIN, b=MAX):
    return randint(a, b)


def get_turns_left():
    return MODE[menu_input(tuple(MODE.keys()), numbers=True)]


def get_user_guess():
    return int_input(
        f"Guess a number between {MIN} and {MAX}: ", min=MIN, max=MAX,
    )


def check(number, user_guess):
    if user_guess > number:
        return False, "Too high."
    elif user_guess < number:
        return False, "Too low."
    else:
        return True, f"Your guess is correct! The number is {number}"


def main():
    write_letters(TITLE)
    number = get_number()
    turns_left = get_turns_left()
    while turns_left > 0:
        text_align(f"{turns_left} turns left.")
        user_guess = get_user_guess()
        has_guessed, message = check(number, user_guess)
        print(message)
        if has_guessed:
            break
        turns_left -= 1
    if turns_left == 0:
        print(f"No turns left. The correct number was {number}")


if __name__ == "__main__":
    main()
