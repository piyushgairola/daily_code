"""
Date: 03-06-2021
Author: Piyush Gairola
Problem: 164. Maximum Gap [https://leetcode.com/problems/maximum-gap/]
"""

from collections import defaultdict

def maximumGap(nums):
    low,high,n = min(nums), max(nums), len(nums)
    if n<=2 or high == low:
        return high-low

    bucket = defaultdict(list)

    for num in nums:
        idx = n-2 if num == high else ((num-low)*(n-1))//(high-low)
        bucket[idx].append(num)

    temp = [[min(bucket[i]), max(bucket[i])] for i in range(n-1) if bucket[i]]

    return max(y[0]-x[1] for x,y in zip(temp, temp[1:]))
    