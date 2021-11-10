def solution(nums):
    answer = 0
    height = 0
    n = len(nums)
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            height += (nums[i] - nums[i-1])
        else:
            answer = max(answer, height)
            height = 0
    answer = max(answer, height)
    return answer

print(solution([5, 2, 4, 7, 7, 3, 9, 10, 11]))
print(solution([8, 12, 2, 3, 7, 6, 20, 3]))