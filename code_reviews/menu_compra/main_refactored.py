"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

stock = {
    "product A": 100,
    "product B": 200,
    "product C": 300,
    "product D": 400,
}


def _validar(n):
    try:
        n = int(n)
    except ValueError:
        return
    return n


def _check(x):
    if x is None:
        raise Exception("Error")
    return x


def _producto(d, n):
    n = _validar(n)
    if n is None or n > len(d):
        return
    return d.get(list(d.keys())[n-1])


def mostrar_menu(stock):
    print("Productos:")
    for i, item in enumerate(stock, 1):
        print(f"{i}. {item}: {stock[item]}")


def comprar():
    mostrar_menu(stock)
    opcion = input("Ingresar número del producto: ")
    producto = _check(_producto(stock, opcion))
    cantidad = _check(_validar(input("Ingresar cantidad: ")))
    return producto * cantidad


def main():
    total = 0
    while True:
        try:
            total += comprar()
        except Exception as e:
            print(e)
        else:
            if input("Desea continuar? (s/n): ").lower() in "no":
                return total


if __name__ == "__main__":
    if input("Desea realizar una compra? (s/n): ").lower() in "si":
        total = main()
        print(f"Total: {total}")
