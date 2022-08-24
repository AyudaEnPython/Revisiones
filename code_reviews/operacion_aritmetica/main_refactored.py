"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Union
# pip install prototools
from prototools import Menu, float_input, textbox


class OpcionAritmetica:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def sumar(self) -> float:
        return self.x + self.y

    def restar(self) -> float:
        return self.x - self.y
    
    def multiplicar(self) -> float:
        return self.x * self.y

    def dividir(self) -> Union[float, str]:
        try:
            return self.x / self.y
        except ZeroDivisionError:
            return "No se puede dividir entre cero."


class App(Menu):

    def __init__(self) -> None:
        super().__init__()
        self.add_options(
            ("Sumar", lambda: self._g(self._f().sumar())),
            ("Restar", lambda: self._g(self._f().restar())),
            ("Multiplicar", lambda: self._g(self._f().multiplicar())),
            ("Division", lambda: self._g(self._f().dividir())),
        )

    def _f(self):
        return OpcionAritmetica(
            float_input("Primer valor: "), float_input("Segundo valor: ")
        )

    def _g(self, r):
        textbox(f"Resultado: {r}")


if __name__ == "__main__":
    app = App()
    app.run()
