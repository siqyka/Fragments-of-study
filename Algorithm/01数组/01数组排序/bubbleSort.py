def sortArray(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


nums = [1, 8, 3, 7, 5, 2]
print(sortArray(nums))
