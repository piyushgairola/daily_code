"""
Date: 14-06-2021
Author: Piyush Gairola
Problem: 199. Binary Tree Right Side View [https://leetcode.com/problems/binary-tree-right-side-view/]
"""

def rightSideView(root):
    def dfs(node,depth):
        if node:
            if len(ans) == depth:
                ans.append(node.val)

            dfs(node.right, depth+1)
            dfs(node, depth+1)

    ans = []
    dfs(root, 0)
    return ans