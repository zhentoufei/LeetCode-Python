class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0
        self.ans = None

    def printTree(self, root: TreeNode):
        self.dfs_depth(root, 0)
        rows = self.max_depth + 1
        cols = 2 ** (self.max_depth + 1) - 1
        self.ans = [[''] * cols for _ in range(rows)]
        self.dfs_print(root, 0, int((cols - 1) / 2))
        return self.ans

    def dfs_depth(self, node: TreeNode, depth: int):
        if not node:
            return
        self.max_depth = max(self.max_depth, depth)
        if node.left:
            self.dfs_depth(node.left, depth + 1)

        if node.right:
            self.dfs_depth(node.right, depth + 1)

    def dfs_print(self, node: TreeNode, row, col):
        if not node:
            return
        print(f"row:{row}, col:{col}")
        self.ans[row][col] = str(node.val)
        if node.left:
            self.dfs_print(node.left, row + 1, col - 2 ** (self.max_depth - row - 1))
        if node.right:
            self.dfs_print(node.right, row + 1, col + 2 ** (self.max_depth - row - 1))


if __name__ == '__main__':
    cls = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t2.left = t3
    # cls.dfs_depth(t1, 0)
    print(cls.printTree(t1))
