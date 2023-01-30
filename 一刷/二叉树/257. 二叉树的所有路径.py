class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        self.paths = []
        self.getPaths(root, '')
        return self.paths


    def getPaths(self, root: TreeNode, path: str):
        if root:
            path += str(root.val)
            if not root.left and not root.right:
                self.paths.append(path)
            else:
                path += '->'
                self.getPaths(root.left, path)
                self.getPaths(root.right, path)



