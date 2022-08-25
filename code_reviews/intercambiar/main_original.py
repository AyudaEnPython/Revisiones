"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
m=[["1","2","3"],["4","5","6"],["7","8","9"]]
print(m[0])
print(m[1])
print(m[2])
def intercambiar(x):
    matrix=x
    matrix[0][2]=x[1][2]
    #mostrar matriz x que es el argumento
    print("mostrar matriz x que es el argumento")
    print(x)
    print("---")
    return matrix

print("**********")
print(intercambiar(m))