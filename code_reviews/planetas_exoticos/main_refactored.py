"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint, choice
from typing import Tuple

MIN, MAX = 4, 7
ABC: Tuple[str, ...] = ("", "aeiou", "bcdfghjklmnñopqrstvwxyz")


def generar() -> str:
    return "".join([choice(ABC[(-1)**x]) for x in range(randint(MIN, MAX))])


def main():
    nombres = [generar().capitalize() for _ in range(10)]
    print(*sorted(nombres), sep="\n")


if __name__ == "__main__":
    main()
