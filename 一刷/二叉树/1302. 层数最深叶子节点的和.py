class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deepestLeavesSum(self, root: TreeNode):

        memo = [root]
        while memo:
            size = len(memo)
            ans = 0

            for _ in range(size):
                current = memo.pop(0)
                ans += current.val
                if current.left:
                    memo.append(current.left)

                if current.right:
                    memo.append(current.right)
        return ans
