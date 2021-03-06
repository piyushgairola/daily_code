"""
Date: 14-06-2021
Author: Piyush Gairola
Problem: 110. Balanced Binary Tree [https://leetcode.com/problems/balanced-binary-tree/]
"""


def isBalanced(root):
    def getHeight(node):
        if root is None:
            return 0

        l_height = getHeight(root.left)
        r_height = getHeight(root.right)

        if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1:
            return -1

        return max(l_height,r_height)+1


    return getHeight(root) != -1