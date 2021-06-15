"""
Date: 15-06-2021
Author: Piyush Gairola
Problem: 563. Binary Tree Tilt [https://leetcode.com/problems/binary-tree-tilt/]
"""


class Solution:
    def findTilt(self,root):
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            self.tilt_sum += abs(l-r)
            return node.val+l+r

        self.tilt_sum = 0
        dfs(root)
        return self.tilt_sum
