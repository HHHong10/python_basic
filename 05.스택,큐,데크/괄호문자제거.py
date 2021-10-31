def solution(s):
    stack = []
    for i in s:
        if i == ')':
            while stack.pop() != '(':
                continue
        else:
            stack.append(i)

    return "".join(stack)

print(solution('(A(BC)D)EF(G(H)(IJ)K)LM(N)'))