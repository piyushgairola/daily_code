"""
Date: 23-07-21
Problem: 814. Binary Tree Pruning [https://leetcode.com/problems/binary-tree-pruning/]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pruneTree(root):
    if not root: return None
    root.left = pruneTree(root.left)
    root.right = pruneTree(root.right)
    if not root.left and not root.right and not root.val:
        return None
    return root