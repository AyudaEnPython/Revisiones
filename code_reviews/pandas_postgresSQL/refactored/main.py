"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# -*- coding: utf-8 -*-
from datetime import datetime
import locale
import os
import pandas as pd
import requests
from typing import Dict

from base import engine

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
SUBCARPETA = f"{datetime.now().year}-{datetime.now().strftime('%B')}"
FUENTES = {
    "museos":
        "https://datos.cultura.gob.ar/dataset/"
        "37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/"
        "4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museo.csv",
    "cine":
        "https://datos.cultura.gob.ar/dataset/"
        "37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/"
        "392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv",
    "biblioteca_popular":
        "https://datos.cultura.gob.ar/dataset/"
        "37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/"
        "01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
}
COLUMNAS = {
    "cod_loc": "cod_localidad",
    "idprovincia": "id_provincia",
    "iddepartamento": "id_departamento",
    "categoria": "categoria",
    "provincia": "provincia",
    "localidad": "localidad",
    "nombre": "nombre",
    "direccion": "domicilio",
    "domicilio": "domicilio",
    "cp": "codigo_postal",
    "telefono": "numero_de_telefono",
    "mail": "mail",
    "web": "web",
}


def fname(categoria: str) -> str:
    return os.path.join(
        os.getcwd(), categoria, SUBCARPETA,
        f"{categoria}-{datetime.now().strftime('%d-%m-%Y')}.csv",
    )


def crear_carpetas(categoria: str) -> None:
    if not os.path.exists(os.path.join(os.getcwd(), categoria)):
        os.mkdir(categoria)
    if not os.path.exists(
        os.path.join(os.getcwd(), categoria, SUBCARPETA)
    ):
        os.mkdir(os.path.join(categoria, SUBCARPETA))


def _descargar(categoria: str, url: str) -> None:
    req = requests.get(url)
    req.encoding = "utf-8"
    with open(fname(categoria), "w+", encoding="utf-8") as f:
        f.write(req.text)


def descargar_fuentes(fuentes: Dict[str, str]) -> None:
    for categoria, url in fuentes.items():
        crear_carpetas(categoria)
        _descargar(categoria, url)


def _rename(df: pd.DataFrame) -> pd.DataFrame:
    for c, s in zip("áéíóú", "aeiou"):
        df = df.rename(columns=lambda x: x.replace(c, s))
    return df


def main():
    descargar_fuentes(FUENTES)
    conjunto = [
        _rename(pd.read_csv(fname(categoria), encoding="utf-8")
        .rename(columns=str.lower))
        .rename(columns=COLUMNAS)[list(COLUMNAS.values())]
        for categoria in list(FUENTES.keys())
    ]
    df_conjunto = pd.concat(conjunto)
    df_conjunto.to_csv("conjunto.csv")
    df_conjunto.to_sql(
        "registros", con=engine, index=False, if_exists="replace"
    )


if __name__ == "__main__":
    main()
