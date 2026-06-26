"""AyudaEnPython: https://www.facebook.com/groups/ayudapython"""

print("Generador de Nombres de usuario")

while True:
    try:
        cantidad = int(input("Ingresar cantidad de usuarios a registrar: "))
        if cantidad > 0:
            break
        print("Debe ser mayor a cero, ingrese de nuevo!\n")
    except ValueError:
        print("Ingresar un número válido (entero positivo).")

usuarios, existentes = [], set()

for i in range(cantidad):
    print(f"Usuario {i + 1}")
    nombre = input("Nombre: ").strip()
    paterno = input("Apellido paterno: ").strip()
    materno = input("Apellido materno: ").strip()
    usuario = (
        nombre[0].capitalize()
        + paterno.capitalize()
        + (materno[0].capitalize() if materno else "")
    )
    usuario_generado = usuario
    n = 1
    while usuario_generado in existentes:
        usuario_generado = f"{usuario}{n}"
        n += 1
    existentes.add(usuario_generado)
    usuarios.append(usuario_generado)
    print(f"Usuario generado: {usuario_generado}")

print("Lista de usuarios generados:")
print("\n".join(f"- {usuario}" for usuario in usuarios))
input("\nPresionar Enter para salir...")
