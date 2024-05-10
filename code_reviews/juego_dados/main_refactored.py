"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from textwrap import dedent
from typing import Dict, List, Tuple

INSTRUCCIONES = """\
En el juego puede lanzar dos dados y apostar al resultado. Puede apostar a
mayores que 7, menores que 7 o al 7. Si acierta con mayores o menores recibe
el doble de la cantidad que apostó. Si gana con el 7 recibe el triple de lo
que apostó.

Por ejemplo, si apuesta 5 puntos a los mayores y gana entonces recibe 5 más y
tiene 10. Si apuesta al 7 y gana entonces recibe 10 más y tiene 15. El jugador
comienza con 20 puntos y las apuestas no pueden ser de más de 3 puntos. Pierde
cuando se queda sin puntos y gana cuando llega a 30.
"""

T, V, A = "+-------+", "|       |", "| O     |"
B, C, D = "|   O   |", "|     O |", "| O   O |"
DADO: Dict[int, List[str]] = {
    1: [V, B, V], 2: [C, V, A], 3: [C, B, A],
    4: [D, V, D], 5: [D, B, D], 6: [D, D, D],
}


def lanzar_dados() -> Tuple[int, int]:
    return randint(1, 6), randint(1, 6)


def mostrar_dados(a: int , b: int) -> None: 
    print(T, T)
    for x, y in zip(DADO[a], DADO[b]):
        print(x, y)
    print(T, T)


def introduccion() -> None:
    respuesta = input("Ver instrucciones <s/n>: ").lower()
    if respuesta in "si":
        print(dedent(INSTRUCCIONES))


def ingresar_apuesta(puntos: int) -> int:
    while True:
        apuesta = input("Cantidad a apostar: ")
        try:
            apuesta = int(apuesta)
        except ValueError:
            print("Cantidad inválida, ingresar un número entero entre 1 y 3")
        else:
            if apuesta not in range(1, 4):
                print("No se puede apostar esa cantidad")
                continue
            elif apuesta > puntos:
                print("No tiene suficiente puntos para realizar esta apuesta")
                continue
            else:
                return apuesta


def ingresar_tipo() -> str:
    while True:
        tipo = input("A quéa apuesta? <mayores/menores/7>: ")
        if tipo in ("mayores", "menores", "7"):
            return tipo
        else:
            print("Opción no válida")


def puntuacion(
    dados: Tuple[int, int],
    jugada: Tuple[int, str],
    puntos: int,
) -> int:
    suma, (apuesta, tipo) = sum(dados), jugada
    m = 3 if tipo == "7" else 2
    if (
        (tipo == "mayores" and suma > 7) or
        (tipo == "menores" and suma < 7) or
        (tipo == "7" and suma == 7)
    ):
        puntos += m * apuesta
        print("¡Acertaste!")
    else:
        puntos -= apuesta
        print("¡No Acertaste!")
    return puntos


def continuar(puntos: int) -> bool:
    return 0 < puntos < 30


def main() -> None:
    puntos = 20
    introduccion()
    while True:
        print(f"Actualmente tiene {puntos} puntos")
        jugada = ingresar_apuesta(puntos), ingresar_tipo()
        dados = lanzar_dados()
        mostrar_dados(*dados)
        puntos = puntuacion(dados, jugada, puntos)
        print(puntos)
        if not continuar(puntos):
            break
    print("¡{} el juego!".format("Perdiste" if puntos == 0 else "Ganaste"))


if __name__ == "__main__":
    main()
