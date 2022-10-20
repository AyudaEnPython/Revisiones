"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

datos = []

x = int(input("Cantidad de alumnos: "))
n = int(input("Cantidad de notas: "))

for i in range(x):
    notas = []
    print(f"Estudiante N°{i+1}")
    nombre = input("Nombre: ")
    for j in range(n):
        nota = float(input(f"Nota N°{j+1}: "))
        notas.append(nota)
    datos.append([
        nombre, min(notas), max(notas), sum(notas)/n
    ])

print("\nResultados:\n")
for alumno, min_, max_, mean_ in datos:
    print(f"Nombre: {nombre} | min: {min_} | max: {max_} | promedio: {mean_}")
