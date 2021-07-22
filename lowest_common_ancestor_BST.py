"""
Date: 22-07-2021
Problem: 235. Lowest Common Ancestor of a Binary Search Tree [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root,p,q):
    if p.val < root.val > q.val:
        return lowestCommonAncestor(root.left,p,q)
    elif p.val > root.val < q.val:
        return lowestCommonAncestor(root.right,p,q)

    return root