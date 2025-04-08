"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#sORT ACOMODA LAS PALABRAS
import random
while True:
    Opcion = input("Quieres seguir jugando? si/no").upper()
    if Opcion == "SI":
        letra = ["robot", "sensor", "azul", "cafe", "voltaje"]
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
        p = []
        secreta = random.choice(letra)
        for intentos in range(3):
            print(f"La palabra contiene la letra: {random.choice(secreta)}")
            p.append(random.choice(secreta))
            if secreta in abc:
                p.append(abc.remove(secreta))
            palabra = input("ingresa la palabra ").lower()
            if palabra in secreta:
                print("Adivinaste")
                break
            elif intentos == 2:
                print("Demasiados intentos")
                lista = "".join(p)
                print(f"La palabra correcta era: {secreta}")
            else:
                print("Incorrecto")
    elif Opcion == "NO":
        break
    else:
        ...