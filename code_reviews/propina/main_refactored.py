"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
pcs = 10, 15, 20, 25, 30

while True:
    print("¿Le gustaría dejar propina?\n1. Sí\n2. No")
    answer = input("> ")
    if answer == "2":
        break
    elif answer  == "1":
        while True:
            print("¿Qué porcentaje le gustaría dejar?")
            print("\n".join(f"{i}. {x}%" for i, x in enumerate(pcs, 1)))
            answer = input("> ")
            if answer.isdigit() and int(answer) in range(1, len(pcs) + 1):
                print(f"¡Gracias por la propina del {pcs[int(answer) - 1]}%!")
                break
            print(f"¡Opción inválida! Presionar del '1' al '{len(pcs)}'")
        break
    else:
        print("¡Opción inválida! Presionar '1' o '2'")
print("¡Que tenga un buen día!")
