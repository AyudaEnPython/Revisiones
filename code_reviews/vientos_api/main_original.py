"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import requests
import pandas as pd
import os

def consultar_datos(fecha_inicial, fecha_final):
    try:
        # URL de datos abiertos parametrizada con las variables definidas en python para traer los datos de forma dinamica por dia.
        url = ("https://www.datos.gov.co/resource/sgfv-3yp8.json?$SELECT=FechaObservacion,CodigoEstacion,CodigoSensor,ValorObservado,NombreEstacion,Departamento,Municipio,ZonaHidrografica,Latitud,Longitud,DescripcionSensor,UnidadMedida,'NA' as control,'ok' as estado &$where=FechaObservacion BETWEEN +'{}'+ and +'{}'+ limit 1000000").format(fecha_inicial, fecha_final)

        # Realizar solicitud GET a la URL.
        # Perform GET request to the URL.
        response = requests.get(url)

        # Verificar el estado de la solicitud.
        response.raise_for_status()

        # Convertir la respuesta a formato JSON.
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None

# Ejemplo de uso:
fecha_inicial = '2015-07-01T00:00:00'
fecha_final = '2015-07-31T23:59:59'
datos = consultar_datos(fecha_inicial, fecha_final)
if datos:
    print("Datos obtenidos correctamente.")
    # Hacer algo con los datos, como imprimirlos.
    print(datos)
else:
    print("No se pudieron obtener los datos.")

df = pd.DataFrame(datos)

df = df.reindex(columns=['CodigoEstacion', 'CodigoSensor', 'FechaObservacion', 'ValorObservado', 'NombreEstacion',
'Departamento', 'Municipio', 'ZonaHidrografica', 'Latitud', 'Longitud',
'DescripcionSensor', 'UnidadMedida', 'control', 'estado'])

mapeo_columnas = {
'CodigoEstacion': "codigoestacion",
'CodigoSensor': "codigosensor",
'FechaObservacion': "fechaobservacion",
'ValorObservado': "valorobservado",
'NombreEstacion': "nombreestacion",
'Departamento': "departamento",
'Municipio': "municipio",
'ZonaHidrografica': "zonahidrografica",
'Latitud': "latitud",
'Longitud': "longitud",
'DescripcionSensor': "descripcionsensor",
'UnidadMedida': "unidadmedida",
'control': "control",
'estado': "estado"
}

df.to_excel("julio_2015.xlsx",sheet_name="julio", index=False)