a = int(input())
b = int(input())
c = int(input())
d = a*b*c

e = list(str(d)) #d가 정수면 하나의 요소로 들어가 count로 셀 수 없다!! d를 문자열로 변환!!
for i in range(0,10):
    print(e.count(str(i))) #count는 문자열만 사용가능한 함수