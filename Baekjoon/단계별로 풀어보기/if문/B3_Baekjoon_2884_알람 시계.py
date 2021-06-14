h, m = map(int, input().split())

if m>=45:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m-45+60) #시에서 1을 빼고 분에서 45를 뺀뒤 60을 더한다
elif m<45 and h==0:
    print(23, m-45+60) #시는 23을 출력하고 분에서 45를 뺀뒤 60을 더한다