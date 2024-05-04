"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *

root = Tk()
root.geometry("400x300")

Frame =Frame(root)

Frame.pack()


foto1 = PhotoImage(file="images/pizza.gif")
foto2 = PhotoImage(file="images/tomahawk.gif")
foto3 = PhotoImage(file="images/jamon.gif")


Label(root, image=foto1).pack()
Label(root, image=foto2).pack()
Label(root, image=foto3).pack()


Checkbutton(root, text="Pizza").pack(side="right")
Checkbutton(root, text="Tomahaw").pack(side="right")
Checkbutton(root, text="Jamon").pack(side="right")





root.mainloop()