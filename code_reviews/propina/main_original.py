"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
while True:
    respu = input("Gusta dejar alguna propina como agradecimiento?"
    "1.Si/2.No ")
    if respu.lower() == "1":
        print("ok, muchas gracias!")
        break
    elif respu.lower() == "2":
        print("ok, muchas gracias!")
        break
    else:
        print("Respuesta invalida, porfavor responda 1 o 2")

if respu.lower() == "1":
    print("Cuanto porcentaje le gustaria dejar?")
elif respu.lower() == "2":
    print("Pase buen dia")

while True:
    respuesta2 = input("Opciones"
    "1.10% 2.20% 3.30% 4.40% 5.50%: ")
    if respuesta2 == "1":
        print("Gracias por esos 10%!")
        break
    if respuesta2 == "2":
        print("Gracias por esos 20%!")
        break
    if respuesta2 == "3":
        print("Gracias por esos 30%!")
        break
    if respuesta2 == "4":
        print("Gracias por esos 40%!")
        break
    if respuesta2 == "5":
        print("Gracias por esos 50%!")
        break