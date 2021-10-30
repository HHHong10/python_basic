def solution(s):
    answer  = list(s)
    left = 0
    right = len(s)-1

    while left < right:
        if not answer[left].isalpha():
            left += 1
        elif not answer[right].isalpha():
            right -= 1
        else:
            temp = answer[left]
            answer[left] = answer[right]
            answer[right] = temp
            right -= 1
            left += 1

    return "".join(answer)

print(solution('a#b!GE*T@S'))