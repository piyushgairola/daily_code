"""
Date: 13-07-2021
Problem: 162. Find Peak Element [https://leetcode.com/problems/find-peak-element/]
"""

def findPeakElement(nums):
    left, right = 0,len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid-1] < nums[mid] > nums[mid+1]:       ## can return any peak element
            return mid

        if nums[mid] <nums[mid+1]:
            left = mid+1

        else:
            right = mid-1


    return left if nums[left]>=nums[right] else right