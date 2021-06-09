a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

sum = a

for i in range(2,n+1):
    sum += d
print(sum)


