def solution(nums):
    n = len(nums)
    answer = [0] * n
    left = 0
    right = n-1
    for i in range(n-1, -1, -1):
        if abs(nums[left]) < abs(nums[right]):
            temp = nums[right]
            right -= 1
        else:
            temp = nums[left]
            left += 1
        answer[i] = temp*temp

    return answer

print(solution([-4, -1, 0, 3, 10]))
print(solution([-7, -3, 2, 3, 11]))