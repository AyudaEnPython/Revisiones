"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import requests
valor_dolar = 'https://www.freeforexapi.com/api/live?pairs=USDCOP'
r = requests.get(valor_dolar)
data = r.json()
print(data)