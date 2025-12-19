"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
a = float(input("Ingresar venta 1: "))
b = float(input("Ingresar venta 2: "))
c = float(input("Ingresar venta 3: "))
sueldo = float(input("Ingresar sueldo de trabajador: "))
print("La venta total es: ", a+b+c)
pago_extra = 0
if a+b+c > 100:
    pago_extra = sueldo * 0.25
if a+b+c >= 10 and a+b+c <= 99:
    pago_extra = sueldo * 0.15

print("El sueldo total del trabajador es: ", sueldo+pago_extra)