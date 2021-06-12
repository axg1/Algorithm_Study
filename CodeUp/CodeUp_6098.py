m = [list(map(int, input().split())) for i in range(10)]

x, y = 1, 1
m[1][1] = 9

while True:
    if m[x][y + 1] == 0:
        y += 1
        m[x][y] = 9

    elif m[x][y + 1] == 1:
        if m[x + 1][y] == 1:
            break
        elif m[x + 1][y] == 2:
            x += 1
            m[x][y] = 9
            break
        else:
            x += 1
            m[x][y] = 9

    else:
        y += 1
        m[x][y] = 9
        break

for i in m:
    print(' '.join(map(str, i)))