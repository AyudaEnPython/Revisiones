"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def tabla_del_(n, end=10):
    result = "" 
    for i in range(1, end + 1):
        result += f"{n} x {i} = {n*i}\n"
    return result


if __name__ == "__main__":
    n = 7
    print(f"Tabla del {n}:")
    print(tabla_del_(n))
