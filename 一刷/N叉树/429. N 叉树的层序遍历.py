class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def levelOrder(self, root: Node):
        if not root:
            return []

        ans = []
        memo = [root]
        while memo:
            size = len(memo)
            tmp = []
            for _ in range(size):
                current = memo.pop(0)
                tmp.append(current.val)
                for ch in current.children:
                    memo.append(ch)
            ans.append(tmp)
        return ans

    def level_order_rec(self, root: Node):
        self.ans = []
        if not root:
            return []

        self.bfs(root, 0)
        return self.ans

    def bfs(self, node: Node, level: int):
        if len(self.ans) == level:
            self.ans.append([])

        self.ans[level].append(node.val)
        for ch in node.children:
            self.bfs(ch, level + 1)
