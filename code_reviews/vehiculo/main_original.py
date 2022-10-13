"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Vehiculo:
    #atributos
    marca = ""
    ruedas = 0
    color = ""
    enMarcha = False
    #constructor
    def __init__(self, marca, ruedas, color ):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color


    #metodos
    def arrancar(self):
        self.enMarcha = True


    def tipoVehiculo(self):
        if self.ruedas == 4:
            print("Automovil")
        
        if self.ruedas == 2:
            print("Motocicleta")


    def mostrar(self):
        print("Marca: " + self.marca)
        print("Color: " + self.color)
        print("Numero de ruedas: ", self.ruedas)
        print("Encendido: ", self.enMarcha)


vehiculo1 = Vehiculo("VW", 4, "rojo")
vehiculo1.arrancar()
vehiculo1.tipoVehiculo()
vehiculo1.mostrar()


vehiculo2 = Vehiculo("Honda", 2, "negro")
vehiculo2.tipoVehiculo()
vehiculo2.mostrar()

Vehiculo.ruedas = 1
vehiculo2.mostrar()