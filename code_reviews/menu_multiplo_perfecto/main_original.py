"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
def formato(palabra):
    mensaje=""
    for x in palabra:
        mensaje=mensaje+x+"-"
    return mensaje

def menu():
    print(formato("Menú"))
    print("1.-Obtener multiplo")
    print("2.-Obtener número perfecto")
    print("3.-Salir")
    
    op=int(input("Ingrese una opción: "))
    return op

def numero_positivo(n):
    if n>0:
        return True
    else:
        return False

def multiplo(mult):
    mult=int(input("Ingrese número: "))
    if mult % 5 == 0 and mult>=1:
        print("%s es múltiplo de 5")
    else:
        print("%s no es múltiplo de 5")

def num_perfecto(numPerf):
    suma=0
    for y in range(1, numPerf):
        if (numPerf % y==0):
            suma+=y
        if numPerf==suma:
            print("%s es un número perfecto" %numPerf)
        else:
            print("%s no es un número perfecto" %numPerf)

op=menu()
while op==True:

    if op==1:
        print(formato("Obtención de múltiplo"))
        multiplo()

    elif op==2:
        numPerf = int(input("ingrese un número: "))
        num_perfecto()

    elif op==3:
        print(formato("hasta la próxima"))
        break

    else:
        print("Seleccione una opción valida")
        print("El número que ingrese debe ser positivo")
        continue