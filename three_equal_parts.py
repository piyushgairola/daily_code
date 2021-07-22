"""
Date: 22-07-2021
Problem: 927. Three Equal Parts [https://leetcode.com/problems/three-equal-parts/]
"""

def threeEqualsPart(arr):
    num_ones = 0
    n = len(arr)
    for i in arr:
        if i == 1:
            num_ones += 1

    if num_ones == 0:
        return [0,n-1]
    
    if num_ones%3 != 0:
        return [-1,-1]

    ones_part = num_ones/3
    start,mid,end = 0,0,0
    count_ones = 0

    for i,val in enumerate(arr):
        if val == 1 and count_ones==0:
            start = i
            count_ones +=1
        
        elif val == 1 and count_ones==(ones_part):
            mid = i
            count_ones +=1
        
        elif val == 1 and count_ones==(2*ones_part):
            end = i
            count_ones +=1

        elif val == 1:
            count_ones +=1

    while(end < n and arr[start] == arr[mid] == arr[end]):
        start += 1
        mid += 1
        end += 1

    if end == n:
        return [start-1,mid]

    else:
        return [-1,-1]


arr = [0,0,0,0,0]
print(threeEqualsPart(arr))