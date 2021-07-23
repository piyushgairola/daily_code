"""
Date: 22-7-2021
Problem: 915. Partition Array into Disjoint Intervals [https://leetcode.com/problems/partition-array-into-disjoint-intervals/]
"""


def partitionDisjoint(nums):
    n = len(nums)
    max_left = [0]*n
    min_right = [0]*n
    
    max_left[0] = nums[0]
    for i in range(1,n):
        max_left[i] = max(max_left[i-1], nums[i])
        
    min_right[-1] = nums[-1]
    for i in range(n-2,-1,-1):
        min_right[i] = min(min_right[i+1],nums[i])
        
    for i in range(1,n):
        if max_left[i-1]<=min_right[i]:
            return i


nums= [5,0,3,8,6]
print(partitionDisjoint(nums))