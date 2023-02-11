class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findMode(self, root: TreeNode):
        self.base = None
        self.count = None
        self.max_count = 0
        self.ans = []

        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        if not root:
            return None

        self.dfs(root.left)
        self.update(root.val)
        self.dfs(root.right)

    def update(self, x):
        if x == self.base:
            self.count += 1
        else:
            self.base = x
            self.count = 1

        if self.count == self.max_count:
            self.ans.append(self.base)

        if self.count > self.max_count:
            self.max_count = self.count
            self.ans.clear()
            self.ans.append(self.base)
