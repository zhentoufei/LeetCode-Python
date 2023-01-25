class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isBalanced(self, root: TreeNode):
        return self.height(root) >= 0

    def height(self, root: TreeNode):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if left_height == -1 or right_height == -1 or abs(right_height - left_height) > 1:
            return -1
        else:
            return max(left_height, right_height) + 1
