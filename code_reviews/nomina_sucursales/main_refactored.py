TITULO = "REPORTE RESUMEN"
ENCABEZADOS = ("SUCURSAL", "CÓDIGO", "EMPLEADOS", "TOTAL", "PROMEDIO")
ANCHO = 60
SEPARADOR = "-" * ANCHO
PLANTILLA = "{:<15}{:^15}{:^10}{:>10.2f}{:>10.2f}"

datos = [
    ("Barbara Ulloa", "Apoquindo", "APO-FG7543-98", 3080),
    ("Camila Crisostomo", "Alameda", "ALA-UK5327-67", 4868),
    ("Macarena Tapia", "Maipu", "MAI-PL8235-90", 4182),
    ("Romina Collantes", "Maipu", "MAI-PL8235-90", 3194),
    ("Ariel Heredia", "Apoquindo", "APO-FG7543-98", 4306),
    ("Mario Tapia", "Alameda", "ALA-UK5327-67", 3366),
    ("Gabriel Muñoz", "Alameda", "ALA-UK5327-67", 3970),
    ("Ariel Heredia", "San Bernardo", "SAN-PWJ123-78", 4034),
    ("Nataly Adonis", "La Florida", "FLO-YDHU425-98", 4629),
    ("Sebastian Collantes", "Quilicura", "QUI-THU765-98", 3496),
    ("Barbara Rebolledo", "San Bernardo", "SAN-PWJ123-78", 4174),
    ("Enrique Zuñiga", "Alameda", "ALA-UK5327-67", 4223),
    ("Miriam Becerra", "Apoquindo", "APO-FG7543-98", 3836),
    ("Gerson Fuentes", "Maipu", "MAI-PL8235-90", 4930),
    ("Victor Parra", "Maipu", "MAI-PL8235-90", 4774),
    ("Mirna Cuevas", "Apoquindo", "APO-FG7543-98", 3664),
    ("Katherina Irrazaba", "La Florida", "FLO-YDHU425-98", 3080),
    ("Cinthia Abarca", "San Bernardo", "SAN-PWJ123-78", 4253),
]

resumen = []
total_empleados = 0
total_sueldos = 0
for _, sucursal, codigo, sueldo in datos:
    for item in resumen:
        if item[0] == sucursal:
            item[2] += 1
            item[3] += sueldo
            item[4] = item[3] / item[2]
            break
    else:
        resumen.append([sucursal, codigo, 1, sueldo, sueldo])
    total_empleados += 1
    total_sueldos += sueldo
promedio_general = total_sueldos / total_empleados
resumen.sort(key=lambda x: x[0])

print(SEPARADOR)
print(TITULO.center(ANCHO))
print(SEPARADOR)
print("{:^15}{:^15}{:^10}{:>10}{:>10}".format(*ENCABEZADOS))
print(SEPARADOR)
for item in resumen:
    print(PLANTILLA.format(*item))
print(SEPARADOR)
print(PLANTILLA.format("TOTAL", "", total_empleados, total_sueldos, promedio_general))
print(SEPARADOR)