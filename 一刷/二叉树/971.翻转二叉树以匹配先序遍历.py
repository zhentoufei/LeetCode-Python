"""
https://leetcode.cn/problems/flip-binary-tree-to-match-preorder-traversal/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.flipped = None
        self.i = None

    def flipMatchVoyage(self, root: TreeNode, voyage: list):
        self.flipped = []
        self.i = 0

        def dfs(node: TreeNode):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1
                # 相等
                if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
