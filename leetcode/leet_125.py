def isPalindrome(s):
    result = ''
    for x in s:
        if x.isalnum():
            result += x

    return  result == result[::-1]

print(isPalindrome("race a car"))