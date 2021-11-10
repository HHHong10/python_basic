def solution(nums):
    n = len(nums)
    up = 1
    down = 1
    maxup = 0
    maxdown = 0

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            up += 1
        else:
            maxup = max(maxup, up)
            up = 1
        if nums[i] < nums[i-1]:
            down += 1
        else:
            maxdown = max(maxdown, down)
            down = 1
        
    maxup = max(maxup, up)
    maxdown = max(maxdown, down)
    answer = max(maxup, maxdown)

    return answer

print(solution([5, 3, 6, 7, 9, 8, 5, 3, 1, 2]))
print(solution([1, 2, 3, 3, 4, 5, 6, 7, 7]))
