class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten(self, root: TreeNode):
        pre_list = []
        self.preorder(root, pre_list)
        for i in range(1, len(pre_list)):
            pre, cur = pre_list[i - 1], pre_list[i]
            pre.left = None
            pre.right = cur

    def preorder(self, root: TreeNode, pre_list: list):
        if root:
            pre_list.append(root)
            self.preorder(root.left, pre_list)
            self.preorder(root.right, pre_list)
