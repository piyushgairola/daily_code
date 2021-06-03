"""
Date: 03-06-2021
Author: Piyush Gairola
Problem: 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts [https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/]
"""

def maxArea(h,w,horizontalCuts,verticalCuts):
    def getBlocks(n, cuts):
        t = 0
        blocks = []
        for i in cuts:
            blocks.append(i-t)
            t=i

        if t!=n:
            blocks.append(n-t)

        return blocks
        
    horizontalCuts.sort()
    verticalCuts.sort()
    h_blocks = getBlocks(h,horizontalCuts)
    v_blocks = getBlocks(w,verticalCuts)

    return max(h_blocks)*max(v_blocks)%1000000007