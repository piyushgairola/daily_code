"""
Date: 07-06-2021
Author: Piyush Gairola
Problem: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers [https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/]
"""

## faster approach.
def minPartition(n):
    for i in range(9,0,-1):
        if str(i) in n:
            return i


## short code.
def min_partition(n):
    return int(max(n))