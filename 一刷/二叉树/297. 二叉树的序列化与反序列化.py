class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: list, inorder: list):
        index = {ele: i for i, ele in enumerate(inorder)}
        size = len(preorder)
        return self.helper(0, size - 1, 0, size - 1, index, preorder, inorder)

    def helper(self, pre_left: int, pre_right: int, in_left: int, in_right: int, index: dict, preorder: list,
               inorder: list):
        if pre_left > pre_right:
            return None

        pre_root = pre_left
        in_root = index[preorder[pre_root]]
        root = TreeNode(preorder[pre_root])
        size_left_subtree = in_root - in_left

        root.left = self.helper(pre_left + 1, pre_left + size_left_subtree, in_left, in_root - 1, index, preorder,
                                inorder)
        root.right = self.helper(pre_left + size_left_subtree + 1, pre_right, in_root + 1, in_right, index, preorder,
                                 inorder)
        return root
