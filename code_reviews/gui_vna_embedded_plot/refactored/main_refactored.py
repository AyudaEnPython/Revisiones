"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import warnings
from tkinter import Frame, Tk, filedialog

from widgets import SideWindow, PlotWindow
from utils import CFG, Data, get_data, process_data


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("Ayuda en Python")
        self.geometry("935x485")
        self.setup_ui()
        self._set_commands()

    def setup_ui(self) -> None:
        self.left = Frame(self)
        self.right = Frame(self)
        self.side = SideWindow(self.left)
        self.plotter = PlotWindow(self.right)
        self.left.grid(column=0, row=0, sticky="nsew")
        self.right.grid(column=1, row=0, sticky="nsew")
        self.side.grid(column=0, row=0, sticky="nsew")
        self.plotter.grid(column=0, row=0, sticky="nsew")

    def _set_commands(self):
        self.side.btn_group.open_1.config(command=self.open_1)
        self.side.btn_group.open_2.config(command=self.open_2)
        self.side.btn_group.process.config(command=self.process)
        self.side.btn_group.plot.config(command=self.plot)

    def _open(self, f1: str, magnitud: str, db: str) -> Data:
        filetypes = (("Excel files", "*.xlsx"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(
            initialdir ="/",
            title="Selecione archivo",
            filetypes=filetypes,
        )
        return get_data(filename, f1, magnitud, db)

    def open_1(self) -> None:
        self.data_x = self._open("F1", "Magnitud", "S11(dB)_1")
        self.min_1, self.i_1, self.i_2, self.n_df, self.df_1 = self.data_x

    def open_2(self) -> None:
        self.data_y = self._open("F2", "Magnitud_2", "S11(dB)_2")
        self.min_2, self.j_1, self.j_2, self.m_df, self.df_2 = self.data_y

    def process(self) -> None:
        resultado, (self.diff, self.dif_1, self.dif_2) = process_data(
            self.data_x, self.data_y
        )
        for i, line in enumerate(resultado):
            self.side.display.insert(i, line)

    def _set_text(self):
        if self.diff > 0:
            self.side.txt_1.config(text=CFG["db"][1].format(self.dif_1))
        if self.diff < 0:
            self.side.txt_1.config(text=CFG["db"][-1].format(self.dif_1))
        if self.diff == 0:
            self.side.txt_1.config(text=CFG["db"][0].format(self.dif_1))
        if self.dif_2 > 0:
            self.side.txt_2.config(text=CFG["fr"][1].format(self.dif_2))
        if self.dif_2 < 0:
            self.side.txt_2.config(text=CFG["fr"][-1].format(self.dif_2))
        if self.dif_2 == 0:
            self.side.txt_2.config(text=CFG["fr"][0].format(self.dif_2))

    def plot(self) -> None:
        x_1 = self.df_1["F1"]
        y_1 = self.df_1["S11(dB)_1"]
        x_2 = self.df_2["F2"]
        y_2 = self.df_2["S11(dB)_2"]
        self.plotter.plot(x_1, y_1, x_2, y_2)
        self._set_text()


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    app = App()
    app.mainloop()
