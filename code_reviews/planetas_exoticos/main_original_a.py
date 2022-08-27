"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

def nombres_planetas():
    n_letras = random.randint(4, 7)
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    nombre = ""
    for i in range(n_letras):
        if i % 2 == 0: # Lugar par corresponde a vocales
            nombre = nombre + vocales[random.randint(0, 4)]
        else:
            nombre = nombre + consonantes[random.randint(0,21)]
    return nombre.capitalize()
lista_nombres = []
for i in range(10):
    lista_nombres.append(nombres_planetas())
lista_nom_ord = sorted(lista_nombres) # Lista ordenada alfabeticamente
for item in lista_nom_ord:
    print(item)