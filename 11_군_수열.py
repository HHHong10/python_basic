# 군수열
# 수열의 합이 최초 100을 초과하는 n번째 항의 값과 n을 출력하는 프로그램
flag = True
n = 1
nCnt = 1; searchNC = 0; searchNP = 0
sumN = 0
while flag:
    for i in range(1, (n+1)):
        print('{}/{} '.format(i,(n - i + 1)), end='')

        sumN += i / (n - i + 1)
        nCnt += 1

        if sumN > 100:
            searchNC = i
            searchNP = n - i + 1
            flag = False
            break

    print()
    n += 1

print("수열의 합이 최초 100을 초과하는 항, 값, 합: {}항, {}/{}, {}".
      format(nCnt, searchNC, searchNP, sumN))