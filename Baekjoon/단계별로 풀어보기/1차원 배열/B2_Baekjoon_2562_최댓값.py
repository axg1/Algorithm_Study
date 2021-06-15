a = [] #빈 배열

for i in range(9): #9번 반복
    a.append(int(input())) #정수로 입력받아 a에 요소 추가
print(max(a))
print(a.index(max(a))+1) #최댓값의 인덱스를 찾음!!인덱스는 0부터시작하므로 1을 더한다