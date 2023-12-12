class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        self.elems = set()

        def dfs(node, val):
            if node:
                node.val = val
                self.elems.add(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.elems
