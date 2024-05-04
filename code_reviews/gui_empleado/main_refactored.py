"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
from tkinter import Label, LabelFrame, Entry, Button, Tk, messagebox

LABELS = (
    "Nombre",
    "Apellido",
    "Sexo",
    "Fecha de nacimiento",
    "Fecha de ingreso",
    "Salario",
)


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("AyudaEnPython | Empleado")
        self.geometry("270x250")
        self.entries = {}
        self.setup_ui()

    def setup_ui(self):
        frame = LabelFrame(text="Registrar Empleado")
        frame.grid(column=0, row=0, columnspan=2, padx=10, pady=10)
        for i, label in enumerate(LABELS, 1):
            Label(frame, text=label).grid(column=0, row=i, sticky="e")
            entry = Entry(frame)
            entry.grid(column=1, row=i, padx=5, pady=5)
            self.entries[label.lower()] = entry
        registrar = Button(text="Registrar", command=self.registrar)
        calcular = Button(text="Prestaciones", command=self.prestaciones)
        registrar.grid(column=0, row=7)
        calcular.grid(column=1, row=7)

    def registrar(self):  # TODO
        data = ", ".join(v.get() for v in self.entries.values())
        messagebox.showinfo(title="Registro", message=data)

    def prestaciones(self):  # TODO
        messagebox.showinfo(title="Fecha Actual", message=datetime.now())


if __name__ == "__main__":
    app = App()
    app.mainloop()
