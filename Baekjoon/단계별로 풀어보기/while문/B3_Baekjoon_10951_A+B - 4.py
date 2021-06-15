while True:
    try: #try-except 구문 활용
        a, b = map(int, input().split())
        print(a+b)
    except: #예외 발생 시
        break;