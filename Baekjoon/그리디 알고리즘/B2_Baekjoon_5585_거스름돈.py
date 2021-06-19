coin = [500, 100, 50, 10, 5, 1] #동전의 종류를 coin 리스트에 넣는다
mon = int(input()) #지불할 돈을 입력받는다
mon2 = 1000-mon #거슬러줄 돈을 계산한다
count = 0 #잔돈의 개수를 구하기 위해 count = 0으로 만든다

for i in coin: #동전을 i에 넣으며 반복
    count += mon2//i #거슬러줄 돈에서 i를 나눈 몫을 카운트한다
    mon2 = mon2%i #다음 계산을 위해 mon2를 동전으로 나눈 나머지로 만들어준다

print(count)