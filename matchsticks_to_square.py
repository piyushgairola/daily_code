"""
Date: 15-06-2021
Author: Piyush Gairola
Problem: 473. Matchsticks to Square [https://leetcode.com/problems/matchsticks-to-square/]
"""

def makeSquare(matchsticks):
    def dfs(idx):
        if idx == n:
            return square[0] == square[1] == square[2] == possible_side

        for i in range(4):
            if square[i] + matchsticks[idx] <= possible_side:
                square[i] += matchsticks[idx]

                if dfs(idx+1):
                    return True
                square[i] -= matchsticks[idx]

        
        return False

    if not matchsticks:
        return False

    n = len(matchsticks)
    perimeter = sum(matchsticks)
    possible_side = perimeter//4
    if possible_side*4 != perimeter:
        return False

    matchsticks.sort(reverse= True)

    square = [0]*4

    return dfs(0)