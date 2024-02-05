"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Agenda:
    def __init__(self):
        self.contactos = []

    def add_contacto(self):
        contacto = {
            "nombre": input("Ingrese nombre: "),
            "telefono": input("Ingrese # telefonico: "),
            "email": input("Ingrese Email: ")
        }
        self.contactos.append(contacto)

    def list_contactos(self):
        if not self.contactos:
            print("No hay contactos.")
            return

        print("Contactos: ")
        print("____________________________")
        for i, contacto in enumerate(self.contactos):
            print(f"{i}-\tNombre: {contacto['nombre']}")
            print(f"\tTelefono: {contacto['telefono']}")
            print(f"\tEmail: {contacto['email']}")
            print("---------------------------------------")

    def search_contacto(self, field, value):
        for contacto in self.contactos:
            if contacto[field] == value:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Telefono: {contacto['telefono']}")
                print(f"Email: {contacto['email']}")
                return True
        return False

    def edit_contacto(self, field, item_index, new_value):
        self.contactos[item_index][field] = new_value

    def menu(self):
        print("*** Agenda ***")
        print("------------------")
        print('1. Añadir')
        print('2. Listar')
        print('3. Buscar')
        print('4. Editar')
        print('5. Cerrar')
        print("------------------")

    def run(self):
        while True:
            self.menu()
            opc = int(input("## Ingrese opción: "))
            print()

            if opc == 1:
                print("- Agregar Contacto ...")
                self.add_contacto()
            elif opc == 2:
                print("- Listar Contactos ...")
                self.list_contactos()
            elif opc == 3:
                print("- Buscar Conctacto ...")
                field = input("Buscar por (nombre, telefono, email): ")
                value = input(f"Ingrese {field}: ")
                found = self.search_contacto(field, value)
                if not found:
                    print(f"El {field} no se encuentra registrado")
            elif opc == 4:
                print("- Editar Conctactos ...")
                # Implement edit functionality here, using self.edit_contacto()
            elif opc == 5:
                print("##########################")
                print("  PROGRAMA TERMINAD0")
                print("##########################")
                break
            else:
                print("Opción inválida")

if __name__ == "__main__":
    Agenda().run()
