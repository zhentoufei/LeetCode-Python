class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    # BFS
    def serialize(self, root: TreeNode):

        if not root:
            return ''

        queue = []
        ans = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            if current:
                ans.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                ans.append('None')
        return '[' + ','.join(ans) + ']'

    def deserialize(self, data: str):
        if not data:
            return []
        data = data[1:-1].split(',')
        root = TreeNode(int(data[0]))
        queue = []
        queue.append(root)
        index = 1
        while queue:
            current = queue.pop(0)
            if data[index] != 'None':
                current.left = TreeNode(int(data[index]))
                queue.append(current.left)
            index += 1

            if data[index] != 'None':
                current.right = TreeNode(int(data[index]))
                queue.append(current.right)
            index += 1
        return root


class Solution2:

    def serialize(self, root: TreeNode):
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data: str):
        return self.helper(data[1:-1].split(','))

    def helper(self, data: list):
        current = data.pop(0)
        if current == 'None':
            return None
        node = TreeNode(int(current))
        node.left = self.helper(data)
        node.right = self.helper(data)
        return node
