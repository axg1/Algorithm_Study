h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

result = h*b*c*s/8
result = result/1024
result = result/1024

print(format(result,".1f"), "MB")