from collections import deque
def solution(need, plan):
    answer = "YES"
    need = deque(need)

    for p in plan:
        if p in need:
            if p != need.popleft():
                answer = "NO"
                break
    else:
        if len(need) == 0:
            answer = "YES"
        else:
            answer = "NO"

    return answer

print(solution('CBA', 'CBDAGE'))
print(solution('CBA', 'CADBGE'))
print(solution('CBA', 'CBDBAGE'))