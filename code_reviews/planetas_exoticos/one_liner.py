"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint, choice

print(
    *sorted([
        "".join([
            choice(("", "aeiou", "bcdfghjklmnñopqrstvwxyz")[(-1)**x])
            for x in range(randint(4, 7))
        ]).capitalize() for _ in range(10)
    ]),
    sep="\n",
)
