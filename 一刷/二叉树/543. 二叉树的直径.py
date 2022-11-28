class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode):
        self.backtrack(root)
        return self.max_diameter - 1

    def backtrack(self, root: TreeNode):
        if root is None:
            return 0

        left_max = self.backtrack(root.left)
        right_max = self.backtrack(root.right)
        self.max_diameter = max(self.max_diameter, left_max + right_max + 1)
        return max(left_max, right_max) + 1

