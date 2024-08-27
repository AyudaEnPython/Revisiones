"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from time import perf_counter
import numpy as np

N = 1_000_000
A, B = range(N), range(N)
X, Y = np.array(N), np.array(N)


def time_f(f, *a, **kw):
    t = perf_counter()
    v = f(*a, **kw)
    r = perf_counter() - t
    print(f"Finished {f.__name__!r} in {r:.6f} secs")
    return v


def builtin_list(a, b):
    return [x - y for x, y in zip(a, b)]


def numpy_before(a, b):
    return np.array(a) - np.array(b)


def numpy_after(a, b):
    return a - b


if __name__ == "__main__":
    for f, args in zip(
        (builtin_list, numpy_before, numpy_after),
        ((A, B), (A, B), (X, Y)),
    ):
        time_f(f, *args)
