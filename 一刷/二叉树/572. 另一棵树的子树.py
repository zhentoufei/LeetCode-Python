class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode):
        return self.dfs(s, t)

    def dfs(self, s: TreeNode, t: TreeNode):
        if s is None:
            return False

        return self.check(s, t) or self.dfs(s.left, t) or self.dfs(s.right, t)

    def check(self, s: TreeNode, t: TreeNode):
        if s is None and t is None:
            return True

        if s is None or t is None or s.val != t.val:
            return False

        return self.check(s.left, t.left) and self.check(s.right, t.right)