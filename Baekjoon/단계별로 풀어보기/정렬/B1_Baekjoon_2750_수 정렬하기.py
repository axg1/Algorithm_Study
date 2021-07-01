x = int(input()) #n개의 수 주어진다
num_list = [] #리스트를 만든다
for i in range(x): #x만큼 반복
    num_list.append(int(input())) #리스트에 요소들을 추가
num_list1 = sorted(num_list) #정렬한다
for i in range(len(num_list)): #num_list의 길이만큼 반복
    print(num_list1[i]) #요소들을 출력