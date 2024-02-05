"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: still needs more refactoring...
"""
import numpy as np
from sympy import *


def grad(f, v):
    return [diff(f, v[i]) for i in range(len(v))]


def ev_grad(g, v, u):
    return [
        float(g[i].subs(v[0], u[0]).subs(v[1], u[1]).subs(v[2], u[2]))
        for i in range(len(v))
    ]


def ev_sol(f, v, u):
    return [
        f.subs(v[0], u[0]).subs(v[1], u[1]).subs(v[2], u[2])
        for i in range(len(v))
    ]


def cal_paso(f, g, v, u):
    c = ev_grad(g, v, u)
    t = Symbol('t')
    xt = []
    for i in range(len(v)):
        xt += [float(u[i]) - t*float(c[i])]
    fs = f.subs(v[0], u[0])
    for i in range(1, len(v)):
        fs = fs.subs(v[i], xt[i])
    df = diff(fs, t)
    ddf = diff(df, t)
    s = 1
    for i in range(5):
        s = s - float(df.subs(t, s))/float(ddf.subs(t, s))
    return(s)


def metodo_grad(f, v, u, e, it):
    g = grad(f, v)
    print(f" {u[0]:8.5f} {u[1]:8.5f} {u[2]:8.5f}")
    for k in range(it):
        c = ev_grad(g, v, u)
        fm = ev_sol(f, v, u)
        s = cal_paso(f, g, v, u)
        uk = [
            float(u[i]) - float(s) * float(c[i])
            for i in range(len(v))
        ]
        u = uk.copy()
        print(
            f"{k + 1:3d} {u[0]:8.5f} {u[1]:8.5f} "
            f"{u[2]:8.5f} {fm:12.5e} {s:8.5f}"
        )


def main():
    x, y, z = symbols("x y z")
    Z = (
        (3*x - cos(y*z) - (1/2))**2 +
        ((x**2) - 625*(y**2))**2 +
        (exp(-x*y) + 20*z +
        (10*pi - 3)/3)**2
    )
    v = [x, y, z]
    u = [0, 0, 0]
    metodo_grad(Z, v, u, 1e-10, 40)


if __name__ == "__main__":
    main()
