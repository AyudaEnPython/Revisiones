"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from string import ascii_letters, punctuation

ALLOWED = ascii_letters + "ÁÉÍÓÚáéíóúü"
NOT_ALLOWED = punctuation + " "
letras = {}

palabra = input("Ingresar palabra: ")

for letra in palabra:
    if letra in NOT_ALLOWED:
        continue
    if letra not in letras and letra in ALLOWED:
        letras[letra] = 1
    else:
        letras[letra] += 1

for letra, frecuencia in letras.items():
    print(
        f"La letra {letra} aparece {frecuencia} "
        f"{'vez' if frecuencia == 1 else 'veces'}."
    )
