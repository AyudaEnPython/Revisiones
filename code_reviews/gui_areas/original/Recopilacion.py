"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import tkinter as tk

"""
Funciones para eventos
"""

def ElemenetoSeleccionado(seleccion):
    if seleccion == 'Circulo':
        figura = Circulo(0)
        figura.Radio()
        figura.ValorRadio()
        
    elif seleccion == 'Triangulo equilatero':
        figura = TrianguloEquilatero(0,0)
        figura.Base()
        figura.ValorBase()
        figura.Altura()
        figura.ValorAltura()
        
ventana =tk.Tk()
ventana.title("Programa en fase beta")
ventana.resizable(False,True)
ventana.geometry("720x1280")

# fondo = tk.PhotoImage(file="fondo.gif")
# fondo = fondo.subsample(1,1)
# fondo1 = tk.Label(image=fondo)
# fondo1.place(x=0,y=0,relwidth=1.0,relheight=1.0)

bienvenida = tk.Label(ventana,text='Bienvenido Kevin')
bienvenida.place(x=280,width=190,height=20)
bienvenida.pack

solicitud = tk.Label(ventana,text='Ingresa los valores conocidos',bg='grey')
solicitud.place(x=530,y=30,width=160,height=20)
solicitud.pack

lista_seleccion_figura = tk.StringVar(ventana)
lista_seleccion_figura.set('Figura')

lista_seleccion_metodo = tk.StringVar(ventana)
lista_seleccion_metodo.set('Metodo')

lista_figuras = ['Circulo','Triangulo equilatero','Triangulo rectangulo','Rectangulo']
lista_metodos = ['trigonométrico','teorema de pitagoras']

seleccion_figura =tk.OptionMenu(ventana,lista_seleccion_figura,*lista_figuras)
seleccion_figura.config(width=20)
seleccion_figura.pack(side='left',padx=30,pady=30)

seleccion_metodo =tk.OptionMenu(ventana,lista_seleccion_metodo,*lista_metodos)
seleccion_metodo.config(width=20)
seleccion_metodo.pack(side='left',padx=30,pady=30)

class Figura:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def Base(self):
        base = tk.Label(ventana,text='valor de la base')
        base.place(x=400,y=60,width=100,height=20)
        base.pack
    def ValorBase(self):
        valor_base = tk.Entry(ventana)
        valor_base.place(x=500,y=60,width=210,height=20)
        valor_base.pack
    def Altura(self):
        altura = tk.Label(ventana,text='valor de la altura')
        altura.place(x=400,y=90,width=100,height=20)
        altura.pack
    def ValorAltura(self):
        valor_altura = tk.Entry(ventana)
        valor_altura.place(x=500,y=90,width=210,height=20)
        valor_altura.pack

#figuras geometricas
class TrianguloEquilatero(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)


class TrianguloRectangulo(TrianguloEquilatero):
    def __init__(self, base, altura, angulo,hipotenusa):
        super().__init__(base, altura, )
        self.angulo = angulo
        self.hipotenusa = hipotenusa
    def Angulo(self):
        ""
        
    def ValorAngulo(self):
        ""
class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        
class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def Radio(self):
        radio = tk.Label(ventana,text='Valor del radio')
        radio.place(x=400,y=60,width=100,height=20)
        radio.pack
    def ValorRadio(self):    
        valor_radio = tk.Entry(ventana)
        valor_radio.place(x=500,y=60,width=210,height=20)
        valor_radio.pack
        
#metodos
class Metodo:
    def __init__(self,trigonometrico,teorema):
        self.trigonometrico = trigonometrico
        self.teorema = teorema
   
class Operaciones():
    ""        
#los resultados de las operaciones con los datos ingresados
class Resultados():
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro
    def Area(self):    
        area = tk.Label(ventana,text='valor del área')
        area.place(x=400,y=120,width=100,height=20)
        area.pack
    def ValorArea(self):
        valor_area = tk.Label(ventana,text="aqui se muestra el resultado")
        valor_area.place(x=500,y=120,width=210,height=20)
        valor_area.pack
    def Perimetro(self):
        perimetro = tk.Label(ventana,text='valor del perimetro')
        perimetro.place(x=400,y=150,width=100,height=20)
        perimetro.pack
    def ValorPerimetro(self):
        valor_perimetro = tk.Label(ventana,text="aqui se muestra el resultado")
        valor_perimetro.place(x=500,y=150,width=210,height=20)
        valor_perimetro.pack
class ResultadosCirculo(Resultados):
    def __init__(self, area, circunferencia):
        super().__init__(area)
        self.circunferencia = circunferencia
    def Circunferencia(self):
        circunferencia = tk.Label(ventana,text='valor de la circunferencia')
        circunferencia.place(x=400,y=90,width=100,height=20)
        circunferencia.pack
    def ValorCircunferencia(self):
        valor_circunferencia = tk.Label(ventana,text="aqui se muestra el resultado")
        valor_circunferencia.place(x=500,y=90,width=210,height=20)
        valor_circunferencia.pack













ventana.mainloop()