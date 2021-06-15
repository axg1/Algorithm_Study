n = int(input()) #문자열 인덱스로 푸는 것이 생각보다 어렵다!! 정수로 푸는 것이 편리!!
num = n #n의 값을 num에 저장해서 계산!! 나중에 원래 n의 값과 비교해야 하니까!!
count = 0

while True:
    a = num//10 #십의 자리
    b = num%10 #일의자리
    c = (a+b)%10 #십의자리+일의자리 계산한 값의 일의자리
    num = int(str(b)+str(c)) #문자열 형식으로 합치고 정수형으로 변환

    count = count+1 #사이클 길이 추가
    if n == num:
        break;

print(count)