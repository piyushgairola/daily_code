"""
Date: 17-06-2021
Author: Piyush Gairola
Problem: 795. Number of Subarrays with Bounded Maximum [https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/]
"""


def numSubarrayBoundedMax(nums,left,right):
    window_start,temp,ans = 0,0,0

    for i,val in enumerate(nums):
        if left<=val<=right:
            temp = i-window_start+1
            ans += temp
        
        elif val < left:
            ans += temp

        else:
            window_start = i+1
            temp = 0

    return ans