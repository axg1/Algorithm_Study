a, b = input().split()
a = int(a)
b = int(b)
print((bool(a) and bool(not b)) or (bool(b) and bool(not a)))