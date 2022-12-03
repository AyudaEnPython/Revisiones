"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Vehículos:
    def __init__(self,patente="",modelo="",año="",
    estado="",kilometraje="",combustión=""):
        self.__patente=patente
        self.__modelo=modelo
        self.__año=año
        self.__estado=estado
        self.__kilometraje=kilometraje
        self.__combustión=combustión

    def getPatente(self):
        return self.__patente

    def setPatente(self,patente):
        self.__patente=patente

    def getModelo(self):
        return self.__modelo

    def setModelo(self,modelo):
        self.__modelo=modelo

    def getAño(self):
        return self.__año

    def setAño(self,año):
        self.__año=año

    def getEstado(self):
        return self.__estado
    
    def setEstado(self,estado):
        self.__estado=estado

    def getKilometraje(self):
        return self.__kilometraje
    
    def setKilometraje(self,kilometraje):
        self.__kilometraje=kilometraje

    def getCombustión(self):
        return self.__combustión
    
    def setCombustión(self,combustión):
        self.__combustión=combustión

    def imprimir(self):
        return f"""Patente:  {self.__patente}\nModelo: {self.__modelo}
        \nAño: {self.__año}\nEstado: {self.__estado}\nKilometraje: {self.__kilometraje}
        \nTipo Combustión: {self.__combustión}\n"""