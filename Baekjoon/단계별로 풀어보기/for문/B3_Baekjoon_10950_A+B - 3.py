t = int(input()) #테스트 케이스의 개수t
for i in range(t): #t만큼 테스트 케이스를 입력받기
    a, b = map(int, input().split())
    print(a+b)