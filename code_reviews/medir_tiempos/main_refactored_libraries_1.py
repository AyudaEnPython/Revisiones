"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np
# pip install prototools
from prototools import timer

N = 1_000_000
A, B = range(N), range(N)
X, Y = np.array(N), np.array(N)


@timer
def builtin_list(a, b):
    return [x - y for x, y in zip(a, b)]


@timer
def numpy_before(a, b):
    return np.array(a) - np.array(b)


@timer
def numpy_after(a, b):
    return a - b


if __name__ == "__main__":
    builtin_list(A, B)
    numpy_before(A, B)
    numpy_after(X, Y)
