class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode):
        return self.dfs(root, 0)

    def dfs(self, root: TreeNode, pre_total: int):
        if not root:
            return 0

        total = pre_total * 10 + root.val
        if not root.left and not root.right:
            return total
        else:
            return self.dfs(root.left, total) + self.dfs(root.right, total)

class Solution1:

    def sumNumbers(self, root: TreeNode):

        if not root:
            return 0

        ans = 0
        queue = []
        queue.append((root, root.val))

        while queue:
            node, num = queue.pop(0)
            if node.left is None and node.right is None:
                ans += num
            else:
                if node.left is not None:
                    queue.append((node.left, num * 10 + node.left.val))

                if node.right is not None:
                    queue.append((node.right, num * 10 + node.right.val))
        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    cls = Solution1()
    print(cls.sumNumbers(t1))




