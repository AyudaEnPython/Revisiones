"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import numpy as np

s=[ ['jose',[15,18,19]], ['maria',[14,17]], ["victoria",[15,13,18,12]], ["kike",[6,15,12]] ]

[print("{}: promedio {} mayor: {} menor: {}".format(i[0],np.mean(i[1]), max(i[1]), min(i[1]))) for i in s]

