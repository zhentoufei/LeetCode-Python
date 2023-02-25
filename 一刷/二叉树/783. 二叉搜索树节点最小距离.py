class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = float('inf')
        self.pre = -1

    def minDiffInBST(self, root: TreeNode):
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return

        self.dfs(node.left)
        if self.pre == -1:
            self.pre = node.val
        else:
            self.ans = min(self.ans, abs(self.pre - node.val))
            self.pre = node.val
        self.dfs(node.right)
