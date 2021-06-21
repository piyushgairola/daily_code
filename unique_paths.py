"""
Date: 21-06-2021
Author: Piyush Gairola
Problem: 62. Unique Paths [https://leetcode.com/problems/unique-paths/]
"""


def uniquePaths(m,n):
    if m==0 or n==0:
        return 0

    if m==1 or n==1:
        return 1

    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]


    return dp[-1][-1]