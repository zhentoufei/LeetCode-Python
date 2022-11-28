class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        return self.backtrack(root.left, root.right)

    def backtrack(self, left: TreeNode, right: TreeNode):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return self.backtrack(left.left, right.right) and self.backtrack(left.right, right.left)
