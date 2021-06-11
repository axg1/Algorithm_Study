h, w = input().split()
h = int(h)
w = int(w)

z = [[0]*(w+1) for _ in range(h+1)]

n = int(input())
for i in range(n):
    l, d, x, y = input().split()
    if int(d) == 0:
        for j in range(int(l)):
            z[int(x)][int(y)+j] = 1
    else:
        for j in range(int(l)):
            z[int(x)+j][int(y)] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(z[i][j], end=' ')
    print()