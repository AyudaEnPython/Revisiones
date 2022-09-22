"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

n = int(input("n: "))
s = i = 0
x = 2
while i != n:
    s += x
    x += 2
    i += 1
print(f"Result: {s}")

n = int(input("n: "))
s = 0
for x in range(2, 2*n+1, 2):
    s += x
print(f"Result: {s}")

# print(f"Result: {n*(n + 1)}")
# print(f"Result: {sum(range(2, 2*n+1, 2))}")
