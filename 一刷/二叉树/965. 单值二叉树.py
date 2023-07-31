class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isUnivalTree(self, root: TreeNode):
        return self.dfs(root, root.val)

    def dfs(self, node: TreeNode, val: int):
        if not node:
            return True
        if node.val != val:
            return False

        return self.dfs(node.left, node.val) and self.dfs(node.right, node.val)

if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(1)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t7 = TreeNode(1)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t7

    cls = Solution()
    print(cls.isUnivalTree(t1))
