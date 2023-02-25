import collections


class BSTIterator(object):

    def __init__(self, root):
        self.queue = collections.deque()
        self.inOrder(root)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.queue.append(root.val)
        self.inOrder(root.right)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue) > 0
