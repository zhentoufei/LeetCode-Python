class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def widthOfBinaryTree(self, root: TreeNode):

        if not root:
            return 0

        res = 0
        queue = [(root, 1)]
        while queue:
            tmp = []
            for current, index in queue:
                if current.left:
                    tmp.append((current.left, index * 2))
                if current.right:
                    tmp.append((current.right, index * 2 + 1))
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            queue = tmp
        return res

    def widthOfBinaryTree_v1(self, root: TreeNode):
        level_depth = {}
        return self.dfs(root, 1, 1, level_depth)

    def dfs(self, node: TreeNode, depth: int, index: int, level_depth: dict):
        if not node:
            return 0
        if depth not in level_depth.keys():
            level_depth[depth] = index
        current_width = index - level_depth[depth] + 1
        left_width = self.dfs(node.left, depth + 1, index * 2, level_depth)
        right_width = self.dfs(node.right, depth + 1, index * 2 + 1, level_depth)
        return max(current_width, left_width, right_width)
