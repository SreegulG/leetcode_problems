# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        mid = self.ll_mid(head)
        mid = self.reverse_ll(mid.next)

        while mid and head:
            if mid.val != head.val:
                return False
            mid = mid.next
            head = head.next
        
        return True
    
    def ll_mid(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

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