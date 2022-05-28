"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: there's still a lot to refactor.
"""
from tkinter import Entry, Tk, Label, Button, Frame

from constants import CFG
from system import App


class Login(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        #self.config(width=600, height=400)
        self.master["bg"] = "#314252"
        self.setup_ui()

    def setup_ui(self) -> None:
        Label(self.master, text="Usuario", **CFG["lbl"]).place(x=60, y=110)
        Label(self.master, text="Contreseña", **CFG["lbl"]).place(x=60, y=160)
        self.user = Entry(self.master, font=("Arial", 12), relief="flat")
        self.password = Entry(self.master, font=("Arial", 12), relief="flat")
        self.confirm = Button(self.master, text="Entrar", **CFG["btn"])
        self.cancel = Button(self.master, text="Salir", **CFG["btn"])
        self.user.place(x=180, y=110, height=25, width=150)
        self.password.place(x=180, y=160, height=25, width=150)
        self.confirm.place(x=60, y=250, width=90)
        self.cancel.place(x=180, y=250, width=90)


class MainWindow(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("600x400")
        self.login = Login(self)
        self.login.pack()
        self.login.confirm.config(command=self.autorizado)

    def autorizado(self):
        if (
            self.login.user.get() == "admin" and
            self.login.password.get() == "123"
        ):
            self.geometry("1200x400")
            for w in self.winfo_children():
                w.destroy()
            self.show_system()
        else:
            pass
    
    def show_system(self):
        system = App(self)
        system.pack()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
