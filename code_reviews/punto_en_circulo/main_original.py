"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import sqrt

def main():

    print("Ingrese las coordenadas de centro de la circunferencia")
    h = float(input("ingrese la absisa del centro: "))
    k = float(input("ingrese la ordenada del centro: "))
    print("ingrese las coordenadas del punto P: ")
    x1 = float(input("ingrese la absisa del punto P: "))
    y1 = float(input("ingrese la ordenada del punto P: "))
    r = sqrt((x1-h)**2 + (y1-k)**2)	
    if (x1-h)**2 + (y1-k)**2 < r**2:
        print(f"el punto P({x1},{y1}) esta en el interior de la circunferencia y del cuadrado")
    if x1 > r or y1 > r:
        print(f"El punto P({x1},{y1}) esta en el exterior de la circunferencia y el cuadrado")
    if h < x1 < r and k < y1 < r and ((x1-h)**2 + (y1-k)**2 > r**2):
        print(f"El punto P({x1},{y1}) se encuentra en la zona 1")	
    if r < x1 < h and k < y1 < r and (x1-h)**2 + (y1-k)**2 > r**2:
        print (f"El punto P({x1},{y1}) esta en la zona 2")
    if r < x1 < h and r < y1 < k and (x1-h)**2 + (y1-k)**2 > r**2:
        print (f"El punto P({x1},{y1}) esta en la zona 3")
    if h < x1 < r and r < y1 < k and (x1-h)**2 + (y1-k)**2 > r**2:
        print (f"El punto P({x1},{y1}) esta en la zona 4")

if __name__ == '__main__':
	main()