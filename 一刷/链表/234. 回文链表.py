class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: ListNode):
        if not head:
            return True

        first_half_end = self.endOfFirstHalf(head)
        second_half_start = self.reverseList(first_half_end.next)
        ans = True
        first_pos = head
        second_pos = second_half_start
        while ans and second_pos is not None:

            if first_pos.val != second_pos.val:
                ans = False

            first_pos = first_pos.next
            second_pos = second_pos.next
        return ans


    def endOfFirstHalf(self, head: ListNode):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head: ListNode):

        prev = None
        current = head
        while current is not None:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev