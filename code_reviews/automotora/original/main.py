"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from Automotora import Vehículos
from Consultas import *

def leerOpcion():
    continuar=True
    num=0
    while continuar:
        try:
            num=int(input("Ingrese una opción: "))
            continuar=False
        except:
            print("Debe ingresar un número")
    return num

def menu():
    op=-1
    while op<0 or op>1:
        print("Automotora")
        print("1.- Vehículos")
        print("0.- Salir")
        op=leerOpcion()
        if op<0 or op>1:
            print("Debe ingresar una opción válida.")
    return op



def subMenu(menu):
    op=-1
    while op<0 or op>5:
        print(f"SubMenú {menu}")
        print(f"1.- Agregar {menu}")
        print(f"2.- Editar {menu}")
        print(f"3.- Eliminar {menu}")
        print(f"4.- Imprimir {menu} (Uno)")
        print(f"5.- Imprimir {menu} (Todos)")
        print(f"0.- Salir")
        op=leerOpcion()
        if op<0 or op>5:
            print("Debe ingresar una opción válida.")
    return op

def existe(patente):
    vehículo=get_vehículo_detalle(patente)
    print("-----------")
    print(vehículo)
    if vehículo.getPatente()=="":
        return False
    else:
        return True

def agregarVehículo():
    patente=input("Ingrese Patente")
    if existe(patente):
        print("La patente ingresada ya se encuentra en la BD")
    else:
        modelo=input("Modelo del vehículo: ")
        año=input("Año de fabricación: ")
        estado=input("Estado del carro: ")
        kilometraje=input("Kilometraje: ")
        combustión=input("Tipo de combustión: ")
        vehículo=Vehículos(patente, modelo, año, estado, kilometraje, combustión)
        resultado=insert_vehículo(vehículo)
        print(resultado)

def editarVehículo():
    patente=input("Ingrese patente del auto a editar: ")
    vehículo=get_vehículo_detalle(patente)
    if vehículo!="":
        print(vehículo.imprimir())
        print("Menú edición")
        print("1.- Modelo")
        print("2.- Año")
        print("3.- Estado")
        print("4.- Kilometraje")
        print("5.- Combustión")
        print("6.- Salir")
        opcion=leerOpcion()
        if opcion==1:
            modelo=input("Ingrese modelo del auto: ")
            vehículo.setModelo(modelo)
        elif opcion==2:
            año=input("Ingrese año de fabricación: ")
            vehículo.setAño(año)
        elif opcion==3:
            estado=input("Estado del auto: ")
            vehículo.setEstado(estado)
        elif opcion==4:
            kilometraje=input("Ingrese kilometraje: ")
            vehículo.setKilometraje(kilometraje)
        elif opcion==5:
            combustión=input("Tipo de combustión: ")
            vehículo.setCombustión(combustión)
        else:
            print("No se realizaron cambios.")
        if opcion>0 and opcion<=4:
            print(update_vehículo(vehículo))

def eliminarVehículo():
    patente=input("Ingrese la patente del vehículo a eliminar: ")
    print(delete_vehículo(patente))

def imprimirVehículo():
    patente=input("Ingrese patente del auto a imprimir: ")
    vehículo=get_vehículo_detalle(patente)
    if patente!="":
        print(patente.imprimir())
    else: 
        print("Este auto no existe")

def imprimirVehículos():
    vehículos=get_vehículos_detalles()
    for vehículo in vehículos:
        print(vehículo.imprimir())

op=-1
while op!=0:
    op=menu()
    if op==1:#menu autos
        op2=-1
        while op2!=0:
            op2=subMenu("Vehículo")
            if op2==1:#Agregar auto
                print("Agregando el vehículo...")
                agregarVehículo()
            elif op2==2:#Editar auto
                print("Editando el vehículo...")
                editarVehículo()
            elif op2==3:#Eliminando el auto
                print("Eliminando el vehículo...")
                eliminarVehículo()
            elif op2==4:#Imprimir un auto
                print("Imprimiendo un vehículo...")
                imprimirVehículo()
            elif op2==5:#imprimir todos los autos
                print("Imprimiendo todos los vehículos...")
                imprimirVehículos()
            elif op2==0:
                print("Volviendo al menú principal")
    elif op==0:#salir
        print("Gracias por preferirnos")
