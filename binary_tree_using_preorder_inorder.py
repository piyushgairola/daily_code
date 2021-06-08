class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    def helper(start,end):
        if start>end:
            return None
        node_val = next(preorder)
        idx = inorder_map[node_val]
        node = TreeNode(node_val)
        node.left = helper(start,idx-1)
        node.right = helper(idx+1, end)
        return node

    preorder = iter(preorder)
    inorder_map = {}
    for i,val in enumerate(inorder):
        inorder_map[val] = i

    return helper(0,len(inorder)-1)