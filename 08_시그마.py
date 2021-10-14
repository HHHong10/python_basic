# 첫째날 쌀 두톨, 둘째날부터 하루 전의 2배에 해당하는 쌀
# 30일째 되는 날 받게 되는 쌀의 개수를 수열과 시그마로 나타내자

# 등비가 일정한 것이니 while 문 사용

inputA1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0; sumN = 0
n = 1
while n <= inputN:
    if n == 1:
        valueN = inputA1
        sumN += valueN
        print('{}번째 항까지의 합: {}'.format(n, sumN))
        n += 1
        continue

    valueN *= inputR
    sumN += valueN
    print('{}번째 항까지의 합: {}'.format(n, sumN))
    n += 1

# sn = a1 * (1 - r^n) / (1 - r)
sumN = inputA1 * (1 - (inputR ** inputN)) / (1 - inputR)
print('{}번째 항까지의 합: {}'.format(inputN, format(sumN, ',')))