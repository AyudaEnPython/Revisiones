"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
start = 1
end = 10

print("|", end="")
for i in range(start, end+1):
    print(f"tabla del {i:^3}", end=" | ")
print("\r")
print("+", end="")
for i in range(start, end+1):
    print(f" {'-'*11} ", end=" + ")
print("\r")
for i in range(1, 11):
    print("|", end="")
    for j in range(start, end+1):
        print(f"{j:>2} x {i:>2} = {i*j:^3}", end=" | ")
    print()
