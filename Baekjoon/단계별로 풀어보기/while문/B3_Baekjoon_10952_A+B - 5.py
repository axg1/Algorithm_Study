while True: #while문을 계속 반복
    a, b = map(int, input().split())
    if a==0 and b==0: #만약 a와 b가 0이라면
        break;
    else:
        print(a+b)