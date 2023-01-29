class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        right_most = {}
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            root, depth = stack.pop()

            if root is not None:
                max_depth = max(depth, max_depth)

                right_most.setdefault(max_depth, root.val)
                stack.append((root.left, depth + 1))
                stack.append((root.right, depth + 1))
        return [right_most[depth] for depth in range(max_depth + 1)]

    def rightSideView_1(self, root: TreeNode):

        if not root:
            return []

        max_depth = -1
        right_most = {}
        queue = []
        queue.append((root, 0))
        while queue:
            node, depth = queue.pop(0)
            if node is not None:
                max_depth = max(max_depth, depth)
                right_most[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [right_most[depth] for depth in range(max_depth + 1)]
