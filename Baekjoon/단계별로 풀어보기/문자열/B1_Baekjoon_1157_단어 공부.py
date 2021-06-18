word = input().lower() #입력받은 word 변수를 소문자로 입력 ex)word = mississipi
word_list = list(set(word)) #set을 이용해서 중복 제거하고 리스트로 묶는다 word_list = ['m', 'i', 's', 'p']
count_list = [] #count_list를 만들어준다

for i in word_list: #반복!! m,i,s,p를 순서대로 i에 넣는다
    count = word.count(i) #word에서 i가 몇개 있는지 센다
    count_list.append(count) #count_list에 추가

if count_list.count(max(count_list)) >= 2: #만약 가장 많이 사용된 알파벳이 여러개 존재하면
    print("?")
else:
    print(word_list[count_list.index(max(count_list))].upper())