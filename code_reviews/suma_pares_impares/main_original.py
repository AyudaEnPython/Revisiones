"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# Solicitar la cantidad de números a procesar
n = int(input("Ingrese la cantidad de números: "))

# Inicialización de acumuladores y contadores
suma_pares = 0
suma_impares = 0
cont_pares = 0
cont_impares = 0

# Bucle para leer n números
for i in range(n):
    num = int(input(f"Ingrese el número {i+1}: "))

    # Determinar si es par o impar y actualizar sumas y contadores
    if num % 2 == 0:
        suma_pares += num
        cont_pares += 1
    else:
        suma_impares += num
        cont_impares += 1

# Calcular promedios (evitar división entre 0)
prom_pares = suma_pares / cont_pares if cont_pares > 0 else 0
prom_impares = suma_impares / cont_impares if cont_impares > 0 else 0

# Mostrar resultados
print("\nResultados:")
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")
print(f"Promedio de números pares: {prom_pares:.2f}")
print(f"Promedio de números impares: {prom_impares:.2f}")