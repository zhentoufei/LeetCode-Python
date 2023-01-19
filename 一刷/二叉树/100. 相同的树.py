class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 深度优先
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # 广度优先
    def isSameTree_v1(self, p: TreeNode, q: TreeNode):
        if not p and not q:
            return True
        if not p or not q:
            return False

        que1 = []
        que2 = []
        que1.append(p)
        que2.append(q)
        while que1 and que2:
            node1 = que1.pop(0)
            node2 = que2.pop(0)
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (left1 is not None and left2 is None) or (left1 is None and left2 is not None):
                return False
            if (right1 is not None and right2 is None) or (right1 is None and right2 is not None):
                return False

            if left1:
                que1.append(left1)

            if right1:
                que1.append(right1)

            if left2:
                que2.append(left2)

            if right2:
                que2.append(right2)

        if not que1 and not que2:
            return True
