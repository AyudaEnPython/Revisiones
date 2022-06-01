"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sqlalchemy as db
from decouple import config


engine = db.create_engine(config("DATABASE_URL"))
# engine = db.create_engine("postgresql://postgres:root@localhost:5432/pruebasql")
connection = engine.connect()
metadata = db.MetaData()
tabla_registros = db.Table("registros", metadata,
                           db.Column("id_registro", db.Integer(), primary_key=True, autoincrement=True),
                           db.Column("fecha_carga", db.Date()),
                           db.Column('cod_localidad', db.String(255)),
                           db.Column('id_provincia', db.String(255)),
                           db.Column('id_departamento', db.String(255)),
                           db.Column('id_categoria', db.String(255)),
                           db.Column('provincia', db.String(255)),
                           db.Column('localidad', db.String(255)),
                           db.Column('nombre', db.String(255)),
                           db.Column('domicilio', db.String(255)),
                           db.Column('codigo_postal', db.String(255)),
                           db.Column('numero_tel', db.String(255)),
                           db.Column('mail', db.String(255)),
                           db.Column('web', db.String(255))
                           )

metadata.create_all(engine)
