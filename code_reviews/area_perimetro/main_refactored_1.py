"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import pi

while True:
    print("1. Área y perímetro\n2. Salir\nIngresar una opción: ")
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
        radio = float(radio)
        area = pi * radio ** 2
        perimetro = 2 * pi * radio
        print("\nResultados")
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")
print("!Gracias por utilizar el programa, vuelve pronto!")
