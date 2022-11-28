class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rob(self, root: TreeNode):
        memo = {}
        return self.robHelper(memo, root)

    def robHelper(self, memo: dict, root: TreeNode):

        if root is None:
            return 0

        if root in memo.keys():
            return memo[root]

        money = root.val
        if root.left:
            money += self.robHelper(memo, root.left.left)
            money += self.robHelper(memo, root.left.right)

        if root.right:
            money += self.robHelper(memo, root.right.left)
            money += self.robHelper(memo, root.right.right)
        tmp = max(money, self.robHelper(memo, root.left) + self.robHelper(memo, root.right))
        memo[root] = tmp
        return tmp
