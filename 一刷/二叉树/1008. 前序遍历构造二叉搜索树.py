class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.size = 0
        self.preorder = None
        self.index = 0

    def bstFromPreorder(self, preorder: list):
        self.size = len(preorder)
        self.preorder = preorder
        return self.dfs(float('-inf'), float('inf'))

    def dfs(self, lower, upper):
        if self.index == self.size:
            return None

        current = self.preorder[self.index]
        if current < lower or current > upper:
            return None

        self.index += 1
        root = TreeNode(current)
        root.left = self.dfs(lower, current)
        root.right = self.dfs(current, upper)
        return root
