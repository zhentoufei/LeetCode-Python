class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = []

    def postorderTraversal(self, root: TreeNode):
        self.postorder(root)
        return self.ans

    def postorder(self, root: TreeNode):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.ans.append(root.val)

    def postorderTraversal_1(self, root: TreeNode):
        if root is None:
            return []
        order = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            temp_node = stack.pop()
            order.append(temp_node.val)
            if temp_node.left is not None:
                stack.append(temp_node.left)
            if temp_node.right is not None:
                stack.append(temp_node.right)
        order.reverse()
        return order
