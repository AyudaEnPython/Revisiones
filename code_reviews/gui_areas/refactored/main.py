"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Tk

from widgets import CustomMenu, CustomFrame
from figuras import FIGURAS, MEDIDAS, figuras_entries


class App(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("270x215")
        self.frame = None
        self.setup_ui()

    def setup_ui(self):
        self.figuras = CustomMenu(
            "Seleccionar figura",
            FIGURAS.keys(),
            command=lambda _: self.manage_entries()
        )
        self.medidas = CustomMenu(
            "Seleccionar medida",
            MEDIDAS,
        )
        self.calcular = Button(text="Calcular", command=self.calculate)
        self.figuras.pack()
        self.medidas.pack()
        self.calcular.pack(pady=5)

    def manage_entries(self):
        try:
            self.frame.destroy()
        except AttributeError:
            pass
        self.frame = CustomFrame(figuras_entries(self.figuras.get()))
        self.frame.pack()

    def calculate(self):
        figura = FIGURAS[self.figuras.get()](*self.frame.get_entries())
        result = {
            "Área": figura.area(),
            "Perímetro": figura.perimetro(),
        }
        medida = self.medidas.get(default="Área")
        self.frame.set_result(
            f"{medida}: {result[medida]}"
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()
