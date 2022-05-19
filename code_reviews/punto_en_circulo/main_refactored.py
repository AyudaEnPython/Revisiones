"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import namedtuple
from typing import Tuple
# pip install prototools
from prototools import float_input

Punto: Tuple[float, float] = namedtuple("Punto", ["x", "y"])


def get_data() -> Punto:
    return (
        Punto(float_input("h: "), float_input("h: ")),
        Punto(float_input("x: "), float_input("y: ")),
        float_input("r: ")
    )


def get_zone(p: Punto, c: Punto) -> int:
    if p.x > c.x and p.y > c.y:
        return "A"
    elif p.x < c.x and p.y > c.y:
        return "B"
    elif p.x < c.x and p.y < c.y:
        return "C"
    else:
        return "D"


def show_result(c: Punto, p: Punto, r: float) -> str:
    if (p.x - c.x) ** 2 + (p.y - c.y) ** 2 < r ** 2:
        return f"{p} esta en el interior del circulo"
    elif (p.x - c.x) ** 2 + (p.y - c.y) ** 2 == r ** 2:
        return f"{p} esta en el circunferencia del circulo"
    elif p.x <= c.x + r and p.y <= c.y + r:
        return (
            f"{p} esta fuera del circulo pero dentro del cuadrado\n"
            f"{p} se encuentra en la zona {get_zone(p, c)}"
        )
    else:
        return f"{p} está fuera del circulo y del cuadrado"


def main():
    print(show_result(*get_data()))


if __name__ == "__main__":
    main()
