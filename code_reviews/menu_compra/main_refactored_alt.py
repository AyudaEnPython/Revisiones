"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import menu_input, int_input, main_loop, ask_to_finish

stock = {
    "product A": 100,
    "product B": 200,
    "product C": 300,
    "product D": 400,
}
total = []


def comprar():
    print("Productos:")
    item = menu_input(tuple(stock.keys()), numbers=True, lang="es")
    cantidad = int_input("Ingresar cantidad: ", min=0)
    total.append(stock[item] * cantidad)


if __name__ == "__main__":
    if ask_to_finish("Desea realizar una compra? (s/n): ", "s"):
        main_loop(comprar, lang="es")
        print(f"Total: {sum(total)}")
