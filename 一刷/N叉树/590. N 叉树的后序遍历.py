class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def postorder(self, root:Node):
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, node: Node):
        if node is None:
            return
        for ch in node.children:
            self.dfs(ch)
        self.ans.append(node.val)

    def postorder_traverse(self, root:Node):
        if not root:
            return []
        ans = []
        memo = [root]
        visited = set()
        while memo:
            current = memo[-1]
            # 如果当前节点为叶子节点或者当前节点的子节点已经遍历过
            if len(current.children) == 0 or current in visited:
                ans.append(current.val)
                memo.pop()
                continue
            memo.extend(reversed(current.children))
            visited.add(current)
        return ans

