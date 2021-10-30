import collections

def solution(s1, s2):
    H1 = collections.Counter(s1)
    
    for s in s2:
        if s in H1:
            H1[s] -= 1
            if H1[s] == 0:
                del H1[s]
            
    if not H1:
        return "TES"
    else:
        return "NO"

print(solution('abaCC', 'Caaab'))