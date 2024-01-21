from tkinter import Checkbutton, Label, PhotoImage, Tk

root = Tk()

foto1 = PhotoImage(file="images/pizza.gif")
foto2 = PhotoImage(file="images/tomahawk.gif")
foto3 = PhotoImage(file="images/jamon.gif")

Label(root, image=foto1).pack()
Checkbutton(root, text="Pizza").pack()
Label(root, image=foto2).pack()
Checkbutton(root, text="Tomahawk").pack()
Label(root, image=foto3).pack()
Checkbutton(root, text="Jamon").pack()

root.mainloop()
