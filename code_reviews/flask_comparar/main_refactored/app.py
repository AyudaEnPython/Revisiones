"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
from flask import Flask, render_template
from typing import Any, Callable, List

FILES = "data/document_a.csv", "data/document_b.csv"
app = Flask(__name__)


def _get_data(filename) -> List[List[Any]]:
    return pd.read_csv(filename).values.tolist()


def _compare(a: int, b: int) -> str:
    return "diferentes" if a != b else "iguales"


def _message(
    a: str, x: int, b: str, y: int, f: Callable[[int, int], str]
) -> str:
    return f"{a}({x}) y {b}({y}) tienen edades {f(x, y)}."


@app.route('/')
def index():
    return render_template(
        'index.html', 
        results=[
            _message(p, x, q, y, _compare)
            for (p, x), (q, y) in zip(*[_get_data(f) for f in FILES])
        ],
    )


if __name__ == '__main__':
    app.run(debug=True)
