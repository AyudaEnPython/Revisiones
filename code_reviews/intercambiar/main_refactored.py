"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
#from copy import deepcopy
from typing import List
# pip install prototools
from prototools import show_matrix, text_align


def intercambiar(arr: List[List[str]]) -> List[List[str]]:
    # arr_ = deepcopy(x)
    arr_ = [_[:] for _ in arr] 
    arr_[0][2] = arr[1][2]
    return arr_


def main():
    m: List[List[str]] = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
    text_align("'m' antes de intercambiar")
    show_matrix(m)
    v = intercambiar(m)
    text_align("'v' intercambiado")
    show_matrix(v)
    text_align("'m' despues de intercambiar")
    show_matrix(m)


if __name__ == "__main__":
    main()
