class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def balanceBST(self, root: TreeNode):
        nums = []
        self.inorder(root, nums)
        return self.helper(0, len(nums) - 1, nums)

    def inorder(self, root: TreeNode, nums: list):
        if root is None:
            return None

        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

    def helper(self, left: int, right: int, nums: list):
        if left > right:
            return None

        mid = (right - left) // 2 + left
        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid - 1, right, nums)
        return root
