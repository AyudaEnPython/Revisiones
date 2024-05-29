"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
while True:
    print("¿Le gustaría dejar propina?\n1. Si\n2. No")
    respuesta = input("> ")
    if respuesta == "2":
        break
    elif respuesta == "1":
        while True:
            print("¿Qué porcentaje le gustaría dejar?")
            print("1. 10%\n2. 20%\n3. 30%\n4. 40%\n5. 50%")
            respuesta = input("> ")
            if respuesta == "1":
                print("Gracias por esos 10%!")
                break
            elif respuesta == "2":
                print("Gracias por esos 20%!")
                break
            elif respuesta == "3":
                print("Gracias por esos 30%!")
                break
            elif respuesta == "4":
                print("Gracias por esos 40%!")
                break
            elif respuesta == "5":
                print("Gracias por esos 50%!")
                break
            else:
                print("¡Opción inválida! Presionar del '1' al '5'")
        break
    else:
        print("¡Opción inválida! Presionar '1' o '2'")
print("¡Que tenga un buen día!")
