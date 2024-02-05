"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
def Alta_Empleados(n:int, nomina:dict): # Agrega n empleados a las nominas de la empresa

    for persona in range(n):

        nomina[input(f" Introduce el nombre del empleado {persona+1}: ")] = [] # Crea un nuevo empleado con clave el nombre y valor una lista vacía

def Ingresar_Nominas (nomina:dict): # Crea la lista con las horas trabajadas por cada empleado en cada semana

    for empleado in nomina:

        semanas = int(input(f" ¿Cuantas semanas ha trabajado {empleado}?: "))

        for semana in range(semanas):

            horas = int(input(f" ¿Cuantas horas ha trabajado la semana {semana+1}?:"))
            nomina[empleado].append(horas)

def Calcular_Salario (nomina:dict): # Calcula el salario de cada empleado

    for empleado in nomina:

        print(f" El total del coste de la nómina de {empleado} es {sum(nomina[empleado]*10000)}")

def Gasto_x_Semana (nomina:dict): # Calcula el gasto de la empresa por cada semana
    # Dado que cada trabajador habrá empleado un número de semanas diferentes para trabajar
    # habrá que tener en cuenta esto para extraer ese dato de cada lista (la cual cada una es de una longitud)
    # por tanto intentamos sumar en la lista destino suma_x_semanas lo que hay en una posición determinada
    # si no es posible realizar esa operación es que el elemento no existe, por tanto lo damos de alta con append
    # Finalmente se imprime la lista resultante suma_x_semanas multiplicando cada valor por 10000

    suma_x_semanas = []

    for empleado in nomina:

        for semana in range(len(nomina[empleado])): 

            try:
                suma_x_semanas[semana] += nomina[empleado][semana]

            except:

                suma_x_semanas.append(nomina[empleado][semana])
    
    for semana in range(len(suma_x_semanas)):

        print(f" EL gasto de la empresa en la semana {semana +1} es {suma_x_semanas[semana]*10000}")



nominas = {}
num_empleados = int(input(" ¿Cuántos empleados tiene la empresa?: "))

Alta_Empleados(num_empleados,nominas)
Ingresar_Nominas(nominas)
Calcular_Salario(nominas)
Gasto_x_Semana(nominas)