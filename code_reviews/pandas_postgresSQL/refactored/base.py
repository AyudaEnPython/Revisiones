"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from sqlalchemy import create_engine

from config import DATABASE_URI
from base import Base

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
