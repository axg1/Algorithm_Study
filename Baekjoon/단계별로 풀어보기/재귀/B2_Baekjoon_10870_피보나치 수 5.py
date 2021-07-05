def fibonacci(n): #함수의 이름을 fibonacci로 짓는다
    if n == 0 or n == 1: #만약 n이 0이나 1이면
        return n #n을 그대로 리턴한다
    return fibonacci(n-1) + fibonacci(n-2) #아니면 앞의 두 수를 더한 값을 리턴한다

#위의 함수를 활용하여 실제 코드 작성
n = int(input())
print(fibonacci(n))