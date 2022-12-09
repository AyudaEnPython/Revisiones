"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *

def main():
    root = Tk()
    root.title("Cursor change tkinter")
    root.configure(bd=20)
    etiqueta1 = Label(root, bg="#0095E5", width=15, height=8, cursor="arrow")
    etiqueta1.grid(column=0, row=0, padx=5)
    etiqueta2 = Label(root, bg="#F529A4", width=15, height=8, cursor="hand2")
    etiqueta2.grid(column=1, row=0, padx=5)
    etiqueta3 = Label(root, bg="#9532B2", width=15, height=8, cursor="heart")
    etiqueta3.grid(column=2, row=0, padx=5)
    etiqueta4 = Label(root, bg="#775AA1", width=15, height=8, cursor="fleur")
    etiqueta4.grid(column=0, row=1, pady=10)
    etiqueta5 = Label(root, bg="#F4CF00", width=15, height=8, cursor="watch")
    etiqueta5.grid(column=1, row=1, padx=5)
    etiqueta6 = Label(root, bg="#F5375C", width=15, height=8, cursor="pirate")
    etiqueta6.grid(column=2, row=1, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()