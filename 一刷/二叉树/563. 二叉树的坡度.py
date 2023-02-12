class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode):
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return 0

        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_right - sum_left)
        return node.val + sum_left + sum_right
