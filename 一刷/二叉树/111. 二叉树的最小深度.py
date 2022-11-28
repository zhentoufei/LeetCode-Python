class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minDepth(self, root:TreeNode):

        if root is None:
            return 0

        memo = []
        memo.append(root)
        self.depth = 1

        while memo:

            size = len(memo)
            for _ in range(size):
                current = memo.pop(0)
                if current.left is None and current.right is None:
                    return self.depth

                if current.left:
                    memo.append(current.left)

                if current.right:
                    memo.append(current.right)
            self.depth += 1