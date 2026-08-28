# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(None)
        new_head = dummy
        temp = head

        while temp:
            new_node = ListNode(temp.val)
            dummy.next = new_node
            dummy = dummy.next
            temp = temp.next

        
        new_head = self.reverse_ll(new_head.next)

        while head and new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        
        return True
    
    def reverse_ll(self, head):
        prev = None
        curr = head

        while curr:
            rem = curr.next
            curr.next = prev
            prev = curr
            curr = rem

        return prev