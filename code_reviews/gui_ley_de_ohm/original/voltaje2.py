"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import*

def llamar_voltaje():
    voltaje = Tk()
    voltaje.title("Prueba")
    voltaje.geometry("300x400")
    resultado = StringVar()  # must be: resultado = StringVar(voltaje)

    def calcular_voltaje():
        operacion = float(entrada_resistencia.get()) * float(entrada_intensidad.get())
        return resultado.set(operacion)
    
    resistencia = Label(voltaje, text="Ingrese la resistencia: ", font=("Arial", 12))
    resistencia.pack(padx=20, pady=5, ipadx=5, ipady=5,)
    entrada_resistencia = Entry(voltaje, font=("Arial", 12))
    entrada_resistencia.pack(padx=5, pady=5, ipadx=5, ipady=5)

    intensidad= Label(voltaje, text="Ingrese la intensidad: ", font=("Arial", 12))
    intensidad.pack(padx=20, pady=5, ipadx=5, ipady=5,)
    entrada_intensidad = Entry(voltaje, font=("Arial", 12))
    entrada_intensidad.pack(padx=5, pady=5, ipadx=5, ipady=5)

    boton = Button(voltaje, text="calcular", command=calcular_voltaje)
    boton.pack(side=TOP)

    res = Label(voltaje, font=("Arial", 12), textvariable=resultado, padx=5, pady=5)
    res.pack()