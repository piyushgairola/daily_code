"""
Date: 06-06-2021
Author: Piyush Gairola
Problem: 968. Binary Tree Cameras. [https://leetcode.com/problems/binary-tree-cameras/]
"""

def minCameraCover(root):
    camera = 0
    covered = {None}

    def dfs(root, parent=None):
        if root:
            dfs(root.left, root)
            dfs(root.right, root)

            if parent is None and root not in covered or root.left not in covered or root.right not in covered:
                nonlocal camera
                camera += 1

                covered.update({root, parent, root.left, root.right})

    dfs(root)

    return camera
