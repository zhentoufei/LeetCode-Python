class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findFrequentTreeSum(self, root: TreeNode):
        self.counter = {}
        self.dfs(root)
        max_count = max(self.counter.values())
        return [key for key, value in self.counter.items() if value == max_count]

    def dfs(self, root: TreeNode):
        if not root:
            return 0

        sum = root.val + self.dfs(root.left) + self.dfs(root.right)
        if sum not in self.counter:
            self.counter[sum] = 0
        self.counter[sum] += 1
        return sum
