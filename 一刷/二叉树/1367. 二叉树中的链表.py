class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def dfs(self, head:ListNode, root:TreeNode):
        if head is None:
            return True

        if root is None:
            return False

        if head.val != root.val:
            return False

        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

    def isSubPath(self, head:ListNode, root:TreeNode):
        if root is None:
            return False

        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
