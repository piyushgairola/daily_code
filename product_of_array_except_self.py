"""
Date: 10/7/2021
Problem: 238. Product of Array Except Self [https://leetcode.com/problems/product-of-array-except-self/]
"""

def productExceptSelf(nums):
    max_prod = min_prod = ans = nums[0]
    n = len(nums)

    for i in range(1,n):
        max_prod = max(max_prod*nums[i], min_prod*nums[i], nums[i])
        min_prod = min(max_prod*nums[i], min_prod*nums[i], nums[i])

        ans = max(ans, max_prod)

    return ans