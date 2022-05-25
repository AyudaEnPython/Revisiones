"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame, Label, Listbox, Button
from typing import List


class ButtonGroup(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self["bg"] = "gray26"
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.setup_ui()

    def setup_ui(self) -> None:
        self.open_1 = Button(self, text="Abrir archivo 1", bg="green2")
        self.open_2 = Button(self, text="Abrir archivo 2", bg="green2")
        self.process = Button(self, text="Operar", bg="magenta")
        self.plot = Button(self, text="Graficar", bg="magenta")
        self.open_1.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        self.open_2.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.process.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        self.plot.grid(row=1, column=1, padx=5, pady=5, sticky="we")


class SideWindow(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.setup_ui()

    def setup_ui(self) -> None:
        Label(self, text="CREDES VNA").grid(column=0, row=0)
        Label(self, text="Agrega el archivo 1 y 2").grid(column=0, row=1)
        self.btn_group = ButtonGroup(self)
        self.display = Listbox(self, width=50, height=11)
        self.txt_1 = Label(self, text="")
        self.txt_2 = Label(self, text="")
        self.btn_group.grid(column=0, row=2, padx=5, pady=5, sticky="we")
        self.display.grid(column=0, row=3, padx=5, pady=5, sticky="we")
        self.txt_1.grid(column=0, row=4, padx=5, pady=5, sticky="we")
        self.txt_2.grid(column=0, row=5, padx=5, pady=5, sticky="we")


class PlotWindow(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.custom_legend = ["S11(dB)_1", "S11(dB)_2"]
        self.setup_ui()

    def set_legend(self, legend: List[str]) -> None:
        self.custom_legend = legend

    def setup_ui(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(column=0, row=0, sticky="we")

    def plot(self, x_1, y_1, x_2, y_2) -> None:
        self.ax.clear()
        self.ax.plot(x_1, y_1, x_2, y_2)
        self.ax.legend(self.custom_legend)
        self.canvas.draw()
