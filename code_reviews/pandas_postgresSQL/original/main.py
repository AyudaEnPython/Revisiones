"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#-*- coding: utf-8 -*-
import os
import locale
from datetime import datetime
from enum import Enum

import pandas as pd
import requests
import psycopg2

from sqlalchemy import create_engine

import sqlalchemy as db
from decouple import config


locale.setlocale(locale.LC_TIME, "es")

fuentes = {
    'museos': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv',
    'cine': 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv',
    'biblioteca_popular' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv'
}
mes = datetime.now().strftime("%B")
anio = datetime.now().year
nombre_subcarpeta = f'{anio}-{mes}'


def generar_nombre_archivo(categoria):
    fecha_actual = datetime.now().strftime('%d-%m-%Y')
    return f'{categoria}-{fecha_actual}.csv'


def crear_carpetas(categoria):
    assert isinstance(categoria, str), 'Parámetro debe ser string'
    if not os.path.exists(os.path.join(os.getcwd(), categoria)):
        os.mkdir(categoria)
    if not os.path.exists(os.path.join(os.getcwd(), categoria, nombre_subcarpeta)):
        os.mkdir(os.path.join(categoria, nombre_subcarpeta))


def descargar_fuentes (categoria, url):
    nombre_archivo = generar_nombre_archivo(categoria)
    path_archivo = os.path.join(os.getcwd(), categoria, nombre_subcarpeta, nombre_archivo)
    req = requests.get(url)
    req.encoding = 'utf-8'
    with open(path_archivo, 'w+', encoding='utf-8') as f:
        f.write(req.text)

columnas = {
    'Cod_Localidad' : "cod_localidad",
    'ID_Provincia': "id_provincia",
    'ID_Departamento' : "id_departamento",
    'Categoria' : "categoria",
    'Provincia' : "provincia",
    'Localidad' : "localidad",
    'Nombre' : "nombre",
    'Domicilio' : "domicilio",
    'Codigo_Postal' : "codigo_postal",
    'Numero_Tel' : "numero_de_telefono",
    'Mail' : "mail",
    "Web" : "web" 
}

def main():

    for categoria, url in fuentes.items():
        crear_carpetas(categoria)
        descargar_fuentes(categoria, url)

    categorias = list(fuentes.keys())
    def fname (categoria):
        return os.path.join(os.getcwd(), categoria, nombre_subcarpeta, generar_nombre_archivo(categoria))

    df_museos = pd.read_csv(fname(categorias[0]), encoding="utf-8")
    df_cines = pd.read_csv(fname(categorias[1]), encoding="utf-8")
    df_bibliotecas = pd.read_csv(fname(categorias[2]), encoding="utf-8")
    
    columnas_a_filtrar = [a for a in columnas.values()]    
    columnas_a_filtrar = list(columnas.values())  

    df_bibliotecas = df_bibliotecas.rename(columns={
        "Cod_Loc": columnas['Cod_Localidad'],
        "IdProvincia": columnas['ID_Provincia'],
        "IdDepartamento": columnas['ID_Departamento'],
        "Categoría": columnas['Categoria'],
        "Provincia": columnas['Provincia'],
        "Localidad": columnas['Localidad'],
        "Nombre": columnas['Nombre'],
        "Domicilio": columnas['Domicilio'],
        "CP": columnas['Codigo_Postal'],
        "Teléfono": columnas['Numero_Tel'],
        "Mail": columnas['Mail'],
        "Web": columnas['Web']
    })
    df_bibliotecas = df_bibliotecas[columnas_a_filtrar].copy()
    
    
    df_cines = df_cines.rename(columns={
        "Cod_Loc": columnas['Cod_Localidad'],
        "IdProvincia": columnas['ID_Provincia'],
        "IdDepartamento": columnas['ID_Departamento'],
        "Categoría": columnas['Categoria'],
        "Provincia": columnas['Provincia'],
        "Localidad": columnas['Localidad'],
        "Nombre": columnas['Nombre'],
        "Dirección": columnas['Domicilio'],
        "CP": columnas['Codigo_Postal'],
        "Teléfono": columnas['Numero_Tel'],
        "Mail": columnas['Mail'],
        "Web": columnas['Web']
    })
    df_cines = df_cines[columnas_a_filtrar].copy()
    
    df_museos = df_museos.rename(columns={
        "Cod_Loc": columnas['Cod_Localidad'],
        "IdProvincia": columnas['ID_Provincia'],
        "IdDepartamento": columnas['ID_Departamento'],
        "categoria": columnas['Categoria'],
        "provincia": columnas['Provincia'],
        "localidad": columnas['Localidad'],
        "nombre": columnas['Nombre'],
        "direccion": columnas['Domicilio'],
        "CP": columnas['Codigo_Postal'],
        "telefono": columnas['Numero_Tel'],
        "Mail": columnas['Mail'],
        "Web": columnas['Web']
    })
    df_museos = df_museos[columnas_a_filtrar].copy()
    
    df_conjunto = pd.concat([
        df_bibliotecas,
        df_cines,
        df_museos
    ])

    pd.DataFrame.to_csv(df_conjunto, "conjunto.csv", sep=",")
    
    engine = db.create_engine(config("DATABASE_URL"))
    conexion_db = engine.connect()
    df = pd.DataFrame(df_conjunto)
    df.to_sql('registros', con=conexion_db, index=False, if_exists="replace")

if __name__ == "__main__":
    main()