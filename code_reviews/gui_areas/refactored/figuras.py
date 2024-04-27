"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimetro(self):
        ...


class Cuadrilatero(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base * 2 + self.altura * 2


class Cuadrado(Cuadrilatero):

    def __init__(self, lado):
        super().__init__(lado, lado)


class Rectangulo(Cuadrilatero):

    def __init__(self, base, altura):
        super().__init__(base, altura)


class Triangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base * 3


class Circulo(Figura):

    def __init__(self, radio) -> None:
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2

    def perimetro(self):
        return 2 * pi * self.radio


FIGURAS = {
    "Círculo": Circulo,
    "Triángulo equilatero": Triangulo,
    "Cuadrado": Cuadrado,
    "Rectángulo": Rectangulo,
}
MEDIDAS = "Área", "Perímetro"


def figuras_entries(figura):
    return {
        "Círculo": ("radio", ),
        "Cuadrado": ("lado", ),
    }.get(figura, ("base", "altura") )
