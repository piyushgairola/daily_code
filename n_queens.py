"""
Date: 04-06-2021
Author: Piyush Gairola
Problem: 51. N-Queens [https://leetcode.com/problems/n-queens/]
"""

##  Using Backtracking approach
def nQueens(n):
    def dfs(queen, normal_diag, reverse_diag):
        row = len(queen)
        if row == n:
            result.append(queen)
            return

        for col in range(n):
            if col not in queen and row+col not in normal_diag and row-col+n-1 not in reverse_diag:
                dfs(queen+[col], normal_diag+[row+col], reverse_diag+[row-col+n-1])

    result = list()
    dfs([],[],[])

    return [["."*i + "Q" +"."*(n-i-1) for i in sol] for sol in result]


##  Using Bitmasking approach [Faster]
def nQueensBitmasking(n):
    def dfs(queen,column,normal_diag, reverse_diag):
        row = len(queen)
        if row == n:
            result.append(queen)
            return
        
        for col in range(n):
            if column & 1<<col or normal_diag & (1<<row+col) or reverse_diag & (1<< row-col+n-1):
                continue
            dfs(queen+[col],column ^ 1<<col, normal_diag ^ 1<<(row+col), reverse_diag ^ 1<<(row-col+n-1))

    result = []
    dfs([],0,0,0)

    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

