class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def delNodes(self, root: TreeNode, to_delete: list):
        to_delete = set(to_delete)
        ans = []
        self.dfs(root, True, to_delete, ans)
        return ans

    def dfs(self, node: TreeNode, is_root: bool, to_delete: set, ans: list):
        if node is None:
            return None

        is_delete = True if node.val in to_delete else False
        node.left = self.dfs(node.left, is_delete, to_delete, ans)
        node.right = self.dfs(node.right, is_delete, to_delete, ans)
        if is_delete:
            return None
        else:
            if is_root:
                ans.append(node)
            return node
