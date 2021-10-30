def solution(s):
    s = s + ' '
    answer = ''
    cnt = 1
    n = len(s)

    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            answer += s[i]
            if cnt > 1:
                answer += str(cnt)
            cnt = 1

    return answer

print(solution("KKHSSSSSSSE"))
print(solution("KKHSSSSKKSSSE"))