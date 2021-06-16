num_all = set(range(1,10001)) #1부터 10000까지 전체 자연수를 집합으로 만든다
num_sang = set() #생성자가 모일 집합

for i in range(1,10001): #1부터 10000까지 반복
    for j in str(i): #i를 문자열로 바꿔서 각 자리수를 분리!! ex)850이라면 8,5,0
        i += int(j) #i에다가 각 자리수를 더해준다!! ex)850+8+5+0
    num_sang.add(i) #생성자로 생겨난 수인 i를 num_sang에 넣어준다

self_num = num_all-num_sang #셀프넘버 = 전체 자연수 - 생성자 숫자
for i in sorted(self_num): #내장함수인 sorted를 사용해 셀프넘버를 정렬하고 반복해서 출력
    print(i)
