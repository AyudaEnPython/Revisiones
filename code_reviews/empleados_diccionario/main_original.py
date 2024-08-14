"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
empleados = {
    "Carlos": {'departamento': 'Ventas', "salario": 2000},
    "Ana": {'departamento': 'Marketing', "salario": 2500},
    "Luis": {'departamento': 'IT', "salario": 3000},
}

#funcion
def actualizar_salario(nombre, nuevo_salario):
    if nombre in empleados:
        empleados[nombre]['salario'] = nuevo_salario
        return f"El salario de {nombre} ha sido actualizado a {nuevo_salario}."
    return None

#salario actual
print(empleados)

#llamamos a la funcion
nombre_empleado = input("Empleado: ")
nuevo_salario = int(input("Nuevo salario: "))
outcome = actualizar_salario(nombre_empleado, nuevo_salario)

#Imprimimos
if outcome:
    print(outcome)
    print("\nDiccionario de empleados actualizado:")
    print(empleados)
else:
    print("No se encontró el empleado")

