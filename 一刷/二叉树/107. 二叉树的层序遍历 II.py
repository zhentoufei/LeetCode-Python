class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrderBottom(self, root: TreeNode):

        if not root:
            return []
        queue = []
        queue.append(root)
        ans = []
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                current = queue.pop(0)
                tmp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(tmp)
        return ans[::-1]
if __name__ == '__main__':
    r1 = TreeNode(1)
    r2 = TreeNode(2)
    r3 = TreeNode(3)
    r4 = TreeNode(4)
    r1.left = r2
    r1.right = r3
    r2.left = r4
    cls = Solution()
    print(cls.levelOrderBottom(r1))
