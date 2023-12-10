class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.total = 0

    def bstToGst(self, root: TreeNode):
        def dfs(node: TreeNode):
            if node is not None:
                dfs(node.right)
                self.total += node.val
                node.val = self.total
                dfs(node.left)

        dfs(root)
        return root
