n = int(input())
a = list(map(int, input().split())) #리스트를 만들어 점수를 입력받는다

b = [] #빈 배열
for i in range(0,n):
    b.append(a[i]/max(a)*100) #빈 배열에 새로운 점수를 넣는다

result = sum(b)/n #새로운 평균
print(result)