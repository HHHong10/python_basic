import collections
def solution(words):
    for i in range(1, len(words[0]) + 1):
        stringHash = collections.defaultdict(int)
        flag = True
        for j in range(len(words)):
            temp = words[j][:i]
            if stringHash[temp] > 0:
                flag = False
                break
            stringHash[temp] += 1
        if flag:
            break
    answer = i
    return answer

print(solution(["seeasue", "sesseysu", "semeas"]))
print(solution(["ackky", "kabck", "yokkcs"]))
print(solution(["longlong", "longtong", "longbig"]))