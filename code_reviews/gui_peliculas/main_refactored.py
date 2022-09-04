"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Button, Label, Frame

titulo = "Streaming Movie"
generos = "Accion", "Drama", "Comedia"
peliculas = (
    "La Máscara", "El Señor de los Cielos", "Jumanji",
    "Juegos de la Muerte", "La Momia ", "Terminator", 
)


def setup_ui(root, w=25, h=12):
    genre = Frame(root)
    movies = Frame(root)
    Label(root, text=titulo).grid(row=0, column=0)
    for i, genero in enumerate(generos):
        Button(
            genre, text=genero, width=9, height=2
        ).grid(row=1, column=i)
    for i, pelicula in enumerate(peliculas):
        Button(
            movies, text=pelicula, width=w, height=h,
        ).grid(row=2 + i // 2, column=i % 2, padx=15, pady=10)
    genre.grid(row=1, column=0)
    movies.grid(row=2, column=1)


if __name__ == """__main__""":
    root = Tk()
    root.geometry("1000x700")
    setup_ui(root)
    root.mainloop()
