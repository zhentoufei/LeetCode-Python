class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidBST(self, root: TreeNode):
        return self.backtrack(root, float('-inf'), float('inf'))

    def backtrack(self, root: TreeNode, lower, upper):
        if root is None:
            return True

        val = root.val
        if val <= lower or val >= upper:
            return False

        if self.backtrack(root.left, lower, val) and self.backtrack(root.right, val, upper):
            return True
        return False
