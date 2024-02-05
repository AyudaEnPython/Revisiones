"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import choices
from string import ascii_letters, punctuation, digits

MINIMO = 8


def generate_password(length):
    return "".join(choices(ascii_letters + punctuation + digits, k=length))


def main():
    while True:
        usuario = input("Ingresar nombre de usuario ('exit' para salir): ")
        if usuario == "exit":
            break
        longitud = len(usuario)
        if longitud < MINIMO:
            print(
                f"El nombre de usuario debe tener un mínimo de 8 caracteres, "
                f"el nombre ingresado tiene {len(usuario)} caracteres"
            )
        else:
            password = generate_password(longitud)
            print(f"Usuario: {usuario}")
            print(f"Contraseña: {password}")


if __name__ == "__main__":
    main()
