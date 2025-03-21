"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
LENGTH = 8
password = "12345678"

print(f"Restablecimiento de contraseña\n{'='*30}\n")

while True:
    new_password = input("Ingresar nueva contraseña: ")
    if len(new_password) >= LENGTH:
        print("La contraseña es segura.")
        break
    print("La nueva contraseña debe tener 8 o más caracteres.")

response = input(
    f"¿Confirma que desea establecer '{new_password}' "
    f"como su nueva contraseña? (si/no)\n> "
).lower()
if response == "si":
    password = new_password
    print("Contraseña actualizada exitosamente")
else:
    print("No se restablecerá la contraseña.")
print(f"Contraseña: {password}")
