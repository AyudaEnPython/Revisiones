"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import str_input, int_input


def obtener_datos():
    return "".join(map(lambda s: s.capitalize(), [
        str_input("Nombre: ", lang="es")[0],
        str_input("Apellido paterno: ", lang="es"),
        str_input("Apellido materno: ", lang="es")[0],
    ]))


def main():
    usuarios = []
    duplicados = {}
    cantidad = int_input("Ingresar cantidad de usuarios a registrar: ")
    for i in range(cantidad):
        print(f"Usuario {i+1}")
        usuario = obtener_datos()
        if usuario in duplicados:
            duplicados[usuario] += 1
            usuario_generado = f"{usuario}{duplicados[usuario]}"
        else:
            duplicados[usuario] = 0
            usuario_generado = usuario
        usuarios.append(usuario_generado)
        print(f"Usuario generado: {usuario_generado}")
    print("Lista de usuarios generados")
    for usuario in usuarios:
        print(usuario)
    input("\nPresionar Enter para salir...")


if __name__ == "__main__":
    main()
