def solution(s):
    s = s.lower()
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return "NO"
        else:
            left += 1
            right -= 1
    return "YES"

print(solution('gooG'))
print(solution('sktS'))