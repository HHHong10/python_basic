# 확률
# 박스에 '꽝' 6장, '선물' 4장
# '꽝' 3장, '선물' 3장 뽑는 확률
# (6C3 * 4C3) / 10C6

def proFun():
    numN = int(input('numN 입력: '))
    numR = int(input('numR 입력: '))

    resultP = 1
    resultR = 1
    resultC = 1

    # 순열(P)
    for n in range(numN, (numN - numR), -1):
        resultP *= n
    print("resultP: {}".format(resultP))

    # R(f)
    for n in range(numR, 0, -1):
        resultR *= n
    print("resultR: {}".format(resultR))

    # 조합(C)
    resultC = int(resultP / resultR)
    print("resultC: {}".format(resultC))

    return resultC

sample = proFun()
print('sample: {}'.format(sample))

event1 = proFun()
print('event1: {}'.format(event1))

event2 = proFun()
print('event2: {}'.format(event2))

print('result: {}%'.format(round(((event1*event2)/sample)*100, 2)))