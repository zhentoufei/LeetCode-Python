class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.idx = 0
        self.repeat = set()
        self.seen = {}
    def findDuplicateSubtrees(self, root:TreeNode):
        self.dfs(root)
        return list(self.repeat)

    def dfs(self, root:TreeNode):

        if not root:
            return 0

        tri = (root.val, self.dfs(root.left), self.dfs(root.right))

        if tri in self.seen.keys():
            (tree, idx) = self.seen[tri]
            self.repeat.add(tree)
            return idx
        else:
            self.idx += 1
            self.seen[tri] = (root, self.idx)
            return self.idx


