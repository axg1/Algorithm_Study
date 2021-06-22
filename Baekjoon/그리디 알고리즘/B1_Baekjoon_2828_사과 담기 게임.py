n, m = map(int, input().split()) #스크린, 바구니 입력
j = int(input()) #떨어지는 사과의 개수 입력

apples = [int(input()) for i in range(j)] #사과가 떨어지는 위치를 순서대로 입력

size = m-1 #바구니 크기!! 왼쪽 제외
left = 1 #바구니 왼쪽 끝의 위치
right = left + size #바구니 오른쪽 끝의 위치
count = 0

for i in apples:
    if left <= i <= right: #사과가 바구니 안에 들어갈 수 있는 위치라면 바구니를 움직이지 않는다
        continue

    if i < left: #사과가 바구니의 왼쪽에 있다면
        count += abs(left-i) #바구니 왼쪽을 사과의 위치까지 이동한 횟수
        left = i #바구니 왼쪽을 사과의 위치까지 이동
        right = i + size #바구니 오른쪽도 이동
        continue

    if i > right: #사과가 바구니 오른쪽에 있다면
        count += abs(i-right) #바구니 오른쪽을 사과의 위치까지 이동한 횟수
        right = i #바구니 오른쪽을 사과의 위치까지 이동
        left = i - size #바구니 왼쪽도 이동

print(count)



