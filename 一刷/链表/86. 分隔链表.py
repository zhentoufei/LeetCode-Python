class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def partition(self, head: ListNode, x: int):

        small = ListNode()
        large = ListNode()

        small_head = small
        large_head = large

        while head is not None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        small.next = large_head.next
        large.next = None  # 注意最后的next要赋值为空
        return small_head.next