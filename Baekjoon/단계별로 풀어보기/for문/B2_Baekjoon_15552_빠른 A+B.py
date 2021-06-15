import sys

t = sys.stdin.readline() #시간초과일때는 input 대신 sys.stdin.readline을 사용
for i in range(int(t)):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))
print()