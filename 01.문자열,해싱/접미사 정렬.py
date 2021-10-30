def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(s[i:])

    return sorted(answer)

print(solution('kseaedu'))