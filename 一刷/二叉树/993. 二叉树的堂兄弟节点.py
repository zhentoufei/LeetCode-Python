class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCousins(self, root: TreeNode, x:int, y:int):
        x_parent, x_depth, x_found = None, None, False
        y_parent, y_depth, y_found = None, None, False

        def dfs(node: TreeNode, depth: int, parent: TreeNode):
            if not node:
                return

            nonlocal x_parent, x_depth, x_found
            nonlocal y_parent, y_depth, y_found
            if node.val == x:
                x_parent = parent
                x_depth = depth
                x_found = True
            elif node.val == y:
                y_parent = parent
                y_depth = depth
                y_found = True

            if x_found and y_found:
                return

            dfs(node.left, depth + 1, node)

            if x_found and y_found:
                return

            dfs(node.right, depth + 1, node)
        dfs(root, 0, None)
        return x_depth == y_depth and x_parent != y_parent
