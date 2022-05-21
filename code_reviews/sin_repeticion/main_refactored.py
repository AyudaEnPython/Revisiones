"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List


def sin_repeticion(x: List[float], y: List[float]) -> List[float]:
    return list(set(x) & set(y))


def main():
    msg = "Ingresar elementos de {} separados por comas: "
    get_data = lambda s: input(s).split(",")
    x, y = get_data(msg.format("X")), get_data(msg.format("Y"))
    print(*sin_repeticion(x, y), sep=", ")


if __name__ == "__main__":
    main()
