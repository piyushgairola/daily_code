"""
Date: 16-07-2021
Problem: 611. Valid Triangle Number [https://leetcode.com/problems/valid-triangle-number/]
"""

def triangleNumber(nums):
    nums.sort()
    n = len(nums)
    ans = 0
    for i in range(n-1,1,-1):
        side = nums[i]
        start,end = 0,i-1

        while start<end:
            if nums[start]+nums[end] > side:
                ans += end - start
                end -= 1
            else:
                start += 1

    return ans