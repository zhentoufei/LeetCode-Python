class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def preorder(self, root: Node):
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, node: Node):
        if node is None:
            return
        self.ans.append(node.val)
        for ch in node.children:
            self.dfs(ch)

    def preorder_traverse(self, root: Node):
        if not root:
            return []

        ans = []
        memo = [root]
        while memo:
            current = memo.pop()
            ans.append(current.val)
            memo.extend(reversed(current.children))
        return ans
