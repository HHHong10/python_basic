def maxProduct(words):
    def isUnique(s1, s2):
        for x in s1:
            if s2.find(x) != -1:
                return False
        return True
        
    answer = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if isUnique(words[i], words[j]):
                temp = len(words[i]) * len(words[j])
                answer = max(answer, temp)
    return answer

print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))