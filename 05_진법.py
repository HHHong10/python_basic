# 사용자가 입력한 수를 이용해서, 다음 내용에 따라 진법 변환하는 코드
# 10 진수 >> 2, 8, 16진수 변환
# x 진수 >> 10 진수
# x 진수 >> x 진수

dNum = int(input('10진수 입력: '))

print('2진수: {}'.format(bin(dNum)))
print('8진수: {}'.format(oct(dNum)))
print('16진수: {}'.format(hex(dNum)))

print('2진수(0b10101) -> 10진수({})'.format(int('0b10101', 2)))
print('8진수(0o135) -> 10진수({})'.format(int('0o135', 8)))
print('16진수(0x5f) -> 10진수({})'.format(int('0x5f', 16)))
