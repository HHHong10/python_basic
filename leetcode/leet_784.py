def letterCasePermutation(s):
    if s.isnumeric():
        return [s]

    answer = []
    n = len(s)
    def DFS(l, path):
        if l == n:
            answer.append(path)
        else:
            if s[l].isnumeric():
                DFS(l+1, path+s[l])
            else:
                DFS(l+1, path+s[l].lower())
                DFS(l+1, path+s[l].upper())
    DFS(0,'')
    return answer

print(letterCasePermutation('a1b2'))
# print(letterCasePermutation('3z4'))
# print(letterCasePermutation('12345'))