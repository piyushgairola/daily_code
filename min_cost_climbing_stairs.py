"""
Date: 07-06-2021
Author: Piyush Gairola
Problem: 746. Min Cost Climbing Stairs [https://leetcode.com/problems/min-cost-climbing-stairs/]
"""


def minCostClimbingStairs(costs):
    n  = len(costs)
    dp = [None]*n

    for i in range(n):
        if i<2:
            dp[i] = costs[i]
        else:
            dp[i] = costs[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])