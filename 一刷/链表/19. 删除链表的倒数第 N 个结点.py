class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0, head)
        fast = head
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
