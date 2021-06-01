"""
Date: 01-06-2021
Author: Piyush Gairola
Problem: 695. Max Area of Island [https://leetcode.com/problems/max-area-of-island/]
"""

def maxArea(grid):
    r, c = len(grid), len(grid[0])
    max_area = 0

    def dfs(x, y, grid):
        if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == 0:
            return 0
        grid[x][y] = 0

        up = dfs(x-1, y, grid)
        down = dfs(x+1, y, grid)
        left = dfs(x, y-1, grid)
        right = dfs(x, y+1, grid)

        return up+down+left+right+1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                max_area = max(dfs(i, j, grid), max_area)

    return max_area