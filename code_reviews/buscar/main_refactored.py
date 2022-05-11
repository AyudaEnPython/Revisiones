"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add typing and main function later...
"""

empleados = [
    "Juan Pérez",
    "Pedro Páramo",
    "María Contreras",
    "Felipe Saavedra",
]


def buscar(palabra, empleados):
    for empleado in empleados:
        if empleado.find(palabra) != -1:
            return empleado
    return f"No se encontró {palabra}"


print(buscar("Juan", empleados))
