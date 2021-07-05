"""
Date: 05/07/2021
Problem: 576. Out of Boundary Paths [https://leetcode.com/problems/out-of-boundary-paths/]
"""


def findPaths(m,n,maxMove,startRow, startColumn):
    def solve(i,j,moves):
        if moves<0:
            return 0
        if i<0 or i>m-1 or j<0 or j>n-1:
            return 1

        if dp[i][j][moves] != -1:
            return dp[i][j][moves]

        a = solve(i-1,j,moves-1)
        b = solve(i+1,j,moves-1)
        c = solve(i,j-1,moves-1)
        d = solve(i,j+1,moves-1)

        dp[i][j][moves] = a+b+c+d

        return dp[i][j][moves]

    
    dp = [[[-1]*(maxMove+1) for _ in range(n)] for _ in range(m)]

    return solve(startRow,startColumn,maxMove)%(1000000007)

