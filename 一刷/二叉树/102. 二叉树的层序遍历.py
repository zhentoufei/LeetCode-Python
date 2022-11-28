class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode):
        if root is None:
            return []

        ans = []
        memo = []
        memo.append(root)
        while memo:
            size = len(memo)
            tmp = []
            for _ in range(size):
                current = memo.pop(0)
                tmp.append(current.val)
                if current.left:
                    memo.append(current.left)
                if current.right:
                    memo.append(current.right)
            ans.append(tmp)
        return ans