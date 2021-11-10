def solution(nums, m):
    ch = [0] * 1001
    maxH = float('-inf')
    minH = float('inf')
    for x in nums:
        ch[x] += 1
        if x > maxH:
            maxH = x
        if x < minH:
            minH = x
    
    for _ in range(m):
        if maxH == minH:
            return 0
        if ch[maxH] == 1:
            ch[maxH] -= 1
            maxH -= 1
            ch[maxH] += 1
        else:
            ch[maxH] -= 1
            ch[maxH-1] += 1
        if ch[minH] == 1:
            ch[minH] -= 1
            minH += 1
            ch[minH] += 1
        else:
            ch[minH] -= 1
            ch[minH+1] += 1
    
    answer = maxH - minH
    return answer

print(solution([2, 1, 3, 7, 5], 2))
print(solution([69, 42, 68, 76, 40, 87, 14, 65, 76, 81], 50))
