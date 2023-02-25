class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.memo = {}

    def subtreeWithAllDeepest(self, root: TreeNode):
        if not root:
            return root

        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)
        if left_max_depth == right_max_depth:
            return root

        if left_max_depth > right_max_depth:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)

    def max_depth(self, node: TreeNode):
        if node in self.memo.keys():
            return self.memo[node]
        if not node:
            return 0
        depth = max(self.max_depth(node.left), self.max_depth(node.right)) + 1
        self.memo[node] = depth
        return depth
