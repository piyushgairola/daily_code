"""
Date: 04-06-2021
Author: Piyush Gairola
Problem: 52. N-Queens II [https://leetcode.com/problems/n-queens-ii/]
"""

def nQueens(n):
    def dfs(queen,column,normal_diag, reverse_diag):
        row = len(queen)
        if row == n:
            nonlocal ans
            ans += 1
            return
        
        for col in range(n):
            if column & 1<<col or normal_diag & (1<<row+col) or reverse_diag & (1<< row-col+n-1):
                continue
            dfs(queen+[col],column ^ 1<<col, normal_diag ^ 1<<(row+col), reverse_diag ^ 1<<(row-col+n-1))

    ans = 0
    dfs([],0,0,0)

    return ans
