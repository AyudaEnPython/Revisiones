"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from matplotlib import image

# librerias de pandas
from openpyxl import Workbook
import pandas as pd
from numpy import sqrt
from numpy.ma.core import sqrt
import numpy as np
import math

# librerias de la interfas grafica
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
#from click import command
import sqlite3

from tkinter import *
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import pandas as pd
from numpy.ma.core import sqrt
import numpy as np
import math
global mins1, mins2, index, index2, index_3, index4
global df, df2, df3, df4
global  dif, diferencia, diferencia2,Fr,Fr2 


ventana = Tk()
ventana.title('Tree headed Nano Monster VNA')
ventana.geometry("1100x800")

# HACEMOS EL LLAMADO A LOS ARCHIVOS
Label(ventana, text = "CREDES VNA" ).grid(row = 0, column=0)

Label(ventana, text = "Agrega el archivo 1 y 2  " ).grid(row = 1, column=0)


#--------------------------------------------

frame2 = Frame(ventana, bg='gray26')
frame2.grid(column=0,row=3,sticky='nsew')

frame2.columnconfigure(0, weight = 1)
frame2.rowconfigure(3, weight= 1)

frame2.columnconfigure(1, weight = 1)
frame2.rowconfigure(3, weight= 1)

frame2.columnconfigure(2, weight = 1)
frame2.rowconfigure(3, weight= 1)

frame2.columnconfigure(3, weight = 2)
frame2.rowconfigure(3, weight= 1)
#=================

frame3 = Frame(ventana, bg='gray26')
frame3.grid(column=0,row=4,sticky='nsew')

frame3.columnconfigure(0, weight = 1)
frame2.rowconfigure(4, weight= 1)

frame3.columnconfigure(1, weight = 1)
frame3.rowconfigure(4, weight= 1)

def abrir_archivo1():
    filename1 = filedialog.askopenfilename(initialdir ='/', 
											title='Selecione archivo', 
											filetype=(('xlsx files', '.xlsx'),('All files', '.'))) 
    

    global mins1,index,index2,df,df3  
    print(filename1)
    datos_obtenidos =  filename1
        
    archivoexcel =r'{}'.format(datos_obtenidos)

    df = pd.read_excel( archivoexcel )
    
    #-------------------------------------------------------------------------------
    datos = df["# HZ S RI R 50"].str.split(expand=True)
    datos.columns = ["F1","Parte Real","Parte imaginaria"]
    df = pd.concat([datos], axis=1)
    #---------------------------------------------------------------------------------
    valor = np.array(df)
    y=1
    columna =valor[:,y]
    i=0
    x=2
    columna_2=valor[:,x]

    d=[]
    for i in range(101):
        d.append(sqrt((float(columna[i])*2)+(float(columna_2[i])*2)))

    df["Magnitud"]=d
    #--------------------------------------------------------------------------


    df['S11(dB)_1']=(np.log10(df["Magnitud"]))*(20)

    #--------------------------------------------------------------------------
    mins1 = df["S11(dB)_1"].min()
    index = df["S11(dB)_1"].idxmin()
    index2 = df["S11(dB)_1"].idxmax()
    df3 = df.iloc[[index],[0,4]]
    print("-------------------------------------------------")
    print("Ubicacion del minimo de S11(dB)_1 : ")
    print(df3)

    


#==============================================================

def abrir_archivo2():
    filename2 = filedialog.askopenfilename(initialdir ='/', 
											title='Selecione archivo', 
											filetype=(('xlsx files', '.xlsx'),('All files', '.'))) 
    

    global mins2,index_3,index_4, df2,df4
    datos_obtenidos_2 =  filename2
        
    archivoexcel_2 =r'{}'.format(datos_obtenidos_2)

    df2 = pd.read_excel( archivoexcel_2 )
    
    datos2 = df2["# HZ S RI R 50"].str.split(expand=True)
    datos2.columns = ["F2","Parte Real","Parte Imaginaria"]
    df2 = pd.concat([datos2], axis=1)
    #---------------------------------------------------------------------------------

    valor_2 = np.array(df2)
    y_2=1
    columna_1 =valor_2[:,y_2]
    i_2=0
    x_2=2
    columna_2_2=valor_2[:,x_2]

    d_2=[]
    for i_2 in range(101):
        d_2.append(sqrt((float(columna_1[i_2])*2)+(float(columna_2_2[i_2])*2)))

    df2["Magnitud_2"]=d_2
    #--------------------------------------------------------------------------
    df2['S11(dB)_2']=(np.log10(df2["Magnitud_2"]))*(20)
    mins2 = df2["S11(dB)_2"].min()
    index_3 = df2["S11(dB)_2"].idxmin()
    index_4 = df2["S11(dB)_2"].idxmax()
    df4 = df2.iloc[[index_3],[0,4]]
    print("-------------------------------------------------")
    print("Ubicacion del minimo de S11(dB)_2 : ")
    print(df4)
    print("-------------------------------------------------")
#===============================================================
def operaciones():
    
    global diferencia,diferencia2
    diferencia = abs(mins2-mins1)
    dif = (mins2-mins1)
    print("La diferencia entre S11(dB)_1 y S11(dB)_2 es igual a: ", diferencia)
    #----------------------------------------------------------------------------------------------
    Fr = int(df.at[index, "F1"])
    Fr2 = int(df2.at[index_3, "F2"])
    diferencia2 = Fr2 - Fr
    print("La diferencia entre F1 y F2 es igual a: ", diferencia2)
    #print("\n")
    print("-------------------------------------------------")
    
    Resultados.insert(0,"----------------------------------------------------------------")
    Resultados.insert(1)
    Resultados.insert(2,df3)
    Resultados.insert(3,"----------------------------------------------------------------")
    Resultados.insert(4,"Ubicacion del minimo de S11(dB)_2 :")
    Resultados.insert(5,df4)
    Resultados.insert(6,"----------------------------------------------------------------")
    Resultados.insert(7,"La diferencia entre S11(dB)_1 y S11(dB)_2 es igual a:")
    Resultados.insert(8,diferencia)
    Resultados.insert(9,"----------------------------------------------------------------")
    Resultados.insert(10,"La diferencia entre F1 y F2 es igual a: ")
    Resultados.insert(11,diferencia2)
    Resultados.insert(12,"---------------------------------------------------------------")
    


#====================================================================

def grafica ():    
    import matplotlib.pyplot as plt
    
    x_1= df["F1"]
    y_1= df["S11(dB)_1"]

    x_2= df2["F2"]
    y_2= df2["S11(dB)_2"]


    plt.plot(x_1,y_1,x_2,y_2)
    
    
    # LEYENDA 
    plt.legend(["S11(dB)_1","S11(dB)_2"],loc=4)

    #TEXTO PARA EL S11(dB)_11

    dif = (mins2-mins1)

    if dif > 0:
        plt.text(0,2,("La grafica del S11 subio",diferencia,"dB"))

    if dif < 0:
        plt.text(0,2,("La grafica del S11 bajo",diferencia,"dB"))

    if dif == 0:
        plt.text(0,2,("La grafica del S11 permanecio en el mismo lugar",diferencia,"dB"))

    #TEXTO PARA EL Fr

    if diferencia2 > 0:
        plt.text(0,1,("La grafica se movio a la derecha",diferencia2,"Hz"))

    if diferencia2 < 0:
        plt.text(0,1,("La grafica se movio a la izquierda",diferencia2,"Hz"))

    if diferencia2 == 0:
        plt.text(0,1,("La grafica permanecio en la misma poscion",diferencia2,"Hz"))

    
    plt.show()

    

    
boton1 = Button(frame2, text= 'Abrir Archivo 1', bg='green2',command= abrir_archivo1)
boton1.grid(column = 0, row = 3, sticky='nsew', padx=10, pady=10)

boton2 = Button(frame2, text= 'Abrir Archivo 2', bg='green2',command = abrir_archivo2)
boton2.grid(column = 1, row = 3, sticky='nsew', padx=10, pady=10,)



#===================================================================
boton3 = Button(frame3, text= 'Operaciones', bg='magenta',command=operaciones)
boton3.grid(column = 0, row = 4, sticky='nsew', padx=10, pady=10)

boton4 = Button(frame3, text= 'Grafica', bg='magenta',command=grafica)
boton4.grid(column = 1, row = 4, sticky='nsew', padx=10, pady=10)
#===================================================================
    
Resultados = Listbox(ventana,bg = "white")
Resultados.place(x=0, y=250, width=400, height=300)

Grafica =Entry(ventana,bg = "white")
Grafica.place(x=400, y=70, width=700, height=550)

#====================================================================
ventana.mainloop()