word = input() #단어 입력
time = 0 #시간을 계산하기 위해 time = 0으로 설정
for i in word: #알파벳을 확인해서 시간을 더해준다
    if i in ['A','B','C']:
        time += 3
    elif i in ['D','E','F']:
        time += 4
    elif i in ['G','H','I']:
        time += 5
    elif i in ['J','K','L']:
        time += 6
    elif i in ['M','N','O']:
        time += 7
    elif i in ['P','Q','R','S']:
        time += 8
    elif i in ['T','U','V']:
        time += 9
    elif i in ['W','X','Y','Z']:
        time += 10
print(time)