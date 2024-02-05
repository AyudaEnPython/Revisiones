"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from statistics import mean

registro =[
    ["José", [15, 18, 19]],
    ['María', [14, 17]],
    ["Victoria", [15, 13, 18, 12]],
    ["Kike", [6, 15, 12]],
]
print("\n".join(
    f"{nombre}: Promedio: {mean(xs):.1f} mayor: {max(xs)} menor:{min(xs)}"
    for (nombre, xs) in registro
))