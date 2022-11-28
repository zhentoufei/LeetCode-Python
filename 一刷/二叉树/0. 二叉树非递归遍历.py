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
    def __init__(self, tree_node=None):
        self.root = tree_node

    def pre_order(self):
        if self.root is None:
            return []
        order = []
        stack = [self.root]
        while len(stack) != 0:
            temp_node = stack.pop()
            order.append(temp_node.val)
            if temp_node.right is not None:
                stack.append(temp_node.right)
            if temp_node.left is not None:
                stack.append(temp_node.left)
        return order

    def middle_order(self):
        order = []
        stack = []
        temp_node = self.root
        while temp_node is not None or len(stack) != 0:
            if temp_node is not None:
                stack.append(temp_node)
                temp_node = temp_node.left
            else:
                temp_node = stack.pop()
                order.append(temp_node.val)
                temp_node = temp_node.right
        return order

    def after_order(self):
        if self.root is None:
            return []
        order = []
        stack = []
        stack.append(self.root)
        while len(stack) != 0:
            temp_node = stack.pop()
            order.append(temp_node.val)
            if temp_node.left is not None:
                stack.append(temp_node.left)
            if temp_node.right is not None:
                stack.append(temp_node.right)
        order.reverse()
        return order

    def sequence_order(self):
        if self.root is None:
            return []
        order = []
        stack = []
        stack.append(self.root)
        while len(stack) != 0:
            temp_node = stack.pop(0)
            order.append(temp_node.val)
            if temp_node.left is not None:
                stack.append(temp_node.left)
            if temp_node.right is not None:
                stack.append(temp_node.right)
        return order
