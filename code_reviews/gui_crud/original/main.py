"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import *
import Principal as p



class App1:

		def __init__(self, master):

			self.frame = master
			self.DrawEntry1()
			self.DrawButtons1()
			self.DrawLabel1()
			self.login1()
			


		def DrawLabel1(self):
			self.lbl_usuario = Label(self.frame, foreground="white",font=(8), background="#314252",text="Usuario").place(x=60, y=110)
			self.lbl_contrsena = Label(self.frame, foreground="white",font=(8), background="#314252", text="Contreseña").place(x=60, y=160)


		def DrawEntry1(self):
			self.usuario = StringVar()
			self.contra = StringVar()

			self.txt_usuario = Entry(self.frame,font=('Arial', 12),relief="flat", background="#E7E7E7" ,textvariable=self.usuario).place(x=140, y=110, height=25, width=150)
			self.txt_contra = Entry(self.frame,font=('Arial', 12),relief="flat", background="#E7E7E7" ,textvariable=self.contra).place(x=180, y=160, height=25, width=150)

		
		def DrawButtons1(self):
			self.btn_confirm = Button(self.frame,foreground="white", text="entrar",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="#0051C8", command=lambda:self.login1()).place(x=60, y=250, width=90)
			self.btn_cancel = Button(self.frame, text="salir",foreground="white",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="#E81123", command="" )

		def login1(self):
			nom= self.usuario.get()
			nom1= self.contra.get()
			if nom == "admin" and nom1 =="123":
				print("hola")
				p.App
			else:
				pass
if __name__ == "__main__":
	root = Tk()
	root.title("Login")
	root.config(background="#314252")
	root.geometry("600x400")
	aplication = App1(root)
	root.mainloop()