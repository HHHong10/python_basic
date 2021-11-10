def solution(nums, m):
    for _ in range(m):
        for i in range(1, len(nums)):
            nums[i-1] = nums[i] - nums[i-1]
    
    return nums[:-m]

print(solution([5, 3, 7, 9, -2], 1))
print(solution([5, 3, 7, 9, -2], 2))