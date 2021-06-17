a = int(input()) #숫자의 개수 입력
i = int(input()) #숫자들 입력
b = list(map(int, str(i))) #i에 입력받은 숫자를 문자열로 바꿔서 리스트에 하나씩 넣음!!
print(sum(b)) #리스트에 있는 요소들의 합