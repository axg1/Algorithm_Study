t = int(input()) #테스트 케이스 개수t

for i in range(t): #t만큼 반복
    oxqz = input() #ox퀴즈 입력받는다
    a = list(oxqz)
    score = 0 #최종점수
    count = 0 #O의 수 카운트

    for i in a: #리스트a에 있는 값들을 i에 하나씩 넣으면서 반복
        if i == "O": #만약 리스트 안에 O가 있다면
            count += 1 #count에 1을 더하고
            score += count #최종점수에 count만큼 더해서 누적
        elif i =="X": #만약 X일 경우
            count = 0 #count 초기화
    print(score)