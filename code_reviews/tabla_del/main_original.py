"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
def tabla_del(n):
    numero = 1
    print(' Tabla del: ', n)
    
    while numero <= 10:
        print(n, 'x', numero, '=', numero*n)
        numero += 1
    print('Fin')

tabla_del(7)