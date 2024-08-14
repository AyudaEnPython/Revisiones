"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from copy import deepcopy
from typing import Dict, Tuple, Union

Nomina = Dict[str, Dict[str, Union[str, float]]]
nomina: Nomina = {
    "1043": {"nombre": "Carlos", "departamento": "Ventas", "salario": 2000.0},
    "2038": {"nombre": "Ana", "departamento": "Marketing", "salario": 2500.0},
    "0033": {"nombre": "Luis", "departamento": "IT", "salario": 3000.0},
}


def ingresar_id(data: Nomina) -> Tuple[bool, Union[str, None]]:
    while True:
        _id = input("Id del empleado: ")
        if _id in data:
            return True, _id
        else:
            print("Empleado no encontrado. ¿Volver a intentar? (s/n)")
            if input("> ").lower() != 's':
                break
    return False, None


def ingresar_salario() -> float:
    while True:
        try:
            salario = float(input("Salario: "))
            if salario >= 0:
                return salario
            else:
                print("El salario debe ser un número positivo.")
        except ValueError:
            print("Valor inválido. Ingresar un número.")


def actualizar_salario(data: Nomina, _id: str, salario: float) -> None:
    data[_id]["salario"] = salario


def mostrar(data: Nomina, unidad: str = "$") -> None:
    print(f"{'id':>4}{'Nombre':>10}{'Departamento':>14}{'Salario':>12}")
    for k, v in data.items():
        print(
            f"{k:<4}{v['nombre']:>10}{v['departamento']:>14}"
            f"{unidad:>4}{v['salario']:>8.2f}"
        )


def main():
    empleados: Nomina = deepcopy(nomina)
    mostrar(empleados)
    ok, id_empleado = ingresar_id(empleados)
    if ok:
        assert isinstance(id_empleado, str)
        nuevo_salario = ingresar_salario()
        actualizar_salario(empleados, id_empleado, nuevo_salario)
        print("¡Nómina actualizada!")
        mostrar(empleados)
    else:
        print("No se efectuaron cambios.")


if __name__ == "__main__":
    main()
