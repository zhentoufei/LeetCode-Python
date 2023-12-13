class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def sumEvenGrandparent(self, root: TreeNode):

        def dfs(grandparent: TreeNode, parent: TreeNode, node: TreeNode):
            if node is None:
                return

            if grandparent.val % 2 == 0:
                self.ans += node.val

            dfs(parent, node, node.left)
            dfs(parent, node, node.right)

        if root.left:
            dfs(root, root.left, root.left.left)
            dfs(root, root.left, root.left.right)

        if root.right:
            dfs(root, root.right, root.right.left)
            dfs(root, root.right, root.right.right)

        return self.ans
