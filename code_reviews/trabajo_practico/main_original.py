"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
''' Utilizando funciones'''
######################################################
'''
1- Construya un programa en Python tal que, dado como datos la base y la
altura de un rectángulo, calcule el perímetro y la superficie de este.
'''
def calc_perimetro_superficie_rectangulo(base, altura):
    print(f"Base: {base}\nAltura: {altura}\n-----------")
    print(f"Perímetro: {2*(base+altura)}")
    print(f"Superficie: {base*altura}")
calc_perimetro_superficie_rectangulo(2, 3)    # descomentar para testing

'''
2- Elaborar un algoritmo que permita ingresar el número de partidos ganados,
perdidos y empatados, por ABC club en el torneo apertura, se debe de mostrar
su puntaje total, teniendo en cuenta que por cada partido ganado obtendrá 3
puntos, empatado 1 punto y perdido 0 puntos.
'''
def puntaje_torneo_apertura(clubes = ['A', 'B', 'C']):
    if not len(clubes) == 3: exit(f"Maximo 3 clubes.")
    puntajes = {clubes[0]: 0, clubes[1]: 0, clubes[2]: 0}
    index = 0
    index_abversario = 0
    for i in range(1, 4):
        if index_abversario == 2:
            index = 2
            index_abversario = 0
        print(f"Partido {i}: {clubes[index]} vs {clubes[index_abversario+1]}")
        resultado = int(input("** Resultados:\n1- Gana\n2- Empate\n- "))
        if resultado == 1:
            club_ganador = int(input(f"** Club ganador:\n1- {clubes[index]}\n2- {clubes[index_abversario+1]}\n- "))
            if club_ganador == 1:
                puntajes[clubes[index]] = puntajes[clubes[index]] + 3
                puntajes[clubes[index_abversario+1]] = puntajes[clubes[index_abversario+1]] + 0
            else:
                puntajes[clubes[index]] = puntajes[clubes[index]] + 0
                puntajes[clubes[index_abversario+1]] = puntajes[clubes[index_abversario+1]] + 3
        else:
            puntajes[clubes[index]] = puntajes[clubes[index]] + 1
            puntajes[clubes[index_abversario+1]] = puntajes[clubes[index_abversario+1]] + 1    
        index_abversario = index_abversario + 1
    print(puntajes)
# puntaje_torneo_apertura(['Linux','Mac', 'Windows'])    # descomentar para testing

'''
3- Dado un sueldo de un trabajador, aplique un aumento del 15% si su sueldo
es inferior a $1000. Imprima el sueldo que percibirá.
'''
def actualizar_sueldo(sueldo_actual):
    if sueldo_actual < 1000:
        print(f"Su sueldo se actualizará con un plus del 15%.")
        print(f"Sueldo actual: ${sueldo_actual}.")
        print(f"Sueldo actualizado: ${int(sueldo_actual + sueldo_actual*.15)}.")
    else:
        print(f"Sueldo estable: ${sueldo_actual}.")
# actualizar_sueldo(300)    # descomentar para testing
# actualizar_sueldo(999)    # descomentar para testing
# actualizar_sueldo(1000)    # descomentar para testing
# actualizar_sueldo(1200)    # descomentar para testing

'''
4- Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) y
se desea visualizar si el número es par o impar
'''
def par_o_impar():
    database = {}
    print("Ingrese 10 números.")
    for i in range (10):
        n = int(input(f"{i+1}- Ingrese N°: "))
        if n%2 == 0:
            print(f"{n} es par.")
            database[n] = 'par' 
        else:
            print(f"{n} es impar.")
            database[n] = 'impar'
    print(database)
# par_o_impar()    # descomentar para testing
    
'''
5- Modifique el programa anterior para que se puedan ingresar varios números
diciendo si cada uno de ellos es par o no. La ejecución del programa finalizará
cuando se ingrese un 0 (cero).
'''
def par_o_impar():
    database = {}
    print("Ingrese N números, para terminar el programa ingrese el número 0 (cero).")
    i = 0
    while True:
        n = int(input(f"{i+1}- Ingrese N°: "))
        if n == 0: break
        if n%2 == 0:
            print(f"{n} es par.")
            database[n] = 'par' 
        else:
            print(f"{n} es impar.")
            database[n] = 'impar'
        i = i + 1
    print(database)
# par_o_impar()    # descomentar para testing
    
'''
6- Modifique el programa 6 para que aparte de hacer lo que ya hace,
me informe al final del proceso cuántos números fueron pares, cuántos impares
y cuántos números se ingresaron en total.
** Observacion -> Modifique el programa 5 (anterior) 
'''
def par_o_impar():
    database = {}
    print("Ingrese N números, para terminar el programa ingrese el número 0 (cero).")
    i = 0
    pares = 0
    impares = 0
    while True:
        n = int(input(f"{i+1}- Ingrese N°: "))
        if n == 0: break
        if n%2 == 0:
            print(f"{n} es par.")
            pares = pares + 1
            database[n] = 'par' 
        else:
            print(f"{n} es impar.")
            database[n] = 'impar'
            impares = impares + 1
        i = i + 1
    print(f"Total de números ingresados {i}.")
    print(f"Total números pares: {pares}")
    print(f"Total números impares: {impares}")
    print(database)
# par_o_impar()    # descomentar para testing

'''
7- Ingresar por teclado 100 números enteros y calcular cuántos de ellos son
pares. Se debe imprimir el resultado de la suma de los pares y el resultado de
la suma de los impares 
'''
import random
def generador_random_numeros_enteros(start, end):
    return int(random.randrange(start, end))

def par_o_impar():
    database = {}
    print("Ingrese 100 números.")
    i = 0
    pares = 0
    impares = 0
    for i in range(100):
        # n = int(input(f"{i+1}- Ingrese N°: ")) # descomentar para ingresar datos manualmente
        n = generador_random_numeros_enteros(1, 100)  # genera automaticamente numeros enteros
        if n%2 == 0:
            print(f"{n} es par.")
            pares = pares + n
            database[n] = 'par' 
        else:
            print(f"{n} es impar.")
            database[n] = 'impar'
            impares = impares + n
        i = i + 1
    print(f"Total de números ingresados {i}.")
    print(f"Suma total de pares: {pares}")
    print(f"Suma total de impares: {impares}")
    print(database)
# par_o_impar()    # descomentar para testing

'''
8- Escribir un algoritmo que imprima los 10 primeros números pares
comenzando en 2 e imprima también sus respectivos valores elevados al
cuadrado y al cubo. Por ejemplo: valor: 2, cuadrado: 4, cubo: 8, valor: 4,
cuadrado: 16, cubo: 64 ...
'''
def xyz():
    contador = 0 
    valor = 2
    while True:
        if valor%2 == 0:
            print(f"Valor: {valor}, cuadrado: {valor**2}, cubo: {valor**3}")
            contador = contador + 1
        valor = valor + 1
        if contador == 10: break
# xyz()    # descomentar para testing