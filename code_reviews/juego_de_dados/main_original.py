"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint

lista_jugadores = {} # Inicializa la lista de jugadores como un diccionario vacío

def Iniciar_Jugadores (lista_jugadores:dict,num_jugadores:int): # Crea los jugadores en el diccionario

    for jugador in range(num_jugadores):

        nom_jugador = input(f" Introduzca el nombre del jugador {jugador+1}: ")
        lista_jugadores[nom_jugador] = []

def Tirar_Dados (): # Devuelve una tupla con los valores de cada dado de forma aleatoria

    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1, dado2

def Jugar (lista_jugadores:dict): # Recorre cada jugador y le asigna las puntuaciones de los dados

    for jugador in lista_jugadores:

        print(f"\n--------------------- Turno del jugador {jugador} ----------------------")
        lista_tiradas = []

        for tirada in range (6):

            if tirada <= 2: # Las tres primeras tiradas son obligadas

                resultado = Tirar_Dados()
                print (f" Tirada {tirada+1} ha obtenido los valores {resultado[0]} y {resultado[1]}")
                lista_tiradas.append(sum(resultado))
                lista_jugadores[jugador] = lista_tiradas

            else:

                if sum(lista_jugadores[jugador]) <= 50: # Siempre que no supere los 50 puntos se pregunta si se quiere tirar

                    print(f" La suma total de las tiradas del jugador {jugador} es {sum(lista_jugadores[jugador])}")
                    opc = input("\n ¿Desea volver a tirar los dados? (s/n): ")

                    if opc == "s":

                        resultado = Tirar_Dados()
                        print (f" Tirada {tirada+1} ha obtenido los valores {resultado[0]} y {resultado[1]}")
                        lista_tiradas.append(sum(resultado))
                        lista_jugadores[jugador] = lista_tiradas
                    
                    else:

                        break

        print(f" \n\t\t\t ------> Puntuación total de {jugador} es {sum(lista_jugadores[jugador])} <---- ")

def Calcular_Ganador(lista_jugadores:dict): # Ordena la lista de jugadores por la suma de sus puntos

    lista_ordenada = sorted(lista_jugadores.items(),key = lambda x: sum(x[1]), reverse=True) # ORDENA EL DICCIONARIO POR EL VALOR DE LAS TIRADAS
    # Esto devuelve una lista de tuplas con la clave y el valor, nombre y lista de tiradas
    # El primero en la lista será el vencedor siempre y cuando el valor de sus tiradas sea menor a 50
    for jugador in lista_ordenada:

        if sum(jugador[1]) <= 50:
            print("\n******************************************************************************************")
            print (f" El ganador del juego es {jugador[0]} con una puntuación de {sum(jugador[1])}")
            print("******************************************************************************************\n")
            break




Iniciar_Jugadores(lista_jugadores,3)
Jugar(lista_jugadores)
Calcular_Ganador(lista_jugadores)