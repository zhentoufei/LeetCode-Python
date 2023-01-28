class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = []

    def preorderTraversal(self, root: TreeNode):
        self.preorder(root)
        return self.ans

    def preorder(self, root: TreeNode):
        if not root:
            return

        self.ans.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def preorderTraversal_1(self, root: TreeNode):

        if root is None:
            return []
        order = []
        stack = [root]
        while len(stack) != 0:
            temp_node = stack.pop()
            order.append(temp_node.val)
            if temp_node.right is not None:
                stack.append(temp_node.right)
            if temp_node.left is not None:
                stack.append(temp_node.left)
        return order
