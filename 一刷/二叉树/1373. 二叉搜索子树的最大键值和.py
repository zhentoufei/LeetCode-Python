class SubTree:
    def __init__(self, is_bst, min_value, max_value, sum_value):
        self.is_bst = is_bst
        self.min_value = min_value
        self.max_value = max_value
        self.sum_value = sum_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    INF = 0x3f3f3f3f

    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            return SubTree(True, self.INF, -self.INF, 0)

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left.is_bst and right.is_bst and root.val > left.max_value and root.val < right.min_value:
            sum = root.val + left.sum_value + right.sum_value
            self.res = max(self.res, sum)
            return SubTree(True, min(left.min_value, root.val), max(root.val, right.max_value), sum)
        else:
            return SubTree(False, 0, 0, 0)
