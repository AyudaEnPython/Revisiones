"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

def passCreator(longitud):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
    simbolos = ["$","*","@","%","/"]
    randomPass = letras + simbolos
    passWord = ""
    for letra in range(longitud):
        passWord += random.choice(randomPass)
    return passWord

while True:
    print("REGISTRO".center(50,"-"))
    print()
    usuario = input("Usuario a crear: ").strip().upper()
    contra = passCreator(10)
    if len(usuario) != 8:
        print(f"Debes tener mínimo 8 caracteres, el usuario ingresado tiene {len(usuario)}\n")
    else:
        print()
        print(f"Usuario generado: {usuario}")
        print(f"Tu contraseña automática es: {contra}")
        f = open("password.txt", "a+")
        f.write(f"{usuario}: {contra}\n")
        f.close()