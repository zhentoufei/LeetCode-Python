class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def hasCycle(self, head: ListNode):

        if head is None or head.next is None:
            return False

        slow = head
        fast = head
        while True:

            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        return True