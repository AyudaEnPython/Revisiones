"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre= nombre
        self.edad= edad
        self.nacionalidad= nacionalidad
    def hablar(self):
        print("Hola, qlq")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return f'Mi habilidad es:{self.habilidad}'


class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(habilidad)  # missing 'self': Artista.__init__(self, habilidad)
        self.salario= salario
        self.empresa= empresa
    def presentarse(self):
        return f'Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}'

roberto = EmpleadoArtista("Roberto",25,"Peruano","cantar",1000,"Apple")
print(roberto.presentarse())


