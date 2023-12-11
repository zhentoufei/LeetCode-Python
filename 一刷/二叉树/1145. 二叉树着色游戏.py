class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.lsz = 0
        self.rsz = 0

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int):

        def dfs(node: TreeNode):
            if node is None:
                return 0

            left_size = dfs(node.left)
            right_size = dfs(node.right)

            if node.val == x:
                self.lsz = left_size
                self.rsz = right_size

            return left_size + right_size + 1

        dfs(root)
        ans = max(self.lsz, self.rsz, n - 1 - self.lsz - self.rsz) * 2
        return ans > n

