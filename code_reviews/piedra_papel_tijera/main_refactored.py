"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
# pip install prototools
from prototools import int_input, textbox, text_align

T = "Piedra", "Papel", "Tijera"


def check(player, cpu):
    if player - cpu == 0:
        return "Empate"
    if player - cpu in (-2, 1):
        return "Ganaste"
    return "Perdiste"


def main():
    text_align("Piedra, papel o tijera", align="center")
    print("Selecciona una opcion:")
    print("\n".join(f"{i}. {opcion}" for i, opcion in enumerate(T, 1)))
    usuario = int_input("> ", min=1, max=3, lang="es")
    cpu = randint(1, 3)
    text_align(f"{T[usuario - 1]} (Tu) vs {T[cpu-1]} (CPU)", align="center")
    textbox(check(usuario, cpu))


if __name__ == "__main__":
    main()
