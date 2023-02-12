class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode):
        self.ans = 0
        if not root:
            return root
        self.dfs(root)

        return root

    def dfs(self, node: TreeNode):
        if node:
            self.dfs(node.right)
            self.ans += node.val
            node.val = self.ans
            self.dfs(node.left)
