"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: solo corregido, en cuanto a diseño hay varias cosas por mejorar. 
"""


def leer_archivo():
    datos = []
    sucursales = [" "] * 32
    with open("data.csv", "r") as f:
        lineas = f.read().splitlines()
        encabezado = lineas[0].split(",")
        for linea in lineas[1:]:
            fila = linea.split(",")
            sucursales[int(fila[5])-1] = fila[3] + " " + fila[4]
            datos.append(fila)
    return datos, sucursales, encabezado


def main():
    pacientes, centrales, columnas = leer_archivo()
    i_ge = columnas.index("gender")
    i_br = columnas.index("id_branch")
    i_ps = columnas.index("systolic_pressure")
    i_pd = columnas.index("diastolic_pressure")
    i_mq = columnas.index("medicine_quantity")
    len_med = 0
    hombres = 0
    mujeres = 0
    cant_med = 0
    input_central = input()
    for paciente in pacientes:
        if paciente[i_br] == input_central:
            entrega = False
            sis, dia = int(paciente[i_ps]), int(paciente[i_pd])
            if sis < 91 and dia < 63:
                entrega = True
            elif 91 <= sis < 134 and 63 <= dia < 77:
                entrega = False
            elif 134 <= sis < 162 and 77 <= dia < 105:
                entrega = False
            elif 162 <= sis < 188 and 105 <= dia < 119:
                entrega = True
            elif 188 <= sis < 201 and 119 <= dia < 126:
                entrega = True
            elif 201 <= sis < 214 and 126 <= dia < 146:
                entrega = True
            elif sis >= 214 and dia >= 146:
                entrega = True
            elif sis >= 152 and dia < 77:
                entrega = True
            else:
                entrega = False
            if entrega:
                if paciente[i_ge] == "m":
                    hombres += 1
                else:
                    mujeres += 1
                cant_med += int(paciente[i_mq])
                len_med += 1
    print(f"{input_central} {centrales[int(input_central)-1]}")
    print("scheduled patients")
    print(f"male {hombres}")
    print(f"female {mujeres}")
    print(f"total {hombres + mujeres}")
    print("scheduled medicine quantity")
    print(f"mean {cant_med/len_med:.2f}")
    print(f"total {cant_med}")


if __name__ == "__main__":
    main()
