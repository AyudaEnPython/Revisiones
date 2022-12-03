"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import mysql.connector
def get_connection():
    connection = mysql.connector.connect(host='localhost',
    database='automotoradb',user='root',password='')
    return connection
def close_connection(connection):
    if connection:
        connection.close()