# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head
        cnt = 1
        while cnt < left:
            prev = curr
            curr = curr.next
            cnt += 1

        curr = head
        cnt = 1
        while cnt < right:
            curr = curr.next
            cnt += 1

        nxt = curr.next
        curr.next = None

        reverse_node, tail = self.reverse_ll(prev.next)

        prev.next = reverse_node
        tail.next = nxt
        return dummy.next

    def reverse_ll(self, head):
        prev = None
        curr = tail = head
        while curr:
            rem = curr.next
            curr.next = prev
            prev = curr
            curr = rem
        return prev, tail
