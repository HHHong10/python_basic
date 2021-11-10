import collections
def solution(sentence):
    # answer = True
    # stringHash = {}
    # stringHash = collections.Counter(sentence)
    # if len(stringHash.keys()) != 26:
    #     answer = False
    #     return answer
    # return answer
    return len(collections.Counter(sentence).keys()) == 26

print(solution("thequickbrownfoxjumpsoverthelazydog"))
print(solution("leetcode"))