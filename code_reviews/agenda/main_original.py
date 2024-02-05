"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Agenda:
    def __init__(self):
        self.__contactos = []

    def __add(self):
        nombre = input("Ingrese nombre: ")
        telefono = input("Ingrese # telefonico: ")
        email = input("Ingrese Email: ")
        self.__contactos.append({"nombre":nombre, "telefono":telefono, "email":email}) 

    def __list(self):
        if len(self.__contactos) == 0:
            print("No hay contactos.")
        else:
            print("Contactos: ")
            print("____________________________")
            for i in range(len(self.__contactos)):
                print(f"{i}-\tNombre: {self.__contactos[i]['nombre']}")
                print(f"\tTelefono: {self.__contactos[i]['telefono']}")
                print(f"\tEmail: {self.__contactos[i]['email']}")
                print("---------------------------------------")

    def __print_helper_menu(self, leyenda):
        print(f"*** {leyenda}:")
        print("1. Nombre")
        print("2. N° de telefono")
        print("3. Email")
        print("---------------------")
        print()

    def __print_helper_data(self, contacto):    
        print(f"Nombre: {contacto['nombre']}")
        print(f"Telefono: {contacto['telefono']}")
        print(f"Email: {contacto['email']}")

    def __search_by_name(self):
        print("Busqueda por nombre")
        nombre = input("Ingrese nombre: ")
        existe_data = False
        for i in range(len(self.__contactos)):
            if nombre == self.__contactos[i]['nombre']:
                self.__print_helper_data(self.__contactos[i])
                existe_data = True 
                break
        if not existe_data:
            print("El nombre no se encuentra registrado")        

    def __search_by_phone(self):
        print("Busqueda por N° de telefono")
        telefono = input("Ingrese N° de telefono: ")
        existe_data = False
        for i in range(len(self.__contactos)):
            if telefono == self.__contactos[i]['telefono']:
                self.__print_helper_data(self.__contactos[i])
                existe_data = True 
                break
        if not existe_data:
            print("El número no se encuentra registrado")        

    def __search_by_email(self):
        print("Busqueda por Email")
        email = input("Ingrese Email: ")
        existe_data = False
        for i in range(len(self.__contactos)):
            if email == self.__contactos[i]['email']:
                self.__print_helper_data(self.__contactos[i])
                existe_data = True 
                break
        if not existe_data:
            print("El Email no se encuentra registrado")      

    def __search(self):
        if len(self.__contactos) == 0:
            print("No hay contactos")
        else:
            self.__print_helper_menu("Buscar por")
            while True:
                opc = int(input("Tipo de busqueda: "))
                print()
                if opc == 1:
                    self.__search_by_name()
                    break
                elif opc == 2:
                    self.__search_by_phone()
                    break
                elif opc == 3:
                    self.__search_by_email()
                    break
                else:
                    self.__print_helper_menu("Buscar por")

    def __print_edit_items(self, index):
        print("- Seleccione un item")
        for i, contacto in enumerate(self.__contactos):
            if index == "nombre":
                print(f"{i}. {contacto['nombre']}")
            elif index == "telefono":
                print(f"{i}. {contacto['telefono']}")
            else:
                print(f"{i}. {contacto['email']}")
        print("----------------------------------------------------")

    def __edit_by_name(self):
        item = int(input("Ingrese item a modificar: "))
        if item < 0 > len(self.__contactos):
            print("Item no existe")
        else:
            print(f"Nombre actual: {self.__contactos[item]['nombre']}")
            nombre = input("Nombre nuevo: ")
            self.__contactos[item]['nombre'] = nombre
    
    def __edit_by_phone(self):
        item = int(input("Ingrese item a modificar: "))
        if item < 0 > len(self.__contactos):
            print("Item no existe")
        else:
            print(f"Telefono actual: {self.__contactos[item]['telefono']}")
            telefono = input("Telefono nuevo: ")
            self.__contactos[item]['telefono'] = telefono
    
    def __edit_by_email(self):
        item = int(input("Ingrese item a modificar: "))
        if item < 0 > len(self.__contactos):
            print("Item no existe")
        else:
            print(f"Email actual: {self.__contactos[item]['email']}")
            email = input("Email nuevo: ")
            self.__contactos[item]['email'] = email

    def __edit(self):
        if len(self.__contactos) == 0:
            print("No hay contactos")
        else:
            self.__print_helper_menu("Editar")
            while True:
                opc = int(input("Editar: "))
                print()
                if opc == 1:
                    self.__print_edit_items('nombre')
                    self.__edit_by_name()
                    break
                elif opc == 2:
                    self.__print_edit_items('telefono')
                    self.__edit_by_phone()
                    break
                elif opc == 3:
                    self.__print_edit_items('email')
                    self.__edit_by_email()
                    break
                else:
                    self.__print_edit_items()
                    self.__print_helper_menu("Editar")

                    
    def __menu(self):
        print()
        print("*** Agenda ***")
        print("------------------")
        print('1. Añadir')
        print('2. Listar')
        print('3. Buscar')
        print('4. Editar')
        print('5. Cerrar')
        print("------------------")
        print()

    def __get_opcion(self):
        while True:
            self.__menu()
            opc = int(input("## Ingrese opción: "))
            print()
            if opc == 1:
                print("- Agregar Contacto ...")
                self.__add()
            elif opc == 2:
                print("- Listar Contactos ...")
                self.__list()
            elif opc == 3:
                print("- Buscar Conctacto ...")
                self.__search()
            elif opc == 4:
                print("- Editar Conctactos ...")
                self.__edit()
            elif opc == 5:
                print("##########################")
                print("    PROGRAMA TERMINAD0")
                print("##########################")
                break    
            else:
                self.__menu()                

    def run(self):
        self.__get_opcion()

if __name__ == "__main__":
    Agenda().run()