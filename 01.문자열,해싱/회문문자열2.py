def solution(s):
    s = s.lower()
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            subL = s[left:right]
            subR = s[left+1:right+1]
            if subL != subL[::-1] and subR != subR[::-1]:
                return "NO"
            break
        else:
            left += 1
            right -= 1

    return "YES"

print(solution('abcbdcba'))
print(solution('abcabbakcba'))
print(solution('abcacbakcba'))