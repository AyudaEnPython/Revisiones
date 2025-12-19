"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
a = float(input("Ingresar venta 1: "))
b = float(input("Ingresar venta 2: "))
c = float(input("Ingresar venta 3: "))
sueldo = float(input("Ingresar sueldo: "))

venta_total = a + b + c 

if venta_total > 100:
    bonificacion =  0.25
elif 10 <= venta_total <= 99:
    bonificacion =  0.15
else:
    bonificacion = 0.0

total = sueldo * (1 + bonificacion)

print(f"La venta total del trabajador es: {venta_total:.2f}")
print(f"El sueldo total del trabajador es: {total:.2f}")