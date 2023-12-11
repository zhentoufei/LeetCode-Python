class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sufficientSubset(self, root: TreeNode, limit: int):

        def checkSufficientLeaf(node: TreeNode, sum: int, limit: int):
            if node is None:
                return False

            if node.left is None and node.right is None:
                return sum + node.val >= limit

            haveSufficientLeft = checkSufficientLeaf(node.left, sum + node.val, limit)
            haveSufficientRight = checkSufficientLeaf(node.right, sum + node.val, limit)
            if not haveSufficientLeft:
                node.left = None

            if not haveSufficientRight:
                node.right = None

            return haveSufficientRight or haveSufficientLeft

        haveSufficient = checkSufficientLeaf(root, 0, limit)
        return root if haveSufficient else None
