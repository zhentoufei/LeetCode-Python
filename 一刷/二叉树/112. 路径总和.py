class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int):
        if root is None:
            return False
        else:
            if root.left is None and root.right is None:
                return targetSum == root.val

            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSumv1(self, root: TreeNode, targetSum: int):

        if root is None:
            return False

        que = []
        que.append((root, root.val))
        while que:
            node, path = que.pop(0)
            if node.left is None and node.right is None and path == targetSum:
                return True
            if node.left is not None:
                que.append((node.left, path + node.left.val))
            if node.right is not None:
                que.append((node.right, path + node.right.val))
        return False

