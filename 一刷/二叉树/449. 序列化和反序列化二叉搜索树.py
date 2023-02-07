class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def serialize(self, root: TreeNode):
        if not root:
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data: str):
        self.arr = list(data.split(','))
        return self.deser_helper(float('-inf'), float('inf'))

    def deser_helper(self, lower, upper):

        if len(self.arr) == 0 or self.arr[0] == 'None':
            self.arr.pop(0)
            return None
        if int(self.arr[0]) < lower or int(self.arr[0]) > upper:
            return None

        val = int(self.arr.pop(0))
        node = TreeNode(val)
        node.left = self.deser_helper(lower, val)
        node.right = self.deser_helper(val, upper)
        return node

if __name__ == '__main__':
    info = '2,1,None,None,3,None,None'
    cls = Solution()
    root = cls.deserialize(info)
    print(cls.serialize(root))