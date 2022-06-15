"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import tkinter

ventana = tkinter.Tk()
ventana.geometry("1000x700")

etiqueta= tkinter.Label(ventana, text="Streaming Movie")
etiqueta.grid(row=0,column=0)

boton1 = tkinter.Button(ventana, text = "genero", width=9, height=2)
boton2 = tkinter.Button(ventana, text = "Accion", width=9, height=2)
boton3 = tkinter.Button(ventana, text = "Drama", width=9, height=2)
boton4 = tkinter.Button(ventana, text = "Comedia", width=9, height=2)
boton5 = tkinter.Button(ventana, text = "La mascara", width=25,height=15)
boton6 = tkinter.Button(ventana, text = "El señor de los cielos", width=25,height=15)
boton7 = tkinter.Button(ventana, text = "Jumanji", width=25,height=15)
boton8 = tkinter.Button(ventana, text = "juegos de la muerte", width=25,height=15)
boton9 = tkinter.Button(ventana, text = "la momia ", width=25,height=15)
boton10 = tkinter.Button(ventana, text = "terminator", width=25,height=15)

boton1.grid(row=1,column=0)
boton2.grid(row=1,column=2)
boton3.grid(row=1,column=3)
boton4.grid(row=1,column=4)
boton5.grid(row=3,column=1)
boton6.grid(row=3,column=2)
boton7.grid(row=3,column=3)
boton8.grid(row=4,column=1)
boton9.grid(row=4,column=2)
boton10.grid(row=4,column=3)


ventana.mainloop()