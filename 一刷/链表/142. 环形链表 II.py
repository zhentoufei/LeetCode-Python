class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def detectCycle(self, head:ListNode):

        slow = head
        fast = head

        while True:
            if fast is None or fast.next is None:
                return

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast