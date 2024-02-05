"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import Union
# pip install prototools
from prototools import Menu, str_input, int_input, menu_input


@dataclass
class Contacto:
    nombre: str
    telefono: str
    correo: str

    def edit(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self) -> str:
        return (
            f"  Nombre: {self.nombre:}\n"
            f"Teléfono: {self.telefono}\n"
            f"  Correo: {self.correo}"
        )


class Agenda:

    def __init__(self) -> None:
        self.contactos = []
    
    def _is_empty(self) -> bool:
        return len(self.contactos) == 0
    
    def add(self, contacto: Contacto) -> None:
        self.contactos.append(contacto)

    def search(self, attr: str, text: str) -> Union[Contacto, str]:
        found = False
        for contacto in self.contactos:
            if getattr(contacto, attr) == text:
                found = True
                return contacto
        if not found:
            return f"El {attr} '{text}' no se encuentra registrado"

    def edit(self, index, nombre, telefono, correo):
        self.contactos[index].edit(nombre, telefono, correo)

    def show(self) -> None:
        if self._is_empty():
            print("No hay contactos.")
            return
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i:02d}:\n{contacto}")


class App(Menu):

    def __init__(self):
        super().__init__()
        self.agenda = Agenda()
        self.title = "Agenda"
        self.add_options(
            ("Añadir", self.add_contact),
            ("Buscar", self.buscar_contact),
            ("Editar", self.editar),
            ("Mostrar", self.agenda.show),
        )

    def _add_contact(self) -> tuple:
        nombre = str_input("Nombre: ", lang="es")
        telefono = str_input("Telefono: ", lang="es")
        correo = str_input("Correo: ", lang="es")
        return nombre, telefono, correo

    def add_contact(self) -> None:
        self.agenda.add(Contacto(*self._add_contact()))

    def buscar_contact(self) -> None:
        campo = menu_input(
            ("nombre", "telefono", "correo"), numbers=True, lang="es"
        )
        texto = str_input("> ")
        print(self.agenda.search(campo, texto))

    def editar(self) -> None:
        index = int_input("Ingresar índice: ", min=1, lang="es")
        if index > len(self.agenda.contactos):
            print("Índice incorrecto")
            return
        self.agenda.edit(index-1, *self._add_contact())


if __name__ == "__main__":
    app = App()
    app.run()
