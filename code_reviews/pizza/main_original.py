"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
def main():
    
    ingredientes = {1:["Pimiento", "Tofu"],
                    2:["Peperoni", "Jamón", "Salmón"],
                    0:["Mozzarella", "Tomate"]}

    pizza = int(input("Seleccioné 1 Pizza Vegetariana o 2 Pizza Normal: "))

    print("Seleccione su ingrediente")
    for n, i in enumerate(ingredientes[pizza]):
        print(n, i)
    
    ingrediente = int(input("ingrediente: "))

    tipo = "Vegetariana" if pizza == 1 else "No Vegetariana"

    todos = ""
    for i in ingredientes[0]:
        todos += f"{i}, "

    todos += ingredientes[pizza][ingrediente]

    print(f"Pizza {tipo}:\n\tingredientes: {todos}.")

if __name__ == "__main__":
    main()

