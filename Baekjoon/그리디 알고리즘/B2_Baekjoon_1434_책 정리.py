n, m = input().split() #박스의 개수와 책의 개수 입력

c = list(map(int, input().split())) #박스의 용량 입력
d = list(map(int, input().split())) #책의 크기 입력

print(sum(c)-sum(d)) #c의 합에서 d의 합을 뺀다!!