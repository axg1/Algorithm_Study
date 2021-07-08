n = int(input())

list_1 = [] #빈 리스트를 만든다
for i in str(n): #n을 str형식으로 만들어서 하나씩 반복
    list_1.append(int(i)) #리스트에 하나씩 추가

list_1.sort(reverse=True) #내림차순으로 정렬

for i in list_1: #리스트요소를 하나씩 반복
    print(i, end="") #하나씩 출력