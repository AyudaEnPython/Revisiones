"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

cantidad_alumnos =int(input("introduzca cantidad alumnos: "))
cantidad_notas =int(input("introduzca cantidad notas: "))
for num in range(cantidad_alumnos):
    alumno=input("nombre del alumno: ")

n=[]
mayor =0
menor =0
R=1
while (cantidad_notas > 0):
    notas = float(input("nota #" + str(R)+ ":"))
    n.append(notas)
    R = R + 1
    cantidad_notas = cantidad_notas - 1

mayor = max(n)
menor = min(n)

print("\n")
print("notas", alumno, ":", n)
print("nota mayor: ", mayor)
print("nota menor: ", menor)