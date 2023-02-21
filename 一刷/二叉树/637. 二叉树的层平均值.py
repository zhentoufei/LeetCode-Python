class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def averageOfLevels(self, root: TreeNode):

        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                current = queue.pop(0)
                total += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            ans.append(total/size)


        return ans


