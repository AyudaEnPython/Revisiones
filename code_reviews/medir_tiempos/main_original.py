"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import time
import numpy as np

lista1 = range(1000000)
lista2 = range(1000000)
array1 = np.array(range(1000000))
array2 = np.array(range(1000000))

comienzo = time.time()

resultado = [x-y for x,y in zip(lista1,lista2)]

final = time.time()

print("tiempo: " + str(final-comienzo))

comienzo = time.time()

resultado = array1-array2
final = time.time()

print("tiempo" + str(final-comienzo))