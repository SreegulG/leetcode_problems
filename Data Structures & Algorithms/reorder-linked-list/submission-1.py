# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return
        mid = self.find_middle(head)
        mid = self.reverse_ll(mid)
        first = head
        while mid.next:
            rem1 = first.next
            rem2 = mid.next

            first.next = mid
            mid.next = rem1

            first = rem1
            mid = rem2

    def find_middle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_ll(self, head):
        prev = None
        curr = head

        while curr:
            rem = curr.next
            curr.next = prev
            prev = curr
            curr = rem
        return prev
