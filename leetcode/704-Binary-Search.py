def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = left + ((right - left) // 2)
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
