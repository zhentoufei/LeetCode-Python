class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.move = 0

    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(_root: TreeNode):
            move_left = 0
            move_right = 0
            if _root is None:
                return 0
            if _root.left is not None:
                move_left = dfs(_root.left)
            if _root.right is not None:
                move_right = dfs(_root.right)

            self.move += abs(move_right) + abs(move_left)
            return move_left + move_right + _root.val - 1

        dfs(root)
        return self.move
