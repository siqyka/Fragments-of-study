def quick_sort(lists,i,j):
    if i >= j:
        return 
    pivot = lists[i]
    low = i
    high = j
    while i < j:
        while i < j and lists[j] >= pivot:
            j -= 1
        lists[i]=lists[j]
        while i < j and lists[i] <=pivot:
            i += 1
        lists[j]=lists[i]
    lists[j] = pivot
    quick_sort(lists,low,i-1)
    quick_sort(lists,i+1,high)
    return lists

nums = [1, 8, 3, 7, 5, 2]
print(quick_sort(nums,0,len(nums)-1))
