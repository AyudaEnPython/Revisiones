"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import mysql.connector
# pip install prototools
from prototools.protomysql import ProtoMySQL, execute, get_q

TABLE = "automovil"
ejecutar = execute


class Database:

    def __init__(self) -> None:
        self.db = ProtoMySQL(
            host="localhost",
            database="automotoradb",
            user="root",
            password="",
        )
        self._table = TABLE
    
    def insertar(self, obj):
        self.db.add(self._table, obj.__dict__)

    def eliminar(self, pk):
        self.db.delete(self._table, f"patente='{pk}'")

    def actualizar(self, obj):
        self.db.update_(self._table, get_q(obj), f"patente='{obj.patente}'")

    def seleccionar(self, pk):
        return self.db.select(self._table, f"patente='{pk}'")

    def seleccionar_todos(self):
        return self.db.get_all(self._table)
