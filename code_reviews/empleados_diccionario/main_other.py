"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from empleados import EMPLEADOS


def main():
    empleado = ingresar_empleado()
    nuevo_salario = ingresar_nuevo_salario() 
    EMPLEADOS[empleado]["salario"] = nuevo_salario
    print("Diccionario de empleados actualizado:", EMPLEADOS)


def ingresar_empleado():
    while True:
        empleado = input("Empleado: ") or exit()
        if empleado in EMPLEADOS:
            return empleado
        print("No se encontró el empleado")


def ingresar_nuevo_salario():
    while True:
        try:
            nuevo_salario = int(input("Nuevo salario: ")) or exit()
            return nuevo_salario
        except ValueError:
            print("Salario inválido")


if __name__ == "__main__":
    main()