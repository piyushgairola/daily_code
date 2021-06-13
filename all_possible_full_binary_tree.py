"""
Date: 13-06-2021
Author: Piyush Gairola
Problem: 894. All Possible Full Binary Trees [https://leetcode.com/problems/all-possible-full-binary-trees/]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPossibleFBT(n, memo={0:[],1:[TreeNode(0)]}):
    if n not in memo:
        ans = []
        for i in range(n):
            for left in allPossibleFBT(i,memo):
                for right in allPossibleFBT(n-i-1,memo):
                    node = TreeNode(0)
                    node.left = left
                    node.right = right

                    ans.append(node)

        memo[n] = ans
    
    return memo[n]
