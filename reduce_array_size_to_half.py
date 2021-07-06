"""
Date: 06-07-2021
Problem: 1338. Reduce Array Size to The Half [https://leetcode.com/problems/reduce-array-size-to-the-half/]
"""

def minSetSize(arr):
    count_map = {}
    for i in arr:
        if i in count_map:
            count_map[i]  += 1
        else:
            count_map[i] = 1

    freq = list(count_map.values())
    freq.sort()

    ans, reduced_size, half_size = 0,0,len(arr)//2
    while reduced_size<half_size:
        ans += 1
        reduced_size += freq.pop()

    return ans