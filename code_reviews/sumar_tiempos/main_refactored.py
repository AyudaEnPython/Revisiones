"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import timedelta
from typing import List
from prototools.validators import validate_time


def sumar_hora(tiempos: List[str]) -> str:
    t = timedelta()
    for tiempo in tiempos:
        h, m, s = [int(s) for s in tiempo.split(":")]
        t += timedelta(hours=h, minutes=m, seconds=s)
    return str(t)


if __name__ == "__main__":
    tiempos = ["01:30:50", "04:20:30", "02:10:10"]
    tiempos = [validate_time(t) for t in tiempos]
    print(sumar_hora(tiempos)) # output: 8:01:30
