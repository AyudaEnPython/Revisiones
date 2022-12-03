"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Vehiculo:
    patente: str
    modelo: str
    year: str
    estado: str
    kilometraje: str
    combustion: str

    @classmethod
    def get_cli(cls, patente):
        return cls(
            patente,
            input("Modelo: "),
            input("Año: "),
            input("Estado: "),
            input("Kilometraje: "),
            input("Tipo de combustión: "),
        )

    def __str__(self):
        return (
            f"Patente: {self.patente}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.year}\n"
            f"Estado: {self.estado}\n"
            f"Kilometraje: {self.kilometraje}\n"
            f"Tipo de combustión: {self.combustion}\n"
        )
