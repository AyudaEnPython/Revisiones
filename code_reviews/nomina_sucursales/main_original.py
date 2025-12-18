###########################################
# Curso         : Programacion Básica para Redes
# Objetivo      :Reporte resumen
# Núm. Ejerc.   : 1
###########################################

# INGRESO
titulo = "REPORTE RESUMEN"
datos = [
    ["Barbara Ulloa", "Apoquindo", "APO-FG7543-98", 3080],
    ["Camila Crisostomo", "Alameda", "ALA-UK5327-67", 4868],
    ["Macarena Tapia", "Maipu", "MAI-PL8235-90", 4182],
    ["Romina Collantes", "Maipu", "MAI-PL8235-90", 3194],
    ["Ariel Heredia", "Apoquindo", "APO-FG7543-98", 4306],
    ["Mario Tapia", "Alameda", "ALA-UK5327-67", 3366],
    ["Gabriel Muñoz", "Alameda", "ALA-UK5327-67", 3970],
    ["Ariel Heredia", "San Bernardo", "SAN-PWJ123-78", 4034],
    ["Nataly Adonis", "La Florida", "FLO-YDHU425-98", 4629],
    ["Sebastian Collantes", "Quilicura", "QUI-THU765-98", 3496],
    ["Barbara Rebolledo", "San Bernardo", "SAN-PWJ123-78", 4174],
    ["Enrique Zuñiga", "Alameda", "ALA-UK5327-67", 4223],
    ["Miriam Becerra", "Apoquindo", "APO-FG7543-98", 3836],
    ["Gerson Fuentes", "Maipu", "MAI-PL8235-90", 4930],
    ["Victor Parra", "Maipu", "MAI-PL8235-90", 4774],
    ["Mirna Cuevas", "Apoquindo", "APO-FG7543-98", 3664],
    ["Katherina Irrazaba", "La Florida", "FLO-YDHU425-98", 3080],
    ["Cinthia Abarca", "San Bernardo", "SAN-PWJ123-78", 4253]
]

print(" "*30, titulo)
print("-"*80)
print("{:^14}{:^15}{:^12}{:^15}{:^12}".format(
    "SUCURSAL", "CÓDIGO", "CANT.EMPL.", "SUMA SUELDOS", "PROM SUELDOS"))
print("-"*80)

sumaSueldo = 0
cantEmplea = 0
numEmplead = 0
sumSueldos = 0
promSueldo = 0
for x in datos:
    if x[1] == "Apoquindo":
        sumaSueldo += x[3]
        cantEmplea += 1
numEmplead += cantEmplea
sumSueldos += sumaSueldo
promSueldo += (sumaSueldo/cantEmplea)
print("{:<14}{:^15}{:^12}{:>12.2f}{:>12.2f}".format("Apoquindo",
"APO-FG7543-98", cantEmplea, sumaSueldo, sumaSueldo/cantEmplea))
sumaSueldo = 0
cantEmplea = 0
for x in datos:
    if x[1] == "Alameda":
        sumaSueldo += x[3]
        cantEmplea += 1
numEmplead += cantEmplea
sumSueldos += sumaSueldo
promSueldo += (sumaSueldo/cantEmplea)
print("{:<14}{:^15}{:^12}{:>12.2f}{:>12.2f}".format(
    "Alameda", "ALA-UK5327-67", cantEmplea, sumaSueldo, sumaSueldo / cantEmplea))
sumaSueldo = 0
cantEmplea = 0
for x in datos:
    if x[1] == "San Bernardo":
        sumaSueldo += x[3]
        cantEmplea += 1
numEmplead += cantEmplea
sumSueldos += sumaSueldo
promSueldo += (sumaSueldo/cantEmplea)
print("{:<14}{:^15}{:^12}{:>12.2f}{:>12.2f}".format("San Bernardo",
"SAN-PWJ123-78", cantEmplea, sumaSueldo, sumaSueldo / cantEmplea))
sumaSueldo = 0
cantEmplea = 0
for x in datos:
    if x[1] == "La Florida":
        sumaSueldo += x[3]
        cantEmplea += 1
numEmplead += cantEmplea
sumSueldos += sumaSueldo
promSueldo += (sumaSueldo / cantEmplea)
print("{:<14}{:^15}{:^12}{:>12.2f}{:>12.2f}".format("La Florida",
"FLO-YDHU425-98", cantEmplea, sumaSueldo, sumaSueldo / cantEmplea))

print("-"*80)
print("{:<14}{:^15}{:^12}{:>12.2f}{:>12.2f}".format(
    "", "TOTAL", numEmplead, sumSueldos, promSueldo))
print("-"*80)

"""
CONCLUSIÓN:

Se concluye que las tuplas y listas permiten almacenar diferentes tipos de
datos en un solo grupo. Su principal diferencia es que las listas son mutables,
algo que las hace más flexibles, mientras que las tuplas son inmutables,
lo que las hace más rápidas.
"""
input()
