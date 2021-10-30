# 피보나치 수열
# an = a(n-2) + a(n-1)

# n항의 값과 n항까지의 합을 출력하는 프로그램

inputN = int(input('n 입력 : '))

valueN = 0; sumN = 0
valuePreN2 = 0
valuePreN1 = 0

n = 1
while n <= inputN:
    if n==1  or n==2 :
        valueN = 1
        valuePreN2 = valueN
        valuePreN1 = valueN
        sumN += valueN
        n += 1

    else:
        valueN = valuePreN2 + valuePreN1
        valuePreN2 = valuePreN1
        valuePreN1 = valueN
        sumN += valueN
        n += 1

print('{}번째 항의 값: {}'.format(inputN, valueN))
print('{}번째 항까지의 합: {}'.format(inputN, sumN))