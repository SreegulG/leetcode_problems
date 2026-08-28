# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        new_head = dummy
        
        while head:
            print(head.val)
            if head.val != val:
                print(head.val)
                dummy.next = head
                dummy = dummy.next
            head = head.next
        if dummy.next and dummy.next.val == val:
            dummy.next = None
        return new_head.next