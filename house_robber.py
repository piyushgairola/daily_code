"""
Date: 29-07-2021
Problem: 198. House Robber [https://leetcode.com/problems/house-robber/]
"""


def rob(nums):    
    def helper(i):
        if i<0:
            return 0
        
        if dp[i]>=0:
            return dp[i]
        else:                
            res = max(helper(i-2)+nums[i], helper(i-1))
            dp[i] = res
            return res
    
    n = len(nums)
    dp = [-1]*(n+1)
        
    return helper(n-1)


def rob_dp_iterative(nums):
    n = len(nums)
    dp = [-1]*(n+1)
    dp[0] = 0
    dp[1] = nums[0]

    for i in range(1,n):
        dp[i+1] = max(dp[i-1]+nums[i], dp[i])

    return dp[n]


def rob_const_time(nums):
    a = b = 0
    for i in range(len(nums)):
        t = a
        a = max(nums[i]+b, a)
        b = t

    return b

nums = [1,2,3,1]
print(rob_const_time(nums))