"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np


def gss(f, a, b, tol=1e-7):
    phi = (np.sqrt(5) + 1) / 2
    d = b - (b - a) / phi
    c = a + (b - a) / phi
    while abs(d - c) > tol:
        if f(d) < f(c):
            b = c
        else:
            a = d
        d = b - (b - a) / phi
        c = a + (b - a) / phi
    return (a + b) / 2


def gradient_descent_optimal(J, J_grad, x_init, epsilon=1e-10, max_iter=1000):
    x = x_init
    for i in range(max_iter):
        q = lambda alpha: J(x - alpha * J_grad(x))
        alpha = gss(q, 0, 1)
        x = x - alpha * J_grad(x)
        if np.linalg.norm(J_grad(x)) < epsilon:
            return x, i + 1
    return x, max_iter


def f(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


def J(x, y, z):
    return f(x, y, z)


def J_grad(x, y, z):
    return np.array([2 * x, 2 * y, 2 * z])


def main():
    x_init = np.array([1, 1, 1])
    x, n_iter = gradient_descent_optimal(J, J_grad, x_init)
    print(f"x = {x}")
    print(f"n_iter = {n_iter}")


if __name__ == "__main__":
    main()