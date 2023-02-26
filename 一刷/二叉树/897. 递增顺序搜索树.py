class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.res = []

    def increasingBST(self, root: TreeNode):
        self.dfs(root)
        dummy = TreeNode(-1)
        head = dummy
        for val in self.res:
            head.right = TreeNode(val)
            head = head.right
        return dummy.right

    def dfs(self, node: TreeNode):
        if not node:
            return

        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)
