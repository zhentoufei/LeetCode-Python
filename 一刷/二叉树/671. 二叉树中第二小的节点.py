class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.root_value = None
        self.ans = None

    def findSecondMinimumValue(self, root: TreeNode):
        self.ans = -1
        self.root_value = root.val
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):

        if not root:
            return

        if self.ans != -1 and root.val >= self.ans:
            return

        if root.val > self.root_value:
            self.ans = root.val

        self.dfs(root.left)
        self.dfs(root.right)
