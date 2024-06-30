"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
print()
print('Programa de inventario para Ultramarinos  🥝')
print('--' * 30)
print()
class Inventario:
    def __init__(self):
        self.productos = dict()
    def agregar_producto(self, nombre, precio, cantidad):
        self.productos[nombre] = {"precio": precio, "cantidad": cantidad}
    def mostrar_inventario(self):
        print("Inventario de productos:")
        print('--' * 20)
        print()
        for producto, info in self.productos.items():
            print(f"{producto}: Precio: ${info['precio']:.2f}, Cantidad: {info['cantidad']}")
    def calcular_precio_promedio(self):
        try:
            precio_promedio = sum(producto['precio'] for producto in self.productos.values()) / len(self.productos)
            print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}")
        except ZeroDivisionError:
            print("\nNo hay productos en el inventario.")
    def encontrar_producto_mas_caro(self):
        try:
            producto_mas_caro = max(self.productos, key=lambda x: self.productos[x]["precio"])
            print(f"\nEl producto más caro es: {producto_mas_caro} (${self.productos[producto_mas_caro]['precio']:.2f})")
        except ValueError:
            print("\nNo hay productos en el inventario.")
# Uso de la clase Inventario con entrada de datos por teclado
inventario = Inventario()
try:
    while True:
        nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        precio = float(input("Ingrese el precio del producto: $"))
        cantidad = float(input("Ingrese la cantidad del producto: "))
        inventario.agregar_producto(nombre, precio, cantidad)
except ValueError as s:
    print("Error: ¡El precio y la cantidad deben ser números!", s)
inventario.mostrar_inventario()
inventario.calcular_precio_promedio()
inventario.encontrar_producto_mas_caro()
print()
print('Fin del programa!!')
print()