def solution(s, m):
    count = 0
    slen = len(s)
    
    for _ in range(slen):
        word = s.pop(0)
        index = 1
        for wd in s:
            if index <= m and len(word) == len(wd):
                count += 1
            index += 1
            if index > m:
                break

    return count

print(solution(["back", "seen", "big", "good", "size"], 2))
print(solution(["back", "seen", "good", "size"], 2))