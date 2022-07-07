"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def _ingresar_n():
    while True:
        n = input("Número: ")
        try:
            n = int(n)
            if n > 0:
                return int(n)
            print("El número debe ser positivo")
        except ValueError:
            print("Ingresar solo números")


def _es_multiplo(a, b):
    return a % b == 0


def _es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    return False


def multiplo():
    x = 5
    n = _ingresar_n()
    if _es_multiplo(n, x):
        print(f"{n} es múltiplo de {x}")
    else:
        print(f"{n} no es múltiplo de {x}")


def perfecto():
    n = _ingresar_n()
    if _es_perfecto(n):
        print(f"{n} es un número perfecto")
    else:
        print(f"{n} no es un número perfecto")


def menu():
    while True:
        print("\nMenú")
        print("1.- Obtener multiplo")
        print("2.- Obtener número perfecto")
        print("3.- Salir")
        opcion = input("\nIngresar opción > ")
        if opcion not in "123":
            print("Opción inválida")
        else:
            return opcion


def main():
    while True:
        opcion = menu()
        if opcion == "1":
            multiplo()
        elif opcion == "2":
            perfecto()
        elif opcion == "3":
            print("Hasta la próxima")
            break

# -------------------------------------------------------- dict version
# def main():
#     while True:
#         opcion = menu()
#         if opcion == "3":
#             print("Hasta la próxima")
#             break
#         {"1": multiplo, "2": perfecto}[opcion]()


if __name__ == "__main__":
    main()
