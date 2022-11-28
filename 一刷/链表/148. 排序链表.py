class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def sortList(self, head: ListNode):
        return self.sortFun(head, None)

    def sortFun(self, head: ListNode, tail: ListNode):
        print("Head:{}, Tail:{}".format(head.val, None if tail is None else tail.val))
        if not head:
            return head

        if head.next == tail:
            head.next = None
            return head

        slow = head
        fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow

        return self.merge(self.sortFun(head, mid), self.sortFun(mid, tail))

    def merge(self, head1: ListNode, head2: ListNode):
        dummy = ListNode()
        current = dummy
        tmp1 = head1
        tmp2 = head2

        while tmp1 is not None and tmp2 is not None:
            if tmp1.val < tmp2.val:
                current.next = tmp1
                current = current.next
                tmp1 = tmp1.next
            else:
                current.next = tmp2
                current = current.next
                tmp2 = tmp2.next
        if tmp1 is not None:
            current.next = tmp1
        if tmp2 is not None:
            current.next = tmp2

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    cls = Solution()
    print(cls.sortList(l1))
