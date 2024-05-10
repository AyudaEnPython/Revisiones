"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import time
import random

def introduccion():
    print("*************************************")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*             CRODEMY               *")
    time.sleep(2)
    print("*        Software Development       *")
    time.sleep(2)
    print("*             presenta              *")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*************************************")
    time.sleep(2)
    print("*************************************")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*            el juego de            *")
    time.sleep(2)
    print("*        Mayores, Menores y 7       *")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*************************************")
    time.sleep(2)
    print("*************************************")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*            creación de            *")
    time.sleep(2)
    print("*            Adamarys Jimenez       *")
    time.sleep(2)
    print("*                                   *")
    time.sleep(2)
    print("*************************************")

def instrucciones():
    ver_instrucciones = input("Ver instrucciones <y/n> : ")
    if ver_instrucciones.lower() == "y":
        print("En el juego puede lanzar dos dados y apostar al resultado. Puede apostar a mayores que 7, menores que 7 o al 7. Si acierta con mayores o menores recibe el doble de la cantidad que apostó. Si gana con el 7 recibe el triple de lo que apostó.\n")
        time.sleep(2)
        ver_mas = input("Continuar con instrucciones <y/n> : ")
        if ver_mas.lower() == "y":
            print("Por ejemplo, si apuesta 5 puntos a los mayores y gana entonces recibe 5 más y tiene 10. Si apuesta al 7 y gana entonces recibe 10 más y tiene 15. El jugador comienza con 20 puntos y las apuestas no pueden ser de más de 3 puntos. Pierde cuando se queda sin puntos y gana cuando llega a 30.\n")
            time.sleep(2)

def proximaApuesta(puntos):
    cantidad_valida = False
    while not cantidad_valida:
        apuesta = int(input("Cantidad a apostar: "))
        if apuesta < 1 or apuesta > 3:
            print("No puede apostar esa cantidad")
        elif apuesta > puntos:
            print("No tiene suficientes puntos para realizar esa apuesta")
        else:
            cantidad_valida = True
    tipoApuesta = input("A qué apuesta? <mayores/menores/7> : ")
    while tipoApuesta.lower() not in ["mayores", "menores", "7"]:
        print("Opción no válida.")
        tipoApuesta = input("A qué apuesta? <mayores/menores/7> : ")
    return (apuesta, tipoApuesta.lower())

def lanzarDados():
    dado0 = random.randint(1, 6)
    dado1 = random.randint(1, 6)
    return [dado0, dado1]

def mostrarDosDados(dado0, dado1):
    asteriscos_dado0 = random.randint(0,2)
    asteriscos_dado1 = random.randint (0,2)

    print("---  ---  ")
    print("|{}| | {} |".format("*" * asteriscos_dado0 if dado0 < 7 else " ", "*" * asteriscos_dado1 if dado1 < 7 else " "))
    print("|{}| | {} |".format("*" * asteriscos_dado0 if dado0 < 7 else " ", "*" * asteriscos_dado1 if dado1 < 7 else " "))
    print("|{}| | {} |".format("*" * asteriscos_dado0 if dado0 < 7 else " ", "*" * asteriscos_dado1 if dado1 < 7 else " "))
    print("---  ---  ")

def resultadoDeApostar(puntos, apuesta, tipoApuesta, dado0, dado1):
    suma_dados = dado0 + dado1

    if tipoApuesta == "mayores":
        if suma_dados > 7:
            puntos += 2 * apuesta
            print("¡Acertaste en tu apuesta!")
        else:
            puntos -= apuesta
            print("No acertaste en tu apuesta. Se te restan {} puntos".format(apuesta))

    if tipoApuesta == "menores":
        if suma_dados < 7:
            puntos += 2 * apuesta
            print("¡Acertaste en tu apuesta!")
        else:
            puntos -= apuesta
            print("No acertaste en tu apuesta. Se te restan {} puntos".format(apuesta))

    if tipoApuesta == "7":
        if suma_dados == 7:
            puntos += 3 * apuesta
            print("¡Acertaste en tu apuesta!")
        else:
            puntos -= apuesta
            print("No acertaste en tu apuesta. Se te restan {} puntos".format(apuesta))

    print("Actualmente tienes {} puntos".format(puntos))
    return puntos

def determinarStatus(puntos):
    if puntos >= 30:
        print("*******************")
        print("*                 *")
        print("*  Ganaste el juego  *")
        print("*                 *")
        print("*******************")
        return False
    elif puntos <= 0:
        print("*******************")
        print("*                 *")
        print("* Perdiste el juego *")
        print("*                 *")
        print("*******************")
        return False
    else:
        return True

def main():
    #introduccion()
    instrucciones()
    puntos = 20
    continuar = True
    while continuar:
        resultadoApuesta = proximaApuesta(puntos)
        apuesta = resultadoApuesta[0]
        tipoApuesta = resultadoApuesta[1]
        dados = lanzarDados()
        mostrarDosDados(dados[0], dados[1])
        puntos = resultadoDeApostar(puntos, apuesta, tipoApuesta, dados[0], dados[1])
        continuar = determinarStatus(puntos)

main()