n = int(input()) #단어의 개수 입력
count = n #n개부터 시작해서 그룹단어가 아니면 하나씩 빼는 방식!!

for i in range(n): #단어의 개수만큼 반복
    word = input() #단어 입력
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            #find 함수는 해당 단어의 첫번째 인덱스를 알려준다!! ex)happy는 01224/abbc는 0113/abcaaa는 012000/
            #따라서 숫자가 점차 커지면 그룹함수이고, 앞에 뒤보다 큰 숫자가 나오면 그룹함수가 아니다!!
            count-=1 #그룹함수가 아니므로 하나를 빼준다
            break
print(count)