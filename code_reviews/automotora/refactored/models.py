"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, asdict


@dataclass
class Vehiculo:
    patente: str
    marca: str
    año: str
    kilometraje: str
    tipo_combustible: str

    @classmethod
    def get_cli(cls, patente):
        return cls(
            patente,
            input("Marca: "),
            input("Año: "),
            input("Kilometraje: "),
            input("Tipo de combustible: "),
        )

    def to_dict(self):
        return asdict(self)

    def __str__(self):
        return "\n".join(
            f"{k}: {v}" for k, v in self.__dict__.items()
        )
