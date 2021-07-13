"""
Date: 13-07-2021
Problem: 33. Search in Rotated Sorted Array [https://leetcode.com/problems/search-in-rotated-sorted-array/]
"""

def search(nums,target):
    left,right = 0, len(nums)-1

    while left<right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1

        else:
            if nums[mid]<= target<= nums[right]:
                left = mid+1
            else:
                right = mid-1


    return left if nums[left]==target else -1