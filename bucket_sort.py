"""
Date: 03-06-2021
Author: Piyush Gairola
Problem: Bucket Sort Implementation
"""

from collections import defaultdict


def bucket_sort(arr):
    n = len(arr)
    max_elem = max(arr)
    size_of_bucket = max_elem/n
    buckets = defaultdict(list)
    
    for i in arr:
        idx = i//size_of_bucket
        if idx == n:
            buckets[idx-1].append(i)
        else:
            buckets[idx].append(i)

    res = []
    for i in range(n):
        res.extend(insertion_sort(buckets[i]))

    return res

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = key

    return arr
