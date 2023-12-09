class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def maxAncestorDiff(self, root: TreeNode):
        def dfs(node: TreeNode, lower: int, upper: int):
            if node is None:
                return

            lower = min(node.val, lower)
            upper = max(node.val, upper)
            self.ans = max(upper - node.val, self.ans)
            self.ans = max(node.val - lower, self.ans)
            dfs(node.left, lower, upper)
            dfs(node.right, lower, upper)

        dfs(root, root.val, root.val)
        return self.ans
