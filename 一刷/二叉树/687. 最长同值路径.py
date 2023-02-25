class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root: TreeNode):
        self.dfs(root)
        return self.ans

    def dfs(self, node: TreeNode):
        if not node:
            return 0
        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        left_length_1 = 0
        if node.left and node.left.val == node.val:
            left_length_1 = left_length + 1
        right_length_1 = 0
        if node.right and node.right.val == node.val:
            right_length_1 = right_length + 1

        self.ans = max(self.ans, left_length_1 + right_length_1)
        return max(left_length_1, right_length_1)

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(4)
    t3 = TreeNode(5)
    t4 = TreeNode(4)
    t5 = TreeNode(4)
    t6 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    cls = Solution()
    print(cls.longestUnivaluePath(t1))
