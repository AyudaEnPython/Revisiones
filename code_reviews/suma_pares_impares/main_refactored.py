"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
suma_pares = suma_impares = k = 0

n = int(input("Ingresar la cantidad de números: "))

for i in range(n):
    x = int(input(f"Ingresar el número ({i+1}): "))
    if x % 2 == 0:
        suma_pares += x
        k += 1
    else:
        suma_impares += x

promedio_pares = suma_pares / k if k > 0 else 0
promedio_impares = suma_impares / (n - k) if k < x else 0

print("\nResultados:")
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
print(f"Promedio de números pares: {promedio_pares:.2f}")
print(f"Promedio de números impares: {promedio_impares:.2f}")
