"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np
# pip install prototools
from prototools import time_functions

N = 1_000_000
A, B = range(N), range(N)
X, Y = np.array(N), np.array(N)


def builtin_list(a, b):
    return [x - y for x, y in zip(a, b)]


def numpy_before(a, b):
    return np.array(a) - np.array(b)


def numpy_after(a, b):
    return a - b


if __name__ == "__main__":
    time_functions((builtin_list, numpy_before), args=(A, B), number=1)
    time_functions((numpy_after, ), args=(X, Y), number=1)
