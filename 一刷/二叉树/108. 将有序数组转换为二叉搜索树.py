class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    '''
    二叉搜索树的中序遍历是升序序列，题目给定的数组是按照升序排序的有序数组，因此可以确保数组是二叉搜索树的中序遍历序列
    '''
    def sortedArrayToBST(self, nums: list):
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, left: int, right:int, nums: list):
        if left > right:
            return None

        mid = (right - left)//2 + left
        root = TreeNode(nums[mid])
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)

        return root


