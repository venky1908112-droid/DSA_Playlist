def solve(nums):
    ans_start = 0
    ans_end = 0
    curr_sum = 0
    max_sum = float('-inf')
    start = 0
    for i in range(len(nums)):
        if curr_sum <= 0:
            curr_sum = nums[i]
            start = i
        else:
            curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            ans_start = start
            ans_end = i
        
    return (ans_start, ans_end)

nums = [2, 3, -8, 7, -1, 2, 3]
print(solve(nums))