"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
SUCURSALES = {}
SUCURSALES_T = {}
PACIENTES = {}

TABLA = [[89, 69, "Hipotension", 1, 15],
         [129, 89, "Optima", 0, 0],
         [139, 94, "Normal", 0, 0],
         [149, 99, "Normal-Alta", 1, 10],
         [150, 99, "HTA Sistolica Aislada", 1, 20],
         [169, 109, "HTA Grado 1", 1, 10],
         [189, 119, "HTA Grado 2", 1, 20],
         [300, 300, "HTA Grado 3", 1, 50]] # Ponemos el limite "imaginario" para el máximo


def add_datos(sucursales: int, pacientes: int)-> bool:
    if sucursales < 1 or pacientes < 1:
        raise ValueError("Datos erroneos, inténtelo de nuevo")

    SUCURSALES["Total"] = sucursales
    PACIENTES["Total"] = pacientes

    return False

def add_medicamento(sucursal: int, cantidad: int) -> bool:
    if cantidad < 1:
        raise ValueError("cantidad erronea, inténtelo de nuevo")

    SUCURSALES[sucursal] = cantidad
    SUCURSALES_T[sucursal] = cantidad

    return True

def repartir(sucursal: int, cantidad: int):
    SUCURSALES[sucursal] -= cantidad

def get_min_max():
    # Creamos un nuevo diccionaro en base a SUCURSALES pero ordenado
    dict_ord = {key: val for key, val in sorted(SUCURSALES.items(), key=lambda dato: dato[1])}
    # Lo convertimos  a lista para obtener el mínimo y máximo
    lista = list(dict_ord.items())

    min = lista[0]
    max = lista[-1]

    return min, max

def calc_porcentaje(total: int, valor: int):
    porcentaje = (valor * 100) / total

    return round(100 - porcentaje, 2)


def add_paciente(paciente: int, sucursal: int, sistolica: int, diastolica: int):

    datos = []
    for diagnostico in TABLA:
        if sistolica <= diagnostico[0] and diastolica <= diagnostico[1]:
            # print(diagnostico[2]) # Descomentar para debug, mostrará el nombre del diagnostico
            datos.extend([sucursal,
                          diagnostico[2], # Nombre del Diagnostico ejem. HTA Grado 1
                          diagnostico[3], # Tipo de Medicamento
                          diagnostico[4]  # Dosis
                          ])

            break

    PACIENTES[paciente] = datos

def main():

    seguir = True
    is_datos = False
    is_med = False
    while seguir:
        try:
            if is_datos == False:
                c_sucursales, c_pacientes = [int(dato) for dato in (input("Ingrese datos: ").split())]
                seguir = add_datos(c_sucursales, c_pacientes)
            is_datos = True

            #Agregamos uno por uno la informacion de la sucursal
            if is_med == False:
                for sucursal in range(1, SUCURSALES["Total"] + 1):
                    cantidad = int(input(f"S{sucursal}: "))
                    seguir = add_medicamento(sucursal, cantidad)
            is_med = True

            break

        except ValueError as error:
            print(error)

    # Agregamos uno por uno la información del paciente
    for paciente in range(1, PACIENTES["Total"] + 1):
        sucursal, p_sis, p_dias = [int(dato) for dato in (
            input(f"Paciente {paciente}: ").split())]
        add_paciente(paciente, sucursal, p_sis, p_dias)

    # Quitamos los medicamentos utilizados
    for paciente, diagnostico in PACIENTES.items():
        if not paciente == "Total":
            repartir(diagnostico[0], diagnostico[3])

    SUCURSALES.pop("Total") # Eliminamos el elemento, ya no sirve y causará problemas
    min, max = get_min_max()
    print(min[0], min[1])
    print(max[0], max[1])

    for sucursal, cantidad in SUCURSALES.items():
        porcent = calc_porcentaje(SUCURSALES_T[sucursal], cantidad)
        print(f"{sucursal} {porcent}%")


if __name__ == "__main__":
    main()