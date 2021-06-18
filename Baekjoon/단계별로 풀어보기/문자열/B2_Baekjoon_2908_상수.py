a, b = list(map(str, input().split())) #두개의 숫자를 str로 입력
c = a[2]+a[1]+a[0] #a를 거꾸로
d = b[2]+b[1]+b[0] #b를 거꾸로

if c > d:
    print(c)
else:
    print(d)