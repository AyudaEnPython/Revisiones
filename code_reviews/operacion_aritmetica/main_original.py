"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class OpcionAritmetica:
    def __init__(self, ValorUno, ValorDos):
        self.ValorUno = ValorUno
        self.ValorDos = ValorDos
    
    def Suma(self):
        return self.ValorUno + self.ValorDos
    
    def Resta(self):
        return self.ValorUno - self.ValorDos
    
    def Multiplicacion(self):
        return self.ValorUno * self.ValorDos
    
    def Division(self):
        return self.ValorUno / self.ValorDos

print('\n*****  ELEGIR UNA OPCIÓN  *****\n')

print('1. Suma')
print('2. Resta')
print('3. Multiplicación')
print('4. División')
print('5. Salir\n')

opcion = int(input('-> '))

if opcion == 5:
    print('Adios! Vuelve Pronto')

else:
    valor1 = int(input('\nProporcionar 1er valor: '))
    valor2 = int(input('Proporcionar 2do valor: '))

    contador = 0

    while opcion != 5:
        if opcion == 1:
            resultado = OpcionAritmetica(valor1, valor2)
            print(f'\nPerfecto! La Suma es:     {resultado.Suma()}')
            break
        elif opcion == 2:
            resultado = OpcionAritmetica(valor1, valor2)
            print(f'\nPerfecto! La Resta es:    {resultado.Resta()}')
            break
        elif opcion == 3:
            resultado = OpcionAritmetica(valor1, valor2)
            print(f'\nPerfecto! La Multiplicación es:   {resultado.Multiplicacion()}')
            break
        elif opcion == 4:
            resultado = OpcionAritmetica(valor1, valor2)
            print(f'\nPerfecto! La División es:     {resultado.Division()}')
            break