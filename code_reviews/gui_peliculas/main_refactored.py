"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Button, Label

generos = "Accion", "Drama", "Comedia"
peliculas = (
    ("La mascara", "El señor de los cielos", "Jumanji"),
    ("juegos de la muerte", "la momia ", "terminator"),
)


def setup_buttons(root):
    for i, genero in enumerate(generos):
        Button(root, text=genero, width=9, height=2).grid(row=1, column=i)
    for i, pelicula in enumerate(peliculas):
        for j, pelicula in enumerate(peliculas[i]):
            Button(
                root, text=pelicula, width=25, height=15
            ).grid(row=i + 3, column=j)


if __name__ == """__main__""":
    root = Tk()
    root.geometry("1000x700")
    setup_buttons(root)
    root.mainloop()
