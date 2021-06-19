#직접 그림을 그려보면 이해하기 쉽다!!
while True:
    try: #try-except 구문 활용
        A, B, C = map(int, input().split())
        print(max(B-A,C-B)-1) #B와A사이의 거리와 C와B사이의 거리 중 큰 것을 고르고 1을 빼준다
    except: #예외 발생 시
        break;