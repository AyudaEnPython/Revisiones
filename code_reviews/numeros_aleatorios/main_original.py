"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random

limit = 6
count = 0
set = []
while count < limit:
    def checkFucn():
        value = random.randint(0, 48)

        if value not in set:
            set.append(value)
            count = count + 1
        
        else:
            checkFucn()


print(set)
