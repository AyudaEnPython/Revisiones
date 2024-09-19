"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import pi as PI

MENU = "1. Área y perímetro\n2. Salir\nIngresar una opción: "


def calcular(r):
    return PI * r ** 2, 2 * PI * r


def main():
    while True:
        print(MENU)
        opcion = input("> ")
        if opcion == "2":
            break
        if opcion not in "12" or not opcion:
            print("Opción no válida! Ingresar 1 o 2")
            continue
        radio = input("radio: ")
        if not radio.isdigit():
            print("Debes ingresar un número")
            continue
        else:
            area, perimetro = calcular(float(radio))
            print(f"\nResultados\nÁrea: {area}\nPerímetro: {perimetro}")
    print("!Gracias por utilizar el programa, vuelve pronto!")


if __name__ == "__main__":
    main()
