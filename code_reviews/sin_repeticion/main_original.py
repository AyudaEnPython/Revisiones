"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# Copyright © 2022 TrinityXel
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def main():
    resultado = []
    # Pediremos una lista de numeros, divididos cada uno por ","
    x = str(input("Ingrese valor de X: "))
    y = str(input("Ingrese el valor de Y: "))

    # Creamos la lista, dividiendo la cadena en elementos divididos por ","
    n = x.split(",")
    m = y.split(",")

    # Veremos cual es la lista mas chica
    listaG, listaC = ([m,n],[n,m]) [n <= m ]

    for item in range(len(listaC)):
        if listaC[item] in listaG:
            if not listaC[item] in resultado:
                resultado.insert(item, listaC[item])

    print(resultado)


if __name__ == "__main__":
    main()
