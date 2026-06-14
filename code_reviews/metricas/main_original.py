import statistics
# Definir funcion para procesar los datos
def calcular_metricas():
    # Lista de numeros enteros de entrada
    valores = [12, 15, 12, 18, 21, 24, 27, 30, 33, 12]
    # Calcular la media aritmetica
    media = statistics.mean(valores)
    # Obtener el valor de la mediana
    mediana = statistics.median(valores)
    # Hallar el valor mas repetido
    moda = statistics.mode(valores)
    # Calcular la desviacion estandar
    ds = statistics.stdev(valores)
    print(f"Media: {media}, Med: {mediana}, Mode: {moda}, SD: {ds:.2f}")
# Ejecutar el procedimiento principal
calcular_metricas()
