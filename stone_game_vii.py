"""
Date: 12-06-2021
Author: Piyush Gairola
Problem: 1690. Stone Game VII [https://leetcode.com/problems/stone-game-vii/]
"""


from itertools import accumulate


def stoneGameVII(stones):
    n = len(stones)
    stones_sum = [0] + list(accumulate(stones))
    dp = [[0]*n for _ in range(n)]

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            dp[i][j] = max(stones_sum[j+1] - stones_sum[i+1] - dp[i+1][j], stones_sum[j] - stones_sum[i] - dp[i][j-1])


    return dp[0][n-1]