"""
Date: 12-06-2021
Author: Piyush Gairola
Problem: 871. Minimum Number of Refueling Stops [https://leetcode.com/problems/minimum-number-of-refueling-stops/]
"""


def minRefuelStops(target, startFuel, stations):
    n = len(stations)
    dp = [startFuel] + [0]*n

    for i in range(n):
        for j in range(i,-1,-1):
            if dp[j] >= stations[i][0]:
                dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])

    for i,val in enumerate(dp):
        if val >= target:
            return i

    return -1