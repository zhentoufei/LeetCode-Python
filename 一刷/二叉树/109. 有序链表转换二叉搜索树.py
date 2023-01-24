class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: ListNode):
        self.head = head
        length = self.getLength(head)
        return self.helper(0, length - 1)

    def getLength(self, head: ListNode):
        ans = 0
        while head:
            ans += 1
            head = head.next
        return ans

    def helper(self, left: int, right: int):
        if left > right:
            return None

        mid = (right - left) // 2 + left
        root = TreeNode()
        root.left = self.helper(left, mid - 1)
        root.val = self.head.val
        self.head = self.head.next
        root.right = self.helper(mid + 1, right)
        return root
