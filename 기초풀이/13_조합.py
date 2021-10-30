# 조합: 순서 상관없이 r개 선택하자

# nCr 구하는 프로그램
# nCr = nPr / r!

numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))

resultP = 1
resultR = 1

for n in range(numN, (numN - numR), -1):
    resultP *= n
print('resultP: {}'.format(resultP))

for n in range(numR, 0, -1):
    resultR *= n
print('resultR: {}'.format(resultR))

resultC = resultP / resultR
print('resultC: {}'.format(resultC))