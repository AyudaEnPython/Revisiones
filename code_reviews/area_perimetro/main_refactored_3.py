"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import pi as PI
# pip install prototools
from prototools import float_input, textbox, main_loop


def calcular(r):
    return PI * r ** 2, 2 * PI * r


def main():
    r = float_input("Radio: ", lang="es")
    a, p = calcular(r)
    textbox(f"Área: {a}\nPerímetro: {p}")


if __name__ == "__main__":
    print("Área y perímetro de un círculo")
    main_loop(main, lang="es")
