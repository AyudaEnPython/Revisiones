"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Registro(Base):
    __tablename__ = 'registros'

    id_registro = Column(Integer, primary_key=True)
    fecha_carga = Column(Date)
    cod_localidad = Column(String)
    id_provincia = Column(String)
    id_departamento = Column(String)
    id_categoria = Column(String)
    provincia = Column(String)
    localidad = Column(String)
    nombre = Column(String)
    domicilio = Column(String)
    codigo_postal = Column(String)
    numero_tel = Column(String)
    mail = Column(String)
    web = Column(String)
