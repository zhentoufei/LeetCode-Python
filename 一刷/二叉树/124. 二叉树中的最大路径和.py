class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: TreeNode):
        self.ans = float('-inf')
        self.maxGain(root)
        return self.ans

    def maxGain(self, root: TreeNode):
        if not root:
            return 0

        left_gain = max(self.maxGain(root.left), 0)
        right_gain = max(self.maxGain(root.right), 0)
        tmp = root.val + left_gain + right_gain
        self.ans = max(self.ans, tmp)
        return root.val + max(left_gain, right_gain)
