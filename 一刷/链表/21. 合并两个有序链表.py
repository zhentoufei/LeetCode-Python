class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        dummy = ListNode()
        current = dummy

        while list1 is not None and list2 is not None:

            val1 = list1.val
            val2 = list2.val

            if val1 < val2:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 is not None:
            current.next = list1

        if list2 is not None:
            current.next = list2

        return dummy.next
