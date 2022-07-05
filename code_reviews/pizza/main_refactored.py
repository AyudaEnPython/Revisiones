"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
ingredientes = {
    "0": ["Mozzarella", "Tomate"],
    "1": ["Pimiento", "Tofu"],
    "2": ["Peperoni", "Jamón", "Salmón"],
}
print("Tipo de Pizza:\n1.- Vegetariana\n2.- No Vegetariana")

tipo = input("Seleccionar tipo > ")
print("\n".join(f"{i}.- {s}" for i, s in enumerate(ingredientes[tipo], 1)))
opcion = int(input("Seleccionar ingrediente > "))

print(f'\nPizza { {"1": "vegetariana", "2": "no vegetariana"}[tipo] }')
print(
    f"Igredientes: {', '.join(ingredientes['0'])}, "
    f"{ingredientes[tipo][opcion-1]}"
)
