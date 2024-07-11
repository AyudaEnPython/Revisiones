"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
start = 1
end = 10

for i in range(start, end+1):
    print(f"tabla del {i:^3}", end=" ")
print("\r")
for i in range(1, 11):
    for j in range(start, end+1):
        print(f"{j:>2} x {i:>2} = {i*j:^3}", end=" ")
    print()
