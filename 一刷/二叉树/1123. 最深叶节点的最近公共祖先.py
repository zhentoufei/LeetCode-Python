class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lcaDeepestLeaves(self, root: TreeNode):
        def dfs(node: TreeNode):
            if node is None:
                return 0, None
            left_h, lca_left = dfs(node.left)
            right_h, lca_right = dfs(node.right)
            if left_h > right_h:
                return left_h + 1, lca_left
            if left_h < right_h:
                return right_h + 1, lca_right
            return left_h + 1, node

        return dfs(root)[1]
