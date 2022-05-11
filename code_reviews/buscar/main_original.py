"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

lista_de_empleados = ["Juan Pérez","Pedro Páramo","María Contreras","Felipe Saavedra"]

def nombre_a_partir_de_apellido(lista_empleados, apellido):
    for i in lista_empleados:
        if i.find(apellido)>0:
            return i

print(nombre_a_partir_de_apellido(lista_de_empleados,"Pérez"))