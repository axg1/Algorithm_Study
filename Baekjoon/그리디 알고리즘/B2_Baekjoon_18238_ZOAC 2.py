word = list(input()) #문자열 입력

start = 'A'
time = 0

for i in word:
    left = ord(i)-ord(start) #원판 왼쪽으로 돌리기
    right = ord(start)-ord(i) #원판 오른쪽으로 돌리기

    if left < 0:
        left += 26
    elif right < 0:
        right += 26

    time += min(left,right) #왼쪽과 오른쪽 중 작은 것을 출력!!
    start = i

print(time)