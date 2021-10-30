# 100부터 1000 사이의 난수에 대해서 약수, 소수, 그리고 소인수를 출력하는 프로그램
import random

rNum = random.randint(100, 1000)

for num in range(1, rNum+1):

    soinsuFlag = 0

    # 약수
    if rNum % num == 0:
        print(f'[약수]: {num}')
        soinsuFlag += 1

    # 소수
    if num != 1:
        flag = True
        for n in range(2, num):
            if num % n == 0:
                flag = False
                break

        if(flag):
            print(f'[소수]: {num}')
            soinsuFlag += 1
            
    # 소인수
    if soinsuFlag >= 2:
        print(f'[소인수]: {num}')
