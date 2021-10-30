# 수열의 일반항을 구하고, n항의 값을 출력하는 프로그램
# 계차수열

# an = (3n^2 - 2n + 4) / 2

inputA1 = int(input('a1 입력 : '))
inputN = int(input('an 입력 : '))

valueN = ((3 * inputN ** 2) - (3 * inputN) + 4) / 2
print('an의 {}번째 항의 값: {}'.format(inputN, int(valueN)))
