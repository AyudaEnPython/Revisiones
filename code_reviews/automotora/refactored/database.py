"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools.protosql import ProtoSqlite, execute, get_q

DATABASE = "data.db"
TABLE = "automotora"
ejecutar = execute


class Database(ProtoSqlite):

    def __init__(self, db=DATABASE, table=TABLE):
        super().__init__(db, lang="es")
        self._db = db
        self._table = table

    def insertar(self, obj):
        self.add(self._table, obj.__dict__)

    def eliminar(self, pk):
        self._delete(self._table, f"patente='{pk}'")

    def actualizar(self, obj):
        self.update_(self._table, get_q(obj), f"patente='{obj.patente}'")

    def seleccionar(self, pk):
        return self.select(self._table, f"patente='{pk}'")

    def seleccionar_todos(self):
        return self.get_all(self._table)


if __name__ == "__main__":
    db = ProtoSqlite(DATABASE, lang="es")
    db.create_table(
        TABLE, 
        (
            "patente TEXT, modelo TEXT, year TEXT, "
            "estado TEXT, kilometraje TEXT, combustion TEXT"
        )
    )
