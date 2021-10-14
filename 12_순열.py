# 순열
# nPr 순열 값 구하기 n(n-1)(n-2)...(n-r+1)

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
result = 1

for n in range(numN, (numN - numR), -1):
    print('n : {}'.format(n))
    result *= n

print('result: {}'.format(result))


# 카드 7장 일렬 나열, 3장의 카드 서로 이웃하도록 나열하는 경우의 수
# 이웃 카드를 한 묶음으로 보고 (총 5개의 카드 팩토리얼) * (이웃카드 속 3개 카드 팩토리얼)
fnum1 = int(input('factorial1 입력: '))
result1 = 1
result2 = 1

for n in range(fnum1, 0, -1):
    result1 *= n
print('result1: {}'.format(result1))

fnum2 = int(input('factorial2 입력: '))
for n in range(fnum2, 0, -1):
    result2 *= n
print('result2: {}'.format(result2))

print('모든 경우의 수: {}'.format(result1*result2))
