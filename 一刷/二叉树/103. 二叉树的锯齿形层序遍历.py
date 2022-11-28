class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        ans = []
        memo = []
        memo.append(root)
        flag = 'left'
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
            if flag == 'left':
                ans.append(tmp[:])
                flag = 'right'
            else:
                ans.append(tmp[::-1])
                flag = 'left'
        return ans
