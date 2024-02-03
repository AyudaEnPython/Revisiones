from dataclasses import dataclass
from typing import Union
# pip install prototools
from prototools import float_input, int_input, Menu


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def __str__(self) -> str:
        return (
            f"Producto: {self.nombre:<12} | "
            f"Precio: {self.precio:<8} | "
            f"Cantidad: {self.cantidad:.2f}"
        )


class Inventario:

    def __init__(self) -> None:
        self.productos = []

    def agregar(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_productos(self) -> None:
        print("Lista de productos disponibles:")
        for producto in self.productos:
            print(producto)

    def _hay_productos(self) -> bool:
        return len(self.productos) != 0

    def promedio(self) -> Union[float, str]:
        if not self._hay_productos():
            return "No hay productos en el inventario"
        return (
            sum(producto.precio for producto in self.productos) /
            len(self.productos)
        )

    def mas_caro(self) -> Union[Producto, str]:
        if not self._hay_productos():
            return "No hay productos en el inventario"
        return max(self.productos, key=lambda x: x.precio)


def ingresar_producto(inventario):
    nombre = input("Ingresar producto: ")
    precio = float_input("Ingresar precio: ")
    cantidad = int_input("Ingresar cantidad: ")
    inventario.agregar(Producto(nombre, precio, cantidad))


def main():
    inventario = Inventario()
    menu = Menu()
    menu.add_options(
        ("Ingresar", lambda: ingresar_producto(inventario)),
        ("Mostrar", inventario.mostrar_productos),
        ("Precio promedio", lambda: print(inventario.promedio())),
        ("Más caro", lambda: print(inventario.mas_caro())),
    )
    menu.run()


if __name__ == "__main__":
    main()
