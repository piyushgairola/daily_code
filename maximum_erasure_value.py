"""
Date: 05-06-2021
Author: Piyush Gairola
Problem: 1695. Maximum Erasure Value [https://leetcode.com/problems/maximum-erasure-value/]
"""


def maximumSum(nums):
    beg, end = 0, 0
    n = len(nums)
    seen = set()
    curr_sum = 0
    ans = 0

    while(end < n):
        if nums[end] not in seen:
            curr_sum += nums[end]
            seen.add(nums[end])
            ans = max(curr_sum, ans)
            end += 1
        
        else:
            seen.remove(nums[beg])
            curr_sum -= nums[beg]
            beg += 1

    return ans