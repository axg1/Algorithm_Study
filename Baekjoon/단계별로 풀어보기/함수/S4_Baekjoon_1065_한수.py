n = int(input())
hansu = 0 #한수의 개수를 세야하므로 hansu = 0

for i in range(1,n+1):
    if i <= 99: #한자리수나 두자리수는 비교할 다른 자리가 없으므로 1부터 99까지는 모두 한수!!
        hansu += 1

    else:
        ns = list(map(int,str(i))) #숫자를 자릿수마다 분리!!
        if ns[0] - ns[1] == ns[1] - ns[2]: #등차수열 확인
            hansu += 1
print(hansu)