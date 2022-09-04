"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Construya un programa en Python tal que, dado como datos la base y
la altura de un rectángulo, calcule el perímetro y la superficie de
este.

2. Elaborar un algoritmo que permita ingresar el número de partidos
ganados, perdidos y empatadas, por ABC club en el torneo apertura, se
debe mostrar su puntaje total, teniendo en cuenta que por cada partido
ganado obtendrá 3 puntos, empatado 1 y perdido 0 puntos.

3. Dado el sueldo de un trabajador, aplique un aumento del 15% si su
sueldo es inferior a $1000. Imprima el sueldo que percibirá.

4. Se desea leer por teclado un número comprendido entre 0 y 10 (
inclusive) y se desea visualizar si el número es par o impar.

5. Modifique el programa anterior para que se puedan ingresar varios
números diciendo si cada uno de ellos es par o no. La ejecución del
programa finalizará cuando se ingrese un 0 (cero).

6. Modifique el punto 5 para que aparte de hacer lo que ya hace, me
informe al final del proceso cuántos números fueron pares, cuántos
impares y cuántos números se ingresaron en total.

7. Ingresar por teclado 100 números enteros y calcular cúantos de ellos
son pares. Se debe imprimir el resultado de la suma de los pares y el
resultado de la suma de los impares.

8. Escribir un programa que imprima los 10 primeros números pares
comenzando por el 2 e imprima también sus respectivos valores elevados
al cuadrado y al cubo. Por ejemplo: valor: 2, cuadrado: 4, cubo. 8;
valor: 5, cuadrado: 16, cubo: 64...
"""
from typing import Callable, Tuple


# --------------------------------------------------------- Ejercicio 1
def perimetro(base: float, altura: float) -> float:
    return 2 * (base + altura)


def area(base: float, altura: float) -> float:
    return base * altura


# --------------------------------------------------------- Ejercicio 2
def puntaje(
    g: int, p: int, e: int, d: Tuple[int, int , int] = (3, 0, 1)
) -> int:
    return g * d[0] + p * d[1] + e * d[2]


# --------------------------------------------------------- Ejercicio 3
def sueldo(s: float) -> float:
    return s * 1.15 if s < 1000 else s


# --------------------------------------------------------- Ejercicio 4
def _ingresar_n(msg: str, a: int = 0, b: int = 10) -> int:
    while True:
        try:
            n = int(input(msg))
            if a < n <= b:
                return n
        except ValueError:
            print("Ingrese un número entero")


# ----------------------------------------------------- Ejercicio 5 y 6
def es_par(n: int) -> str:
    return n % 2 == 0


def comprobar_par_impar(msg: str, func: Callable, info: bool = False) -> None:
    i = j = k = 0
    while True:
        n = _ingresar_n(msg)
        if n == 0:
            break
        k += 1
        if func(n):
            i += 1
            print(f"{n} es par")
        else:
            j += 1
            print(f"{n} es impar")

    if info:
        print(f"Pares: {i}")
        print(f"Impares: {j}")
        print(f"Total: {k}")


# --------------------------------------------------------- Ejercicio 7
def par_impar_rango(x: int) -> None:
    p = sp = si = 0
    for i in range(x):
        n = _ingresar_n(f"[{i+1}] Ingrese el número: ")
        if es_par(n):
            p += 1
            sp +=n
        else:
            si += n
    print(f"Cantidad de pares: {p}")
    print(f"Suma de pares: {sp}")
    print(f"Suma de impares: {si}")


# --------------------------------------------------------- Ejercicio 8
def cuadrado_cubo(x: int = 10) -> None:
    for i in range(x):
        print(f"valor: {i * 2}, cuadrado: {(i * 2) ** 2}, cubo: {(i * 2) ** 3}")
