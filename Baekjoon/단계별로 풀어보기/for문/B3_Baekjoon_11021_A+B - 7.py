t = int(input())

for i in range(1,t+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a+b)#i는 정수이지만 같이 붙여쓰기 위해서 문자열인 str로 바꿔준다