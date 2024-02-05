"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
palabra = input("Ingresa palabra: ")
dict = {}

diccionario = dict

for p in palabra:
    if p in diccionario:
        diccionario[p] += 1
    else:
        diccionario[p] = 1
    
    print(diccionario)