class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode):
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: list):
        if root is None:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

class Solution1:

    def inorderTraversal(self, root: TreeNode):
        ans = []
        stack = []
        tmp_node = root
        while tmp_node is not None or len(stack) != 0:
            if tmp_node is not None:
                stack.append(tmp_node)
                tmp_node = tmp_node.left
            else:
                tmp_node = stack.pop()
                ans.append(tmp_node.val)
                tmp_node = tmp_node.right
        return ans
