class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:

    def connect(self, root: TreeNode):

        if root is None:
            return root

        queue = []
        queue.append(root)
        while queue:
            size = len(queue)

            for i in range(size):
                current = queue.pop(0)
                if i <= size - 2:
                    current.next = queue[0]

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
        return root
