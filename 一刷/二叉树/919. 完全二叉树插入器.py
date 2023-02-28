class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candidate = []

        queue = [root]
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if not (node.left and node.right):
                self.candidate.append(node)

    def insert(self, val: int):
        candidate_ = self.candidate
        parent = candidate_[0]
        child = TreeNode(val)
        if not parent.left:
            parent.left = child
        else:
            parent.right = child
            candidate_.pop(0)
        candidate_.append(child)
        return parent.val

    def get_root(self):
        return self.root