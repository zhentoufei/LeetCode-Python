class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root:TreeNode):
        if not root:
            return []
        self.ans = []
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node: TreeNode, height: int):
        if not node:
            return
        if height == len(self.ans):
            self.ans.append(node.val)
        else:
            self.ans[height] = max(node.val, self.ans[height])
        self.dfs(node.left, height + 1)
        self.dfs(node.right, height + 1)

if __name__ == '__main__':

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    cls = Solution()
    print(cls.largestValues(t1))


