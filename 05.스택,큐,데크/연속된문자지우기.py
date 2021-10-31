def solution(s):
    stack = []
    for i in s:
        if len(stack) and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return ''.join(stack)

print(solution('acbbcaa'))
print(solution('bacccaba'))