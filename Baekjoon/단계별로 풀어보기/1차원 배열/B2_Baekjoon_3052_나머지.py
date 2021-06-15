a = []

for i in range(10): #반복
    b = int(input())
    a.append(b%42) #b를 42로 나눈 나머지를 리스트에 넣어준다

c = set(a) #set은 집합 자료형!! 중복을 제거하기 위한 역할로 종종 사용
print(len(c)) #len으로 길이 출력