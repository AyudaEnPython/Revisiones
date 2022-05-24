"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime, timedelta

tiempos=["01:30:50","04:20:30"]
def sumar_hora(tiempos):
    formato = "%H:%M:%S"
    for i in (range(len(tiempos))):
        lista = tiempos[0].split(":")
        hora=int(lista[0])
        minuto=int(lista[1])
        segundo=int(lista[2])
        h1 = datetime.strptime(tiempos[1], formato)
        dh = timedelta(hours=hora)
        dm = timedelta(minutes=minuto)
        ds = timedelta(seconds=segundo)
        resultado1 =h1 + ds
        resultado2 = resultado1 + dm
        resultado = resultado2 + dh
        print(type(resultado))
        resultado=resultado.strftime(formato)
        print(resultado)

print(sumar_hora(tiempos))