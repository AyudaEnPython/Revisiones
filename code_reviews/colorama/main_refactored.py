from typing import List, Tuple

from prototools.colorize import red
from prototools import ScreenCanvas, FigureDataclass


class Caracter(FigureDataclass):

    def get_pos(self) -> List[Tuple[int, int]]:
        return [(self.x, self.y)]


class App(ScreenCanvas):

    def __init__(self) -> None:
        super().__init__()
        self.width = 20
        self.height = 10
        self.add_figures([Caracter(0, 0, lambda x: red(":)") if x else ' ')])

    def run(self):
        self.move(self.figures[0])


if __name__ == "__main__":
    app = App()
    app.run()
