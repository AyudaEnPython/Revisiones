"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: Haven't refactored yet (just small changes to run the app)
"""
from tkinter import (
    Button,
    Canvas,
    Entry,
    Frame,
    Label,
    messagebox,
    Toplevel,
    ttk,
)

from constants import CFG


class App(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.frame = master
        self.setup_ui()
        self.draw_lists()

    def setup_ui(self):
        Label(self.frame, **CFG["lbl"],text="Nombre").place(x=60, y=110)
        Label(self.frame, **CFG["lbl"], text="Run").place(x=60, y=160)
        Label(self.frame, **CFG["lbl"], text="Fecha").place(x=60, y=210)
        Label(self.frame, **CFG["lbl"], text="Descripcion").place(x=60, y=260)
        self.txt_name = Entry(self.frame, font=('Arial', 12), **CFG["ent"])
        self.txt_rut = Entry(self.frame, font=('Arial', 12), **CFG["ent"])
        self.txt_date = Entry(self.frame, font=('Arial', 12), **CFG["ent"])
        self.txt_desc = Entry(self.frame, font=('Arial', 12), **CFG["ent"])
        self.txt_name.place(x=140, y=110, height=25, width=150)
        self.txt_rut.place(x=140, y=160, height=25, width=150)
        self.txt_date.place(x=140, y=210, height=25, width=150)
        self.txt_desc.place(x=150, y=260, height=25, width=150)
        self.btn_confirm = Button(
            self.frame, foreground="white", text="Guardar", borderwidth=2,
            relief="flat", cursor="hand1", overrelief="raise",
            background="#0051C8",
        )
        self.btn_cancel = Button(
            self.frame, text="Cancelar",foreground="white", borderwidth=2,
            relief="flat", cursor="hand1", overrelief="raise",
            background="#E81123",
        )
        self.btn_confirm.place(x=750, y=340, width=90)
        self.btn_cancel.place(x=850, y=340, width=90)

    def load_image(self):
        Label(
            self.frame, text="imagen",
            background="#314252", foreground="white",
        ).place(x=430, y=25)
        canvas = Canvas(self.frame)
        canvas.place(x=350, y=50, width=200, height=160)

    def draw_lists(self):
        self.list_elemts = ttk.Treeview(
            self.frame, columns=(1, 2, 3, 4), show="headings", height="8"
        )
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview.Heading", background="#0051C8",
            relief="flat", foreground="white",
        )
        style.map(
            "Treeview",
            background=[('selected', 'yellow')],
            foreground=[('selected', 'black')],
        )
        self.list_elemts.bind("<Double 1>", self.getRow)
        self.list_elemts.heading(1, text="Nombre")
        self.list_elemts.heading(2, text="Run")
        self.list_elemts.heading(3, text="Fecha")
        self.list_elemts.heading(4, text="Descripcion")
        self.list_elemts.column(1, anchor="center")
        self.list_elemts.column(2, anchor="center")
        self.list_elemts.column(3, anchor="center")
        self.list_elemts.column(4, anchor="center")
        self.list_elemts.place(x=340, y=90)


    def getRow(self, event):
        rowName = self.list_elemts.identify_row(event.y)
        item = self.list_elemts.item(self.list_elemts.focus())
        n = item['values'][0]
        e = item['values'][1]
        c = item['values'][2]
        i = item['values'][3]
        pop = Toplevel(self.frame)
        pop.geometry("400x200")
        lbl_n = Entry(pop).place(x=40, y = 40)
        lbl_e = Entry(pop).place(x=40, y = 80)
        lbl_c = Entry(pop).place(x=40, y = 120)
        btn_change = Button(
            pop, text="Actualizar", relief="flat",
            background="#00CE54", foreground="white",
        ).place(x=180, y=160, width=90)
        btn_delete = Button(
            pop, text="Eliminar", relief="flat",
            background="red", foreground="white",
        ).place(x=290, y=160, width=90)

    def eliminar(self, n):
        messagebox.showinfo(
            title="Actualizacion", message="Se han actualizado los datos",
        )
        self.ClearList()
        self.draw_lists()
        self._clear_entry()

    def editar(self, n, na, ed, ca, ic):
        messagebox.showinfo(
            title="Actualizacion", message="Se han actualizado los datos",
        )
        self.ClearList()
        self.draw_lists()
        self._clear_entry()

    def ClearList(self):
        self.list_elemts.delete(*self.list_elemts.get_children())

    def canceProcess(self):
        self._clear_entry()
    
    def _clear_entry(self):
        self.name.set("")
        self.rut.set("")
        self.date.set("")
        self.desc.set("")

    def confirmProcess(self):
        messagebox.showinfo(
            title="Alerta", message="Se inserto correctamente!",
        )
        self.ClearList()
        self.draw_lists()
        self._clear_entry()
