"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import * #IMPORTAMOS LA BIBLIOTECA PARA EL RANDINT
nombre1= ()
nombre2= ()
conjug1 = 0
conjug2 = 0
pts1 = 0           #Creamos contadores para cada variable acumuladora que vamos a usar
pts2 = 0
star = input("Desea jugar el juego 🎲: \nsi o no?\n") #Menu interactivo para el usuario
if star == "si":
    p1 = input("Coloque el nombre del primero jugador 🙂 : ") #Pedimos los nombres de cada usuario para hacerlo mas presentable el programa
    nombre1 = p1
    p2 = input("Coloque el nombre del segundo jugador 🙂 : ")
    nombre2 = p2
    print("Bienvenido al juego usuarios \nEl primero que llegue a la casilla 25 gana!") #Presentamos con un print el juego
    print("------------------------------------------")
    while (conjug1 <= 24) and (conjug2 < 25): #colocamos la condicion madre por asi decirlo para que no se pase de la casilla #25
        print("------------------------------------------")
        print(f"Turno de {nombre1}")
        op = input("Presione enter para tirar los dados:") #Comenzamos a pedir al usuario a que comience a tirar los dados
        if op == "":
            dadojg1 = randint(1, 6)
            print(f"El dado cayo en el {dadojg1}") #utilizamos las variables acumuladoras para que los valores vayan cambiando segun vaya avanzandp
            conjug1 = conjug1 + dadojg1  # aqui sumamos el numero de casillas
            pts1 = pts1 + dadojg1 #aqui los puntos
            print(f"{nombre1} Avanzo hasta la casilla numero {conjug1}")
            if conjug1 == 5: #creamos condiciones para cada trampa en el juego
                print("Mala suerte retrocede 4 casillas")
                conjug1 = conjug1 - 4
                print(f"Esta en la casilla numero {conjug1}")
            elif conjug1 == 10:
                print("Caiste en una trampa, retrocedes a la casilla numero 8")
                conjug1 = conjug1 - 2
                print(f"Estas en la casilla numero {conjug1}")
                print("Que suerte ganastes 3 puntos y avanza al casillero numero 13")
                conjug1 = conjug1 + 5
                pts1 = pts1 + 3                                                       #tambien condiciones para los puntos bonus de cada casilla
            elif conjug1 == 8:
                print("Que suerte ganastes 3 puntos y avanza al casillero numero 13")
                conjug1 = conjug1 + 5
                pts1 = pts1 + 3
                print(f"estas en el casillero numero {conjug1}")
            elif conjug1 == 14:
                print("Mala suerte retrocedes al casillero numero 6")
                conjug1 = conjug1 - 8
                print(f"Estas en el casillero numero {conjug1}")
            elif conjug1 == 9:
                print("Felicidades ganaste 5 puntos")
                pts1 = pts1 + 5
            elif conjug1 == 15:
                print("Tienes  suerte ganaste 5 puntos y avanzas al casillero numero 20")
                conjug1 = conjug1 + 5
                pts1 = pts1 + 5
            elif conjug1 > 25: #aqui la condicion para que no se pase de la casilla #25
                print("VAYAA!!\nTe pasaste de la casilla ganadora, vuelve a intentarlo en tu proximo turno")
                conjug1 = conjug1 - dadojg1 #restamos para que vuelva al valor anterior 
        if conjug1 < 25:  #hacemos exactamente lo mismo para el jugador 2 pero con sus variables conrespondientes
            print("------------------------------------------")
            print(f"Turno de {nombre2}")
            opc = input("Presione enter para lanzar el dado:")
            if opc == "":
                dadojg2 = randint(1, 6)
                print(f"El dado cayo en el {dadojg2}")
                conjug2 = conjug2 + dadojg2
                pts2 = pts2 + dadojg2
                print(f"{nombre2} Avanzo hasta la casilla numero {conjug2}")
            if conjug2 == 5:
                print("Mala suerte retrocede 4 casillas")
                conjug2 = conjug2 - 4
                print(f"Esta en la casilla numero {conjug2}")
            elif conjug2 == 10:
                print("Caiste en una trampa, retrocedes a la casilla numero 8")
                conjug2 = conjug2 - 2
                print(f"Estas en la casilla numero {conjug2}")
                print("Que suerte ganaste 3 puntos y avanzas al casillero numero 13")
                conjug2 = conjug2 + 5
                pts2 = pts2 + 3
            elif conjug2 == 8:
                print("Que suerte ganastes 3 puntos y avanza al casillero numero 13")
                conjug2 = conjug2 + 5
                pts2 = pts2 + 3
                print(f"Estas en el casillero numero {conjug2}")
            elif conjug2 == 14:
                print("Pesima suerte retrocede al casillero numero 6")
                conjug2 = conjug2 - 8
                print(f"Estas en el casillero numero {conjug2}")
            elif conjug2 == 9:
                print("Felicidades ganaste 5 puntos")
                pts2 = pts2 + 5
            elif conjug2 == 15:
                print("Tienes mucha suerte ganaste 5 puntos y avanzas al casillero numero 20")
                conjug2 = conjug2 + 5
                pts2 = pts2 + 5
            elif conjug2 > 25:
                print("VAYAA!!\nTe pasaste de la casilla ganadora, vuelve a intentarlo en tu proximo turno")
                conjug2 = conjug2 - dadojg2 
    print("El ganador es:")
    if conjug1 > conjug2: #Creamos condiciones fuera del bluce while para cuando termine el juego
        print(f"{nombre1} \ncon: {pts1} puntos") #imprimimos los puntos con ayuda del apostrofe "f"
        print("El segundo lugar es: ")
        print(f"{nombre2} que llego hasta la casilla numero {conjug2}\ncon: {pts2} puntos") # aqui damos los datos del segundo jugador con ayuda de las variables ya creadas
    else: #un else por si gana el otro jugador
        print(f"{nombre2}\ncon: {pts2} puntos")  #hacemos exactamente lo mismo para el otro jugador con sus respectivas variables
        print("El segundo lugar es:")
        print(f"{nombre1} que llego hasta la casilla numero {conjug1}\ncon: {pts1} puntos")
else:
    print("Juegue la proxima vez ")