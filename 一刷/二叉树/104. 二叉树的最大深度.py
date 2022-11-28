class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0

        ans = 0
        memo = []
        memo.append(root)
        while memo:
            ans += 1
            size = len(memo)
            for _ in range(size):
                tmp = memo.pop(0)  # 注意这里要把最前面的数据pop出去
                if tmp.left:
                    memo.append(tmp.left)
                if tmp.right:
                    memo.append(tmp.right)
        return ans