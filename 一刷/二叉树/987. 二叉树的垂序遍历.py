class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        nodes = []

        def dfs(node: TreeNode, row: int, col: int) -> None:
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        print(nodes)
        nodes.sort()
        ans = []
        last_col = float('-inf')
        for col, row, value in nodes:
            if col != last_col:
                last_col = col
                ans.append([])
            ans[-1].append(value)
        return ans


if __name__ == '__main__':
    a = TreeNode(3)
    b = TreeNode(4)
    c = TreeNode(20)
    a.left = b
    a.right = c
    s = Solution()
    print(s.verticalTraversal(a))
