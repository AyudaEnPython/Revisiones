"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
no_permitidos = "!\"#$%&\\\'()*+,-./:;<=>?@[]^_`{|}~©®°¦±¼½¾"

cadena = str(input("Entrada: "))
validar = map(lambda c:(c, "")[c in no_permitidos], cadena)

salida = "".join(validar)
print(salida)