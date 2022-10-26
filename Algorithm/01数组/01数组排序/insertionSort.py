# 插入排序
def sortArray(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while j > 0 and temp < nums[j-1]:
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

nums = [1, 8, 3, 7, 5, 2]
print(sortArray(nums))
