from cocos.director import director 
from cocos.scene import Scene
from cocos.menu import*
 
class MiMenu(Menu): 
    def __init__ (self,item1,item2,item3,item4,item5,item6):
        self.item1=('item1')
        self.item2=('item2')
        self.item3=('item3')
        self.item4=('item4')
        self.item5=('item5')
        self.item6=('item6')
        self.MiMenu=('MiMenu')
        super().__init__("Menu Principal")
        item1= ToggleMenuItem('sonido:',self.eleccion_sonido,True)
        resoluciones = ['640*480','800*600','1024*480','1270*720','1600*900']
        item2= MultipleMenuItem ('Resolucion:',self.eleccion_resolucion, 
                                resoluciones)
        colores = [(255,0,0),(0,255,0),(0,0,255),(0,200,200)]
        item3 = ColorMenuItem('Color:',self.eleccion_color,colores)
        item4 = EntryMenuItem('Dificultad (1-10):',self.eleccion_dificultad,
                            '', max_length=2)
        item5 =ImageMenuItem('mi_helicoptero_2.png',self.on_image_call_back)
        item6 =MenuItem('Salir',self.salir)
        self.create_menu([item1,item2,item3,item4,item5,item6])
    def eleccion_sonido(self, b):
        if b:
            sel ='activado'
        else:
            sel ='desactivado'    
        print('Tu eleccion de audio:', sel)
    def eleccion_resolucion(self,valor):    
        print('Has elegido la resolucion numero {}'.format(valor+1))
    def eleccion_color(self,valor):
        print('Has elegido el color numero {}'.format(valor+1))
    def eleccion_dificultad (self,valor):    
        print('Has elegido el nivel de dificultad',valor)
    def on_image_call_back(self):
        print('Has elegido comenzar el juego')
    def salir(self):
        director.windwos.close()
        print('Has elegido salir')
def main():
    ventana=director.init( width=800,height=600, caption='')
    ventana.set_location(500,200)
    director.run(Scene(MiMenu('item1','item2','item3','item4','item5','item6')))
if __name__ == '__main__':
    main()