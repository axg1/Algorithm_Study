#Python3는 시간초과!! PyPy3로 제출!!

n = int(input()) #봉우리(활잡이) 수
h = list(map(int, input().split())) #각 봉우리의 높이

a = [] #빈 리스트

for i in range(n-1):
    count = 0
    for j in range(i+1,n):
        if h[i] > h[j]:
            count+=1
        else:
            break
    a.append(count)
print(max(a))