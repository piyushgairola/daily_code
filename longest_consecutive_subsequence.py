"""
Date: 06-06-2021
Author: Piyush Gairola
Problem: 128. Longest Consecutive Sequence. [https://leetcode.com/problems/longest-consecutive-sequence/]
"""


def longestConsecutive(nums):
    nums = set(nums)
    ans = 0

    for x in nums:
        if x-1 not in nums:
            y = x+1
            while y in nums:
                y+=1
            
            ans = max(ans, y-x)

    return ans