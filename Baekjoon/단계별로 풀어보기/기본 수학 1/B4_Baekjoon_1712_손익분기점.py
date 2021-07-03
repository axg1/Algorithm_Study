a, b, c = map(int, input().split())
#고정비용a + (가변비용b x n) = (노트북가격c x n)
#n으로 정리하면 n = a/(c-b)
if b >= c: #가변비용 > 노트북 가격
    print(-1)
else:
    print(a//(c-b)+1) #a//(c-b)는 손익분기점일 때를 의미!! 따라서 최초로 이익이 발생하는 시점은 +1