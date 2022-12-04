"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Vehiculo:
    patente: str
    marca: str
    año: str
    kilometraje: str
    tipo_combustion: str

    @classmethod
    def get_cli(cls, patente):
        return cls(
            patente,
            input("Modelo: "),
            input("Año: "),
            input("Kilometraje: "),
            input("Tipo de combustión: "),
        )

    def __str__(self):
        return (
            f"{k}: {v}" for k, v in self.__dict__.items()
        )
