"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
opcion_invalida = "Opcíon inválida. ¡Intente de nuevo!"
msg_despedida = "¡Muchas gracias! ¡Que tenga un buen día!"
porc_comunes = ["1.1", "2.2", "3.3", "4.4", "5.5"]

while True:
    dar_propina = input("¿Desea dejar propina? ").lower()
    if dar_propina not in ["si", "no"]:
        print(opcion_invalida)
        continue
    elif dar_propina in ["no"]:
        print(msg_despedida)
        break
    else:
        print("¿Cuánto % desea dejar? Escriba el primer dígito del porcentaje abajo:")
        print("--" * 20)
        joined_string = "0% | ".join(porc_comunes)
        porcentaje_str = input(f"{joined_string}0% \n")
        if not porcentaje_str.isdigit() or int(porcentaje_str) not in range(6):
            print(opcion_invalida)
            continue
        porcentaje = int(porcentaje_str) * 10
        print("--" * 20)
        print(f"¡Agradecemos su propina del {porcentaje}%!")
        print(msg_despedida)
        print("--" * 20)
        break