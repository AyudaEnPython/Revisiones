"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Persona:
    nombre: str
    dob: str  # date of birth / fecha de nacimiento
    nacionalidad: str

    def calcular_edad(self) -> int:
        return int(datetime.today().strftime("%Y")) - int(self.dob[-4:])

    def presentarse(self) -> str:
        return f"Hola, soy {self.nombre} y tengo {self.calcular_edad()} años"


@dataclass
class Empleado(Persona):
    salario: float
    empresa: str

    def presentarse(self) -> str:
        return (
            f"{super().presentarse()}.\n"
            f"Trabajo para {self.empresa} y mi salario es de {self.salario}"
        )


@dataclass
class Artista(Persona):
    habilidad: str

    def mostrar_habilidad(self) -> str:
        return f"Mi habilidad es: {self.habilidad}"


@dataclass
class EmpleadoArtista(Empleado, Artista):

    def presentarse(self) -> str:
        return f"{super().presentarse()}.\n{self.mostrar_habilidad()}."


yngwie = EmpleadoArtista(
    nombre="Yngwie",
    dob="30/06/1963",
    nacionalidad="Sueco",
    habilidad="tocar la guitarra",
    salario=4000,
    empresa="Fender",
)
print(yngwie.presentarse())
