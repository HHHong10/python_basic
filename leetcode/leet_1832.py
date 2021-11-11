import collections
def solution(sentence):
    # stringHash = collections.Counter(sentence)
    # if len(stringHash.keys()) != 26:
    #     return False
    # return True
    return len(collections.Counter(sentence).keys()) == 26

print(solution("thequickbrownfoxjumpsoverthelazydog"))
print(solution("leetcode"))