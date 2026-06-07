def qsort(nums, low, high):
    if low >= high:
        return 
    pivot = low
    i = low + 1
    j = high
    while i <= j:
        if nums[pivot] < nums[i]:
            while i <= j:
                if nums[pivot] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
                j -= 1
        else:
            i += 1
    nums[j] , nums[pivot] = nums[pivot], nums[j]
    qsort(nums, low, j - 1)
    qsort(nums, j + 1, high)
nums = [4, 6, 2, 5, 7, 9, 1, 3]
qsort(nums, 0, len(nums) - 1)
print(nums)