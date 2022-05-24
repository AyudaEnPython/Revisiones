"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import timedelta
from typing import List
# pip install prototools
from prototools.validators import validate_time


def sumar_hora(tiempos: List[str]) -> str:
    return sum([
        timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        for t in tiempos
    ], timedelta())


if __name__ == "__main__":
    tiempos = ["01:30:50", "04:20:30", "02:10:10"]
    print(sumar_hora([validate_time(t) for t in tiempos])) # output: 8:01:30
