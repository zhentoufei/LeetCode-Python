class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode):
        self.pre = -1
        self.ans = float('inf')
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return
        self.dfs(node.left)
        if self.pre == -1:
            self.pre = node.val
        else:
            self.ans = min(self.ans, node.val - self.pre)
            self.pre = node.val
        self.dfs(node.right)
