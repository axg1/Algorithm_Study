#커플석LL의 수에 따라서 출력이 결정!!
#커플석이 없거나, 커플석이 1개이면 모두 컵홀더 사용 가능!!/커플석이 2개 이상이라면 좌석수 - LL의 개수 + 1

n = int(input())
b = input()

num = b.count('LL') #B에서 LL이 몇개 들어가있는지 센다

if num <= 1: #만약 LL이 1개 이하이면
    print(n) #모두 컵홀더 사용가능
else: #아니면
    print(n-num+1) #좌석수 - LL의 개수 + 1