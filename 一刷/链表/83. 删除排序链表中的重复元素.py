class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self, head: ListNode):

        if not head:
            return None

        slow = head
        fast = head
        while fast:

            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next

            fast = fast.next
        slow.next = None # 注意这里最后如果fast一直相同，那么slow的next是有指向性的，因此这里有None的操作
        return head