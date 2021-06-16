c = int(input())

for i in range(c): #c만큼 반복
    a = list(map(int, input().split())) #리스트a 안에 입력받은 값을 넣는다
    avg = sum(a[1:])/a[0] #평균을 구한다
    count = 0 #평균을 넘는 학생들의 수를 구하기 위해 count를 만든다

    for i in a[1:]: #리스트a의 1번 인덱스부터 값들을 차례대로 i에 넣는다
        if i > avg: #만약 평균 이상이면
            count += 1 #평균이상 학생 수는 +1
    rate = ((count/a[0])*100) #비율
    print(f'{rate:.3f}%') #소수점 자리까지 출력