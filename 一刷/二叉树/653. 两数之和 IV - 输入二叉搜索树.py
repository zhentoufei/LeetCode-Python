class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.memo = set()

    def findTarget(self, root: TreeNode, k: int):
        if not root:
            return False

        if k - root.val in self.memo:
            return True
        self.memo.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
