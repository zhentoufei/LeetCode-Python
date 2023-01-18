class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recoverTree(self, root: TreeNode):
        nums = []
        self.inorder(root, nums)
        print(nums)
        swapped = self.findTwoSwapped(nums)
        print(swapped)
        self.recover(root, 2, swapped[0], swapped[1])

    def inorder(self, root: TreeNode, nums: list):

        if not root:
            return

        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

    def findTwoSwapped(self, nums):
        size = len(nums)
        index1 = -1
        index2 = -1
        for i in range(0, size - 1):
            if nums[i + 1] < nums[i]:
                index2 = i + 1
                if index1 == -1:
                    index1 = i
                else:
                    break
        return [nums[index1], nums[index2]]

    def recover(self, root: TreeNode, count: int, left: int, right: int):
        if root is not None:
            if root.val == left or root.val == right:
                if root.val == left:
                    root.val = right
                else:
                    root.val = left
                count -= 1
                if count == 0:
                    return

            self.recover(root.right, count, left, right)
            self.recover(root.left, count, left, right)

if __name__ == '__main__':
    root = TreeNode(1)
    t1 = TreeNode(3)
    t2 = TreeNode(2)
    root.left = t1
    t1.right = t2
    cls = Solution()
    cls.recoverTree(root)
    print(root.val)