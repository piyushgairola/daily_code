"""
Date: 14-06-2021
Author: Piyush Gairola
Problem: 1038. Binary Search Tree to Greater Sum Tree [https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/]
"""

class Solution:
    def bstToGst(self, root):
        def postOrder(node):
            if node:
                postOrder(node.right)
                node.val = self.ans = node.val +self.ans
                postOrder(node.left)

                return root

        self.ans = 0
        postOrder(root)
        return self.ans

        

        