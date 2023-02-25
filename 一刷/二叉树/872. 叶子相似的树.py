class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.seq1 = []
        self.seq2 = []

    def leafSimilar(self, root1: TreeNode, root2: TreeNode):
        self.dfs(root1, self.seq1)
        self.dfs(root2, self.seq2)
        return self.seq1 == self.seq2

    def dfs(self, node: TreeNode, seq: list):
        if not node:
            return

        if not node.left and not node.right:
            seq.append(node.val)

        if node.left:
            self.dfs(node.left, seq)

        if node.right:
            self.dfs(node.right, seq)


if __name__ == '__main__':
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)
