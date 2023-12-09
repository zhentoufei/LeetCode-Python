class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def insertIntoMaxTree(self, root: TreeNode, val: int):

        parent = None
        cur = root
        while cur:

            if cur.val < val:
                if parent is None:
                    return TreeNode(val, cur, None)
                cur_node = TreeNode(val, cur, None)
                parent.right = cur_node
                return root
            else:
                parent = cur
                cur = cur.right

        parent.right = TreeNode(val, None, None)
        return root
