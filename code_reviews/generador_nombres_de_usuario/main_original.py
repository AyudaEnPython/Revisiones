"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
print("Generador de Nombres de usuario")
while True:
    cant_usuarios=int(input("Ingresar la cantidad de usuarios a registrar: "))
    if cant_usuarios > 0:
        break
    else:
        print("Debe ser mayor a cero, ingrese de nuevo!\n")

usuarios_g=[]
token_number = [0]
for x in range(0, cant_usuarios):
    print(f"Trabajador {x+1}:")
    nombre= input("Nombre: ")
    ap_paterno= input("Apellido Paterno:")
    ap_materno= input("Apellido Materno:")
    name_generate=nombre[0].capitalize()+ap_paterno.capitalize() #
    for y in range(0,len(usuarios_g)):
        if name_generate == usuarios_g[y]:
            token_number.append(token_number[len(token_number)-1]+1)
            name_generate += str(token_number[len(token_number)-1])
            break
    usuarios_g.append(name_generate)
    print("\nUsuario generado:",name_generate)
    print()

print(usuarios_g)
print(token_number)
input()