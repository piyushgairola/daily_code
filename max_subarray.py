def maxSubarray(nums):
    curr_sum = ans = nums[0]
    n = len(nums)

    for i in range(1,n):
        curr_sum = max(curr_sum+nums[i], nums[i])

        ans = max(ans, curr_sum)

    return ans