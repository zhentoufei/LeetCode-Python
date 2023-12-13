class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.total = 0
        self.ans = float('-inf')

    def maxProduct(self, root: TreeNode):
        mod = 10 ** 9 + 7

        def get_sum(node: TreeNode):
            if node is None:
                return
            self.total += node.val
            get_sum(node.left)
            get_sum(node.right)

        get_sum(root)

        def dfs(node: TreeNode):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            sub_sum = node.val + left + right
            self.ans = max(self.ans, sub_sum * (self.total - sub_sum))

            return sub_sum

        dfs(root)
        return self.ans % mod
