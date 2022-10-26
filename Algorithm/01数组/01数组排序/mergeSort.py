def mergesort(left, right):
    arr = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1

    while l < len(left):
        arr.append(left[l])
        l += 1

    while r < len(right):
        arr.append(right[r])
        r += 1

    return arr


def sortArray(nums):
    if len(nums) <= 1:
        return nums

    n = len(nums)//2
    left = sortArray(nums[0:n])
    right = sortArray(nums[n:])
    return mergesort(left, right)


nums = [1, 8, 3, 7, 5, 2]
print(sortArray(nums))
