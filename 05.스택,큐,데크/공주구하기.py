from collections import deque
def solution(n, k):
    stack = deque(list(range(1, n + 1)))

    while stack:
        for _ in range(k-1):
            stack.append(stack.popleft())
        stack.popleft()
        if len(stack) == 1:
            return stack[0]

    return False

def solutionB(n, k):
    stack = deque(list(range(1, n + 1)))

    while len(stack) > 1:
        stack.rotate(-(k-1))
        stack.popleft()
    
    return stack[0]

print(solution(8, 3))
print(solution(4, 2))

print(solutionB(8, 3))
print(solutionB(4, 2))