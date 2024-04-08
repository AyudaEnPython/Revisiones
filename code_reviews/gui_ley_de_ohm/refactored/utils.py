"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple

VARIANTS: Dict[str, Tuple[str]] = {
    "Voltaje": ("Intensidad", "*" , "Resistencia"),
    "Intensidad": ("Voltaje", "/","Resistencia"),
    "Resistencia": ("Voltaje", "/", "Intensidad"),
}


def _clean(ws: object) -> None:
    for w in ws:
        w.delete(0, "end")


def _table(x: float, y: float, s: str) -> float:
    return {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y,
    }[s]


def calculate(x: object, op: str, y: object, r: object) -> None:
    try:
        t = _table(float(x.get()), float(y.get()), op)
    except ValueError:
        r.config(text="Valores incorrectos")
        _clean((x, y))
    except ZeroDivisionError:
        r.config(text="Error, división entre cero")
        _clean((x, y))
    else:
        r.config(text=t)
