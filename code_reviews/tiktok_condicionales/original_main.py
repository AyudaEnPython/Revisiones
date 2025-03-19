"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
print("Vamos a calcular si eres famoso en titok")
nombre = input("Cual es tu nombre? R= ")

# VARIABLES
seguidores = input("Digite los seguidores que tiene en Tiktok "+nombre+" R= ")
siguiendo = input("Digite las personas que siguen en Tiktok"+nombre+" R= ")
likes = input("Digite el numero de me gusta que tiene"+nombre+" R= ")



fam = seguidores-siguiendo
famalike = float(input(fama*likes))

if fam > 0:
    print("CALCULANDO FAMA")
    print("TU PORCENTAJE DE FAMA ES IGUAL A = " + fam + "*")
else:
    print("TIENES MAS SEGUIDOS QUE SEGUIDORES, ERES UN PERDEDOR")
    print(" Fin del programa")

# CONTROLAR DECIMALES USAR LA VARIABLE round(x, DECIMALES)