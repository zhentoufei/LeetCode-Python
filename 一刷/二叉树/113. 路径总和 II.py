import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = []
        self.tmp = []

    def pathSum(self, root: TreeNode, targetSum: int):
        self.helper(root, targetSum)
        return self.ans

    def helper(self, root: TreeNode, targetSum: int):
        if root is None:
            return

        self.tmp.append(root.val)

        if root.left is None and root.right is None and targetSum == root.val:
            self.ans.append(self.tmp[:])

        self.helper(root.left, targetSum - root.val)
        self.helper(root.right, targetSum - root.val)
        self.tmp.pop()


class Solution1:

    def getPath(self, node: TreeNode, parent: dict):
        tmp = []
        while node:
            tmp.append(node.val)
            node = parent[node]
        return tmp[::-1]

    def pathSum(self, root: TreeNode, targetSum: int):
        ans = []
        parent = collections.defaultdict()

        if root is None:
            return ans

        que_node = []
        que_node.append((root, root.val))
        while que_node:
            node, total = que_node.pop(0)

            if node.left is None and node.right is None and targetSum == total:
                ans.append(self.getPath(node, parent))
            else:
                if node.left:
                    parent[node.left] = node
                    que_node.append((root.left, total + root.left.val))

                if node.right:
                    parent[node.right] = node
                    que_node.append((root.right, total + root.right.val))
        return ans




