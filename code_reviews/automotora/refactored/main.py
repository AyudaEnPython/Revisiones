"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu
from prototools.colorize import magenta

from database import Database, ejecutar
from models import Vehiculo


class App(Menu):

    def __init__(self, database):
        super().__init__()
        self.title = "Automotora"
        self.add_options(
            ("Agregar", self.agregar),
            ("Editar", self.editar),
            ("Eliminar", self.eliminar),
            ("Imprimir por patente", self.imprimir_uno),
            ("Imprimir todos", self.imprimir_todos),
        )
        self.db = database()

    def _vehiculo(self):
        patente = input("Ingresar patente: ")
        return self.db.seleccionar(patente), patente

    def _insertar(self, patente):
        self.db.insertar(Vehiculo.get_cli(patente))

    def agregar(self):
        ejecutar(
            self._vehiculo,
            self._insertar,
            "La patente {} ya ha sido registrada",
            expression=lambda x: x,
            alt_message="Acción realizada con éxito!",
        )

    def editar(self):
        ejecutar(
            self._vehiculo,
            lambda x: self.db.actualizar(Vehiculo.get_cli(x)),
            "No se encuentra la patente {}",
            alt_message="Acción realizada con éxito!",
        )

    def eliminar(self):
        ejecutar(
            self._vehiculo,
            self.db.eliminar,
            "No se encuentra la patente {}",
            alt_message="Acción realizada con éxito!",
        )

    def imprimir_uno(self):
        ejecutar(
            self._vehiculo,
            lambda: None,
            "No se encuentra la patente {}",
            condition=True,
            alt_function=Vehiculo,
        )

    def imprimir_todos(self):
        for data in self.db.seleccionar_todos():
            print(Vehiculo(*data))


if __name__ == "__main__":
    app = App(Database)
    app.settings(
        style="double",
        separators=True,
        color=magenta,
    )
    app.run()
