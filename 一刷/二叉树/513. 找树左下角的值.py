class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findBottomLeftValue(self, root: TreeNode):
        if not root:
            return None
        queue = [root]
        ans = root.val
        while queue:
            current = queue.pop(0)
            if current.right:
                queue.append(current.right)

            if current.left:
                queue.append(current.left)
            ans =  current.val
        return ans

    def findBottomLeftValue1(self, root: TreeNode):
        if not root:
            return None

        queue = []
        queue.append([root])
        ans = root.val
        while queue:
            current = queue.pop(0)
            size = len(current)
            tmp_list = []
            for _ in range(size):
                node = current.pop(0)
                if node.left:
                    tmp_list.append(node.left)
                if node.right:
                    tmp_list.append(node.right)
            if tmp_list:
                ans = tmp_list[0].val
                queue.append(tmp_list)
        return ans
