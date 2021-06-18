t = int(input()) #테스트 케이스 개수
for i in range(t): #t만큼 반복
    a, b = list(input().split()) #입력
    a = int(a)
    b = str(b)
    for i in b: #b의 알파벳 하나씩 i에 넣는다
        print(a*i, end='')
    print()