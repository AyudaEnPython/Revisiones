"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from ConexionBD import *
from Automotora import Vehículos

def get_vehículo_detalle(vehículo_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from vehículo where patente = %s"
        cursor.execute(select_query, (vehículo_id))
        records = cursor.fetchall()
        vehículo = Vehículos()
        for row in records:
            vehículo.setPatente(row[0])
            vehículo.setModelo(row[1])
            vehículo.setAño(row[2])
            vehículo.setEstado(row[3])
            vehículo.setKilometraje(row[4])
            vehículo.setCombustion(row[5])
        close_connection(connection)
        return vehículo
    except (Exception, mysql.connector.Error) as error:
        print("Error en la operación", error)
        return ""

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Estas conectado a: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error al ejecutar", error)

def insert_vehículo(vehículo):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """insert into vehículo (patente,modelo,
        año,estado,kilometraje,combustión) values(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql_select_query, (vehículo.getPatente(),
        vehículo.getModelo(),vehículo.getAño(),
        vehículo.getEstado(),vehículo.getKilometraje(),vehículo.getCombustión()))
        connection.commit()
        close_connection(connection)
        return "Vehículo Patente:", vehículo.getPatente(), "insertado correctamente"
    except (Exception, mysql.connector.Error) as error:
        return "Error en la consulta", error

def get_vehículos_detalles(vehículo_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = "select * from vehículo"
        cursor.execute(select_query)
        records = cursor.fetchall()
        vehículo=[]
        for row in records:
            vehículo=Vehículos()
            vehículo.setPatente(row[0])
            vehículo.setModelo(row[1])
            vehículo.setAño(row[2])
            vehículo.setEstado(row[3])
            vehículo.setKilometraje(row[4])
            vehículo.setcombustión(row[5])
        close_connection(connection)
        return vehículo
    except (Exception, mysql.connector.Error) as error:
        print("Error en la operación", error)
        return ""

def get_vehículos_modelo_año(modelo,año):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """select * from vehículo where modelo=%s and año >=%s"""
        cursor.execute(sql, (modelo, año))
        records = cursor.fetchall()
        print("Imprimiendo vehículos de", modelo,
        "y años superior o iguales a ", año, "\n")
        for row in records:
            print("Vehículo Patente: ",row[0])
            print("Vehículo Modelo: ",row[1])
            print("Vehículo Año: ",row[2])
            print("Vehículo Estado: ",row[3])
            print("Vehículo Kilometraje: ",row[4])
            print("Vehículo Tipo combustible: ",row[5])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error en la operación", error)
        return ""

def update_vehículo(vehículo):
    try:   
        # Actualizando Vehículo
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update vehículo set modelo=%s,
        año=%s, estado=%s, kilometraje=%s, combustión=%s where patente=%s"""
        cursor.execute(sql_select_query, (vehículo.getModelo(),
        vehículo.getAño(),vehículo.getEstado(),
        vehículo.getKilometraje(), vehículo.getCombustion(),
        vehículo.getPatente()))
        connection.commit()
        close_connection(connection)
        return f"Vehículo Patente: {vehículo.getPatente()} se actualizó"
    except (Exception, mysql.connector.Error) as error:
        return "Error en la consulta", error

def delete_vehículo(patente):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """delete from vehículo where patente = %s"""
        cursor.execute(sql_select_query, (patente,))
        connection.commit()
        close_connection(connection)
        return "Vehículo Patente:", patente, "fue eliminado"
    except (Exception, mysql.connector.Error) as error:
        return ("Error en la consulta delete", error)