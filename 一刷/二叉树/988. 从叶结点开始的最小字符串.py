class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def smallestFromLeaf(self, node: TreeNode):
        self.ans = '~'

        def dfs(node: TreeNode, a: list):
            if node:
                a.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, ''.join(reversed(a)))

            dfs(node.left, a)
            dfs(node.right, a)
            a.pop()

        dfs(node, [])
        return self.ans
