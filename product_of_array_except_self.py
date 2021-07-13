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



def productExceptSelf(nums):
    ans = []
    p = 1
    n = len(nums)

    for i in nums:          ## left elem products
        ans.append(p)
        p = p*i

    p = 1
    for i in range(n-1,-1,-1):  ## right elem products
        ans[i] *= p
        p *= nums[i]

    return ans