import math

def solution(s):
    answer = 0
    for i in s:
        if i.isdecimal():
            answer = answer*10 + int(i)
    # prime = isPrime(answer)
    return answer

# 소수판별
def isPrime(n):
    if n < 2:
        return False
    rang = int(math.sqrt(n))
    for i in range(2, rang+1):
        if n % i == 0:
            return False
    return True

print(solution('g0en2T0s8eSoft'))