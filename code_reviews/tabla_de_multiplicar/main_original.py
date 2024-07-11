"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
txt1 = "x"
txt2 = "="
txt3 = "Tabla del"
for i in range(1,11):
    print("{:8} {:1}".format(txt3,i))
    for j in range(1,11):
        print("{:<2} {:1} {:2} {:1} {:>2}".format(j,txt1,i,txt2,j*i), end=' ')