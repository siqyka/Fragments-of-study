# 选择排序
def sortArray(nums):
    # len(nums)-1：因为后面循环是从i+1开始的，最后一次循环只要对比最后两个数即可，所以是长度-1次循环
    for i in range(len(nums)-1):
        min = i
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                min = j
        if min != i:
            nums[i], nums[min] = nums[min], nums[i]
    return nums


nums = [1, 8, 3, 7, 5, 2]
print(sortArray(nums))
