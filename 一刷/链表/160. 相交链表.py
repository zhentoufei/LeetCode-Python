class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        
        p1 = headA
        p2 = headB

        while p1 != p2:

            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1
