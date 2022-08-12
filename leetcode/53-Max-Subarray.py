def maxSubArray(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0
        currSum += num
        maxSum = max(maxSum, currSum)

    return maxSum


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([1]))
print(maxSubArray([5, 4, -1, 7, 8]))
