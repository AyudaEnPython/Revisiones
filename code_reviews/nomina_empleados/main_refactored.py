"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def alta_empleados(n: int, nomina: dict) -> None:
    for i in range(n):
        nombre = input(f"Nombre del empleado {i + 1}: ")
        nomina[nombre] = []


def ingresar_nominas(nomina: dict) -> None:
    for empleado in nomina:
        semanas = int(input(f"¿Cuántas semanas ha trabajado {empleado}?: "))
        for semana in range(semanas):
            horas = int(input(
                f"¿Cuántas horas ha trabajado la semana {semana + 1}?: "
            ))
            nomina[empleado].append(horas)


def calcular_salario(nomina: dict, base: int = 10_000) -> None:
    for empleado, horas in nomina.items():
        print(
            f"El total del coste de la nómina de {empleado} es "
            f"{sum(horas) * base}"
        )


def gastos_por_semana(nomina: dict, base: int = 10_000) -> None:
    for semana in range(max(len(horas) for horas in nomina.values())):
        total_horas = 0
        for empleado in nomina:
            if semana < len(nomina[empleado]):
                total_horas += nomina[empleado][semana]
        print(
            f"El gasto de la empresa en la semana {semana + 1} es "
            f"{total_horas * base}"
        )


def main():
    nominas = {}
    num_empleados = int(input("¿Cuántos empleados tiene la empresa?: "))
    alta_empleados(num_empleados, nominas)
    ingresar_nominas(nominas)
    calcular_salario(nominas)
    gastos_por_semana(nominas)


if __name__ == "__main__":
    main()
