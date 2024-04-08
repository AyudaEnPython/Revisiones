"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import*
from voltaje2 import*

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

def ventana_electricidad():
    electricidad = Toplevel(ventana)
    electricidad.title("electricidad")
    electricidad.geometry("300x400")
    boton_voltaje = Button(electricidad, text="Voltaje", command=llamar_voltaje, padx=50, pady=5)
    boton_voltaje.pack(pady=5)


boton_electricidad = Button(ventana, text="Electricidad", command=ventana_electricidad, padx=50, pady=4)
boton_electricidad.pack(pady=30)

ventana.mainloop()