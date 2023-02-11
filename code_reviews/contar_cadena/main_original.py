import doctest
def contar(cadena):
    """
    Esta función recibe una cadena de caracteres y devuelve la cantidad de caracteres alfabéticos distintos en la cadena. No se distinguen mayúsculas de minúsculas ni caracteres con tilde.
    >>> contar("Aaaaáb")
    2
    >>> contar("$_12 3*")
    0
    >>> contar("Algoritmos y Programación 1")
    13
    >>> contar("Hola mundo")
    9
    >>> contar("")
    0
    """
    # Crea un conjunto para almacenar los caracteres distintos
    alfabeticos = set()
    for cadenas in cadena:
        if cadenas.isalpha():
            # Convierte el carácter a minúsculas antes de agregarlo al conjunto
            alfabeticos.add(cadenas.lower())
    # Devuelve la cantidad de caracteres alfabéticos distintos
    return len(alfabeticos)
# Ejecuta las pruebas
print(doctest.testmod())