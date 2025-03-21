"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
print("Vamos a restablecer su contraseña")
PSW_NEW = str(input("Digite su nueva contraseña"))

if (len(PSW_NEW) <= 6):
                print("Tu contraseña es muy corta, agregar mas carácteres para continuar")
                PSW_NEW = str(input("Digite su nueva contraseña"))
elif (len(PSW_NEW) > 9):
                print("Tu contraseña es segura")
                print("Estas seguro que desea dejar su contraseña como : ", PSW_NEW)
else:
                print("Hola mundo")