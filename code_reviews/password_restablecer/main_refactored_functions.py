"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def get_password(length=8):
    while True:
        password = input("Ingresar nueva contraseña: ")
        if len(password) >= length:
            print("La contraseña es segura.")
            return password
        print("La nueva contraseña debe tener 8 o más caracteres.")


def confirm(password, new_password):
    while True:
        response = input(
            f"¿Confirma que desea establecer '{new_password}' "
            f"como su nueva contraseña? (si/no)\n> "
        ).lower()
        if response not in ("si", "no"):
            print("Ingresa 'si' o 'no'. Inténtalo de nuevo.")
            continue
        if response == "si":
            password = new_password
            print("Contraseña actualizada exitosamente")
        else:
            print("No se restablecerá la contraseña.")
        return password


def main():
    password = "12345678"
    print(f"Restablecimiento de contraseña\n{'='*30}\n")
    new_password = get_password()
    password = confirm(password, new_password)
    print(f"Contraseña: {password}")


if __name__ == "__main__":
    main()
