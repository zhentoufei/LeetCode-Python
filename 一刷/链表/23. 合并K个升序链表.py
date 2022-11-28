class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKList(self, lists: list):
        return self.merge(lists, 0, len(lists) - 1)

    def merge2List(self, l1: ListNode, l2: ListNode):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next

        current.next = l1 if l1 else l2
        return dummy.next

    def merge(self, lists: list, left: int, right: int):
        if left == right:
            return lists[left]

        if left > right:
            return None

        mid = left + (right - left) // 2
        return self.merge2List(self.merge(lists, left, mid), self.merge(lists, mid + 1, right))
