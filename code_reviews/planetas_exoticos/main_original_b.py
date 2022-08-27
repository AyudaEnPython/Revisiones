"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random as r

vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', \
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
    't', 'v', 'w', 'x', 'y', 'z',
    ]
np = [] # contenedor para los nombres de los planetas
for i in range(10):
    len_name = r.randint(4, 7)
    init_letter = True
    name = ''
    while len_name > 0:
        if init_letter:
            name += vocales[r.randint(0, 4)]
            init_letter = False
        else:
            name += consonantes[r.randint(0, 4)]
            init_letter = True
        len_name = len_name - 1
    np.append(name.capitalize())
    name = ''
    init_letter = True

[print(name) for name in sorted(np)]