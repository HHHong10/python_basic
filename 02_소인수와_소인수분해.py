# 100부터 1000사이의 난수를 소인수분해 하고 각각의 소인수에 대한 지수를 출력하는 프로그램
import random

rNum = random.randint(100, 1000)

soinsuList = []

n = 2
while n <= rNum:
    if rNum % n == 0:
        print(f'소인수: {n}')
        soinsuList.append(n)
        rNum /= n
    else:
        n += 1

print(f'soinsuList: {soinsuList}')

tempN = 0
for s in soinsuList:
    if tempN != s:
        print(f'{s}\'s count: {soinsuList.count(s)}')
        tempN = s