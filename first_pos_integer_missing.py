"""
Date: 08-06-2021
Author: Piyush Gairola

Problem Statement:
    This problem was asked by Stripe.

    Given an array of integers, find the first missing positive integer in linear time and constant space. 
    In other words, find the lowest positive integer that does not exist in the array. 
    The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
"""


def getMissingPos(nums):                            #### Time Complexity= O(n)     Space Complexity= O(1)
    def seperate_pos_neg(nums):
        nonlocal j
        for i in range(n):
            if nums[i]<=0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1

    n = len(nums)
    j = 0
    seperate_pos_neg(nums)

    size = n-j
    nums = nums[j:]

    for i in range(size):
        if abs(nums[i])-1 < size and nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

    for i in range(size):
        if nums[i] > 0:
            return i+1

    return size+1


def getMissingPostive_usingList(nums):              #### Time Complexity= O(n)     Space Complexity= O(n)
    n = len(nums)
    m = max(nums)

    l = [0]*m

    for i in range(n):
        if nums[i]>0:
            if l[nums[i]-1] != 1:
                l[nums[i] - 1] = 1

    for i in range(m):
        if l[i] != 1:
            return i+1

    return n+1