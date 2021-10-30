import collections

def solution(s):
    answer = ''
    sH = collections.Counter(s)
    maxVoted = 0

    for [k, v] in sH.items():
        if v > maxVoted:
            maxVoted = v
            answer = k

    return answer

print(solution('BACBACCACCBDEDE'))
print(solution('BACBAFFCCACCBDEDEFFFFF'))