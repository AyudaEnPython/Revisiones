"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
while True:
    import math
    print("""
    1) Area y perimetro
    2) Salir""")

    numeros = int(input("Ingrese una opcion por favor: "))

    if numeros ==1:
        radio= float(input("Ingrese el radio del circulo: "))
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio

        print("Los resultados del area y perimetro son: ")
        print("el radio del circulo es: ", radio)
        print("El area del circulo es: ", area)
        print("El perimetro del circulo es: ",perimetro)
    
    if numeros ==2:
        print("!Gracias por utilizar el programa, vuelve pronto...")
        break

