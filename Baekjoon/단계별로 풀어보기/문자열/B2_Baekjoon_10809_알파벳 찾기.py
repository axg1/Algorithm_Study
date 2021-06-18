s = input() #s를 입력

abc = list('abcdefghijklmnopqrstuvwxyz') #알파벳 존재 유무 확인위해 a~z리스트 만든다

for i in abc: #a부터 z까지 i로 반복
    if i in s: #만약 s안에 i가 있으면
        print(s.index(i), end =' ') #s안에서 i의 위치를 찾는다
    else:
        print(-1, end =' ')