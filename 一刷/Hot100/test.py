class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        ans = ListNode()
        current = ans
        carry = 0

        while l1 is not None or l2 is not None:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            agg = val1 + val2 + carry
            current.next = ListNode(agg % 10)
            current = current.next
            carry = agg // 10

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)
            current = current.next
        return ans.next
if __name__ == '__main__':
    l11 = ListNode(2)
    l12 = ListNode(2)
    l13 = ListNode(2)
