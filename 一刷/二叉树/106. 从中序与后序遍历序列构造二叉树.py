class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: list, postorder: list):
        index = {ele: i for i, ele in enumerate(inorder)}
        size = len(inorder)
        return self.helper(0, size - 1, 0, size - 1, index, inorder, postorder)

    def helper(self, in_left: int, in_right: int, post_left: int, post_right: int, index: dict, inorder: list, postorder: list):
        if post_left > post_right:
            return None

        post_root = post_right
        in_root = index[postorder[post_root]]
        root = TreeNode(postorder[post_root])
        size_left_subtree = in_root - in_left
        root.left = self.helper(in_left, in_root - 1, post_left, post_left + size_left_subtree - 1, index, inorder, postorder)
        root.right = self.helper(in_root + 1, in_right, post_left + size_left_subtree, post_right - 1, index, inorder, postorder)
        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    cls = Solution()
    print(cls.buildTree(inorder, postorder))
