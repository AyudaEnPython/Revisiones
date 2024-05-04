"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import *
#from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox
from datetime import datetime
from datetime import timedelta
#Declaracion de la clase
class Empleado:
    def __init__(self, ventana):
        #ATRIBUTOS
        self.nombre=StringVar()
        self.apellido=StringVar()
        self.sexo=StringVar()
        self.fechaNac=StringVar()
        self.fechaIng=StringVar()
        self.salario=IntVar()
        #ATRIBUTO VENTANA
        self.ventana=ventana
        self.ventana.title('Programa Empleado')
        self.ventana.geometry('400x300')
        #FRAME O MARCO
        marco = LabelFrame(self.ventana, text='Registrar Empleado')
        marco.grid(column=0, row=0, columnspan=3, pady=20)
        #LABEL NOMBRE
        self.lblnombre=Label(marco, text='Nombre:').grid(column=0, row=1)
        self.entnombre=Entry(marco, textvariable=self.nombre)
        self.entnombre.grid(column= 1, row=1)
        #LABEL APELLIDO
        self.lblapellido=Label(marco, text='Apellido:').grid(column=0, row=2)
        self.entapellido=Entry(marco, textvariable=self.apellido)
        self.entapellido.grid(column= 1, row=2)
        #COMBOBOX
        self.lblSexo= Label(marco, text='Sexo:').grid(column=0,row=3)
        valores=('Masculino', 'Femenino')
        self.cmbSexo= Combobox(marco, width=10, textvariable=self.sexo, values=valores)
        self.cmbSexo.grid(column=1, row=3)
        #ENTRY FECHA DE NACIMIENTO
        self.lblfechaNac=Label(marco, text='Fecha de nacimiento:').grid(column=0, row=4)
        self.entfechaNac=Entry(marco, textvariable=self.fechaNac)
        self.entfechaNac.grid(column= 1, row=4)
        #ENTRY FECHA DE INGRESO
        self.lblfechaIng=Label(marco, text='Fecha de ingreso:').grid(column=0, row=5)
        self.entfechaIng=Entry(marco, textvariable=self.fechaIng)
        self.entfechaIng.grid(column= 1, row=5)
        #LABEL ENTRY SALARIO
        self.lblsalario=Label(marco, text='Salario:').grid(column=0, row=6)
        self.entsalario=Entry(marco, textvariable=self.salario)
        self.entsalario.grid(column= 1, row=6)
        #BUTTON REGISTRAR EMPLEADO
        self.btnRegistrarEmp=Button(ventana, text='Registrar empleado:', command=self.registrarEmpleado)
        self.btnRegistrarEmp.grid(column=0, row=7)
        #BUTTON CALCULAR PRESTACIONES
        self.btnCalcularPres=Button(ventana, text='Calcular Prestaciones', command=self.calcularPrestaciones)
        self.btnCalcularPres.grid(column=1, row=7)
    def registrarEmpleado(self):
        mensaje=self.nombre.get()+' '+self.apellido.get()+','+self.sexo.get()+','+self.fechaNac.get()+','+self.fechaIng.get()+','+str(self.salario.get())
        #print(mensaje)
        mb.showinfo(title='Registro Empleado', message=mensaje)
    def calcularPrestaciones(self):
        fechaActual=datetime.now()
        antiguedad=fechaActual-self.fechaIng
        prestaciones=(antiguedad*self.salario)/12
        mb.showinfo(title='Fecha Actual',message=fechaActual)
if __name__=='__main__':
    ventana=Tk()
    aplicacion=Empleado(ventana)
    ventana.mainloop()