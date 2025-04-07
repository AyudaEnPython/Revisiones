"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import choice


def jugar(palabras, intentos):
    secreta = choice(palabras)
    reveladas = set()
    print(f"La palabra seleccionada tiene {len(secreta)} letras.")
    for intento in range(1, intentos+1):
        pista = choice([letra for letra in secreta if letra not in reveladas])
        reveladas.add(pista)
        print(
            f"Intento {intento}/{intentos}: "
            f"una letra de la palabra secreta es: {pista}"
        )
        palabra = input("Ingresa la palabra: ").lower()
        if palabra == secreta:
            print("Adivinaste!")
            return True
        else:
            print("Incorrecto, intenta nuevamente.")
    print(f"Demasiados intentos. La palabra correcta era: {secreta}")
    return False


def continuar():
    while True:
        respuesta = input("\n¿Quieres jugar otra ronda? (si/no): ").lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Respuesta no válida, ingresar 'si' o 'no'.")


def main():
    PALABRAS = ["robot", "sensor", "azul", "cafe", "voltaje"]
    INTENTOS = 3
    while True:
        resultado = jugar(PALABRAS, INTENTOS)
        if resultado:
            print("¡Ganaste esta ronda!")
        else:
            print("¡Perdiste esta ronda!")
        if not continuar():
            print("\nGracias por jugar!")
            break


if __name__ == "__main__":
    main()
