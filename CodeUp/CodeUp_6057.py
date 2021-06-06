a , b = input().split()
a = int(a)
b = int(b)
print((bool(a) and bool(b)) or (bool(not a) and bool(not b)))