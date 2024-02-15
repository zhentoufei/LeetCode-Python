class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def set_children(self, left=None, right=None):
        self.left = left
        self.right = right


class Tree(object):
    def __init__(self, tree_node: TreeNode = None):
        self.root = tree_node
        self.ans = []

    def pre_order(self, root: TreeNode):
        if root is None:
            return
        stack = []
        res = []
        node = root
        while node is not None or stack is not None:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def pre_order_rec(self, root: TreeNode):
        if root is None:
            return

        self.ans.append(root.val)
        self.pre_order_rec(root.left)
        self.pre_order_rec(root.right)
        return self.ans

    def mid_order(self, root: TreeNode):
        if root is None:
            return

        stack = []
        ans = []
        node = root
        while node is not None or stack is not None:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans

    def mid_order_rec(self, root: TreeNode):
        if root is None:
            return

        self.mid_order_rec(root.left)
        self.ans.append(root.val)
        self.mid_order_rec(root.right)
        return self.ans

    def post_order(self, root: TreeNode):
        if root is None:
            return

        stack = []
        ans = []
        node = root
        while node is not None or stack is not None:
            while node is not None:
                ans.insert(0, node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return ans

    def post_order_rec(self, root: TreeNode):
        if root is None:
            return

        self.post_order_rec(root.left)
        self.post_order_rec(root.right)
        self.ans.append(root.val)
        return self.ans
