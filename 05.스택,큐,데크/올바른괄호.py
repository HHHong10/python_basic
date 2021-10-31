def solution(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()

    if len(stack) > 0:
        return "NO"

    return "YES"

print(solution('(()(()))(()'))
print(solution('(())()'))
print(solution(')))((('))