class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        self.parent = {}
        self.dfs(root)
        visited = set()

        while p:
            visited.add(p.val)
            p = self.parent.get(p.val)

        while q:
            if q.val in visited:
                return q
            q = self.parent.get(q.val)

        return None

    def dfs(self, root: TreeNode):

        if root.left:
            self.parent[root.left.val] = root
            self.dfs(root.left)

        if root.right:
            self.parent[root.right.val] = root
            self.dfs(root.right)
