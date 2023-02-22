class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int):

        if not root:
            return TreeNode(val)
        pos = root
        while pos:
            if val < pos.val:
                if pos.left is not None:
                    pos = pos.left
                else:
                    pos.left = TreeNode(val)
                    break
            else:
                if pos.right is not None:
                    pos = pos.right
                else:
                    pos.right = TreeNode(val)
                    break
        return root
