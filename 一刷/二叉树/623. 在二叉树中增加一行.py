class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int):

        if not root:
            return

        if depth == 1:
            return TreeNode(val, root, None)

        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)

        return root

    def addOneRow1(self, root: TreeNode, val: int, depth: int):

        if depth == 1:
            return TreeNode(val, root, None)

        queue = [root]
        for _ in range(1, depth - 1):
            tmp = []
            for ele in queue:
                if ele.left:
                    tmp.append(ele.left)
                if ele.right:
                    tmp.append(ele.right)
            queue = tmp

        for ele in queue:
            ele.left = TreeNode(val, ele.left, None)
            ele.right = TreeNode(val, None, ele.right)

        return root




