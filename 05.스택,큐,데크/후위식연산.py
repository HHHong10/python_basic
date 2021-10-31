def solution(s):
    stack = []
    for i in s:
        if i.isdigit():
            stack.append(float(i))
        else:
            a = stack.pop()
            b = stack.pop()
            
            if i == '+':
                stack.append(b + a)
            elif i == '-':
                stack.append(b - a)
            elif i == '*':
                stack.append(b * a)
            else:
                stack.append(b / a)
                
    return int(stack[0])

print(solution('352+*9-'))
print(solution('32*56*2/+'))