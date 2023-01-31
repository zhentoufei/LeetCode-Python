class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sumOfLeftLeaves(self, root: TreeNode):
        return self.dfs(root)

    def isLeaf(self, root: TreeNode):
        if not root.left and not root.right:
            return True
        else:
            return False

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        ans = 0
        if root.left:
            if not self.isLeaf(root.left):
                ans += self.dfs(root.left)
            else:
                ans += root.left.val
        if root.right and not self.isLeaf(root.right):
            ans += self.dfs(root.right)
        return ans

class Solution1:

    def sumOfLeftLeaves(self, root: TreeNode):
        if not root:
            return 0
        ans = 0
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    ans += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                if node.right.left is not None or node.right.right is not None:
                    queue.append(node.right)
        return ans



if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    cls = Solution()
    print(cls.sumOfLeftLeaves(t1))